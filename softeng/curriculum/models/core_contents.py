from django.template.defaultfilters import slugify
from core import Query, Sesame
from .core_content import (
    CoreBasicContent, CoreProfessionalContent,
    CoreSpecificContent, FreeModule, Multidisciplinary
)


class CoreContent(object):
    """
    Core Contents
    """

    CORE_BASIC_CONTENT = 0
    CORE_PROFESSIONAL_CONTENT = 1
    CORE_SPECIFIC_CONTENT = 2
    FREE_MODULE = 3
    MULTIDISCIPLINARY = 4

    def __init__(self):
        """
        Create a knowledge area.
        """

        result = self.get_information()

        self.title = result['title']['value']
        self.description = result['description']['value']
        self.slug = slugify(self.title)

    def get_information(self):
        """
        Get the information from triple store
        """

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              pp:Core_Content dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_instance(self, instance=None):
        """
        Get core content.
        """

        if instance == self.CORE_BASIC_CONTENT:
            return CoreBasicContent()
        elif instance == self.CORE_PROFESSIONAL_CONTENT:
            return CoreProfessionalContent()
        elif instance == self.CORE_SPECIFIC_CONTENT:
            return CoreSpecificContent()
        elif instance == self.FREE_MODULE:
            return FreeModule()
        elif instance == self.MULTIDISCIPLINARY:
            return Multidisciplinary()
        else:
            return [
                CoreBasicContent(),
                CoreProfessionalContent(),
                CoreSpecificContent(),
                FreeModule(),
                Multidisciplinary()
            ]
