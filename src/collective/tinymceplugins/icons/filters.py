from bs4 import BeautifulSoup
from plone.outputfilters.interfaces import IFilter
from zope.component import getMultiAdapter
from zope.interface import implementer
from .interfaces import IBrowserLayer


@implementer(IFilter)
class IconFilter:
    order = 999999

    def __init__(self, context=None, request=None):
        self.context = context
        self.request = request

    def is_enabled(self):
        """enable only if the product is installed"""
        return IBrowserLayer.providedBy(self.request)

    def __call__(self, data):
        if not data:
            return data

        soup = BeautifulSoup(data, "html.parser")
        placeholders = soup.find_all("img", class_="plone-icon-placeholder")
        if not placeholders:
            return data

        iconresolver = getMultiAdapter(
            (self.context, self.request), name="iconresolver"
        )

        for img in placeholders:
            src = img.get("src", "")
            if "@@iconresolver/" not in src:
                continue

            icon_name = src.split("@@iconresolver/")[-1]
            if not icon_name:
                continue

            try:
                # Get the SVG markup
                svg_markup = iconresolver.tag(icon_name)
                if svg_markup:
                    # Create a new soup fragment for the SVG
                    svg_soup = BeautifulSoup(svg_markup, "html.parser")
                    # Replace the img tag with the SVG
                    img.replace_with(svg_soup)
            except Exception:  # noqa: S112
                continue

        return str(soup)
