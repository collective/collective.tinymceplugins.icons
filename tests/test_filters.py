from collective.tinymceplugins.icons.filters import IconFilter
from zope.component import getMultiAdapter
from zope.interface import implementer


class MockIconResolver:
    def tag(self, name):
        if name == "home":
            return '<svg class="icon-home"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>'
        return None


class TestFilters:
    def test_icon_filter_transformation(self, portal, request):
        # We need to register a mock iconresolver because the test environment might not have icons
        portal.restrictedTraverse = lambda path: (
            MockIconResolver() if path == "@@iconresolver" else None
        )

        # Manually register the mock iconresolver for the test
        from zope.component import provideAdapter
        from zope.interface import Interface

        @implementer(Interface)
        class MockResolverAdapter:
            def __init__(self, context, request):
                self.context = context
                self.request = request

            def tag(self, name):
                return MockIconResolver().tag(name)

        provideAdapter(
            MockResolverAdapter, (Interface, Interface), Interface, name="iconresolver"
        )

        filter = IconFilter(portal, request)
        data = '<p>Icon: <img class="plone-icon-placeholder" src="@@iconresolver/home"></p>'
        result = filter(data)

        assert '<svg class="icon-home">' in result
        # BeautifulSoup might normalize the output (e.g. adding closing tags)
        assert 'path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"' in result
        assert "<img" not in result

    def test_icon_filter_no_placeholder(self, portal, request):
        filter = IconFilter(portal, request)
        data = "<p>No icon here</p>"
        result = filter(data)
        assert result == data
