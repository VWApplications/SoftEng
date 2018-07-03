from core import Query, Sesame
from django.template.defaultfilters import slugify


class DesignASolutionSearchStrategy(object):
    """
    Subtopic: Design a Solution Search Strategy
    """

    def __init__(self):
        """
        Create a subtopic.
        """

        result = self.get_information()

        self.uri = "http://www.semanticweb.org/ontologies/2018/Knowledge/Design_a_Solution_Search_Strategy"
        self.title = result['title']['value']
        self.description = result['description']['value']
        self.slug = slugify(self.title)

    def get_information(self):
        """
        Get the data from triple store
        """

        query = """
            PREFIX knowledge: <http://www.semanticweb.org/ontologies/2018/Knowledge/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              knowledge:Design_a_Solution_Search_Strategy dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]
