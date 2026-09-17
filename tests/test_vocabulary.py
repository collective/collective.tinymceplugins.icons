from plone.registry import field
from plone.registry.interfaces import IRegistry
from plone.registry.record import Record
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


class TestVocabulary:
    def test_vocabulary_registered(self, integration):
        name = "collective.tinymceplugins.icons.Icons"
        factory = getUtility(IVocabularyFactory, name=name)
        assert factory is not None

    def test_vocabulary_discovery(self, portal, integration):
        registry = getUtility(IRegistry)
        # Mock an icon in registry correctly
        registry.records["plone.icon.test-icon"] = Record(field.TextLine(), "test-icon")

        name = "collective.tinymceplugins.icons.Icons"
        factory = getUtility(IVocabularyFactory, name=name)
        vocabulary = factory(portal)

        assert "test-icon" in [term.value for term in vocabulary]

        # Clean up
        del registry.records["plone.icon.test-icon"]
