from collective.tinymceplugins.icons import PACKAGE_NAME
from plone.base.interfaces.controlpanel import IFilterSchema
from plone.base.interfaces.controlpanel import ITinyMCESchema
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

import json


class TestRegistry:
    def test_tinymce_custom_plugins_installed(self, integration):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ITinyMCESchema, prefix="plone", check=False)
        custom_plugins = settings.custom_plugins
        assert any(
            "ploneicons|++plone++collective.tinymceplugins.icons/plugin.js" in p
            for p in custom_plugins
        )

    def test_tinymce_toolbar_installed(self, integration):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ITinyMCESchema, prefix="plone", check=False)
        assert "ploneicons" in settings.toolbar

    def test_html_filter_tags_installed(self, integration):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IFilterSchema, prefix="plone", check=False)
        assert "svg" in settings.valid_tags
        assert "path" in settings.valid_tags

    def test_html_filter_attributes_installed(self, integration):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IFilterSchema, prefix="plone", check=False)
        assert "viewbox" in settings.custom_attributes
        assert "d" in settings.custom_attributes

    def test_resource_bundle_installed(self, integration):
        registry = getUtility(IRegistry)
        key = "plone.bundles/collective-tinymceplugins-icons.enabled"
        assert key in registry
        assert registry[key] is True
