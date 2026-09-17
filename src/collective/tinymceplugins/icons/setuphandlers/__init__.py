import json
from plone.base.interfaces.controlpanel import ITinyMCESchema
from plone.base.interfaces.installable import INonInstallable
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import implementer


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [
            "collective.tinymceplugins.icons:uninstall",
        ]

    def getNonInstallableProducts(self):
        """Hide the upgrades package from site-creation and quickinstaller."""
        return [
            "collective.tinymceplugins.icons.upgrades",
        ]


def post_install(context):
    """Post install script"""
    registry = getUtility(IRegistry)
    settings = registry.forInterface(ITinyMCESchema, prefix="plone", check=False)

    # Add custom plugin
    custom_plugins = list(settings.custom_plugins or [])
    # Check if plugin already exists
    if not any(p.startswith("ploneicons|") for p in custom_plugins):
        custom_plugins.append(
            "ploneicons|++plone++collective.tinymceplugins.icons/plugin.js"
        )
        settings.custom_plugins = custom_plugins

    # Add button to toolbar string
    toolbar = settings.toolbar or ""
    if "ploneicons" not in toolbar:
        # Append to the first toolbar line if it exists
        lines = toolbar.split("\n")
        if lines:
            lines[0] += " ploneicons"
        else:
            lines = ["ploneicons"]
        settings.toolbar = "\n".join(lines)


def post_uninstall(context):
    """Uninstall script"""
    registry = getUtility(IRegistry)
    settings = registry.forInterface(ITinyMCESchema, prefix="plone", check=False)

    # Remove custom plugin
    custom_plugins = list(settings.custom_plugins or [])
    if any(p.startswith("ploneicons|") for p in custom_plugins):
        custom_plugins = [p for p in custom_plugins if not p.startswith("ploneicons|")]
        settings.custom_plugins = custom_plugins

    # Remove button from toolbar string
    toolbar = settings.toolbar or ""
    if "ploneicons" in toolbar:
        toolbar = toolbar.replace(" ploneicons", "").replace("ploneicons", "")
        settings.toolbar = toolbar
