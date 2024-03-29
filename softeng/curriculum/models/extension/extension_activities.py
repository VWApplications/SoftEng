from core import Query, Sesame
from django.template.defaultfilters import slugify


class ExtensionActivities(object):
    """
    Extension Activities.
    """

    def __init__(self):
        """
        Create Extension Activities model.
        """

        result = self.get_information()

        self.title = result['title']['value']
        self.description = result['description']['value']
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
              pp:Extension_Activities dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]
