import json
from Products.Five import BrowserView
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


class IconsJsonView(BrowserView):
    def __call__(self):
        self.request.response.setHeader("Content-Type", "application/json")
        factory = getUtility(
            IVocabularyFactory, name="collective.tinymceplugins.icons.Icons"
        )
        vocabulary = factory(self.context)
        results = [{"id": term.value, "text": term.title} for term in vocabulary]
        return json.dumps({"results": results})
