from core import Query, Sesame
from django.template.defaultfilters import slugify


class CoreProfessionalContent(object):
    """
    Core professional content to software engineering curriculum.
    """

    def __init__(self):
        """
        Create the core professional content model.
        """

        result = self.get_information()

        self.title = result['title']['value']
        self.description = result['description']['value']
        self.disciplines = self.get_disciplines()
        self.slug = slugify(self.title)

    def get_information(self):
        """
        Get the data from triple store.
        """

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              pp:Core_Professional_Content dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_disciplines(self):
        """
        Get all discipline of core professional content.
        """

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title
            WHERE {
              ?disciplines pp:isPartOf pp:Core_Professional_Content ;
              dc:title ?title
            }
        """

        result = Query.run(Sesame.endpoint, query)

        disciplines = []
        for discipline in result:
            disciplines.append(discipline['title']['value'])

        return disciplines
