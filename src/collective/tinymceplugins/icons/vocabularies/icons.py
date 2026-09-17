from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class PloneIconsVocabulary:
    def __call__(self, context):
        registry = getUtility(IRegistry)
        icons = [
            k.replace("plone.icon.", "")
            for k in registry.records
            if k.startswith("plone.icon.")
        ]
        icons.sort()
        terms = [SimpleTerm(value=icon, token=icon, title=icon) for icon in icons]
        return SimpleVocabulary(terms)


PloneIconsVocabularyFactory = PloneIconsVocabulary()
