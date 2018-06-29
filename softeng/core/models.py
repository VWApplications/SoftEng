from core import Query, Sesame


class SoftwareEngineering(object):
    """
    Class to get information about Software Enginering.
    """

    def __init__(self):
        """
        Create Software Engineering model.
        """

        result = self.get_information()
        self.title = result['title']['value']
        self.description = result['description']['value']

    def get_information(self):
        """
        Get all information about software engineering ontology
        """

        query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              pp:Software_Engineering dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]
