from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.registry import field
from plone.registry.interfaces import IRegistry
from plone.registry.record import Record
from zope.component import getUtility

import json


class TestBrowser:
    def test_icons_json_view(self, portal, integration):
        setRoles(portal, TEST_USER_ID, ["Manager"])
        registry = getUtility(IRegistry)
        registry.records["plone.icon.test-browser-icon"] = Record(
            field.TextLine(), "test-browser-icon"
        )

        view = portal.restrictedTraverse("@@tinymce-icons-json")
        result = json.loads(view())

        results = [item["id"] for item in result["results"]]
        assert "test-browser-icon" in results

        # Clean up
        del registry.records["plone.icon.test-browser-icon"]
