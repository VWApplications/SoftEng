from django.template.defaultfilters import slugify
from core import Query, Sesame
from .computing_foundations import ComputingFoundations


class Knowledge(object):
    """
    Knowledge area
    """

    COMPUTING_FOUNDATIONS = 0

    def __init__(self):
        """
        Create a knowledge area.
        """

        result = self.get_information()

        self.uri = "http://www.semanticweb.org/ontologies/2018/Knowledge/Knowledge_Area"
        self.title = result['title']['value']
        self.description = result['description']['value']
        self.slug = slugify(self.title)

    def get_information(self):
        """
        Get the information from triple store
        """

        query = """
            PREFIX knowledge: <http://www.semanticweb.org/ontologies/2018/Knowledge/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              knowledge:Knowledge_Area dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_instance(self, instance=None):
        """
        Get core content.
        """

        if instance == self.COMPUTING_FOUNDATIONS:
            return ComputingFoundations()
        else:
            return [
                ComputingFoundations(),
            ]
