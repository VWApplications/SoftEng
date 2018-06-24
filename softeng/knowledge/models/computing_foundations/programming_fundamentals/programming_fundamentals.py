from core import Query, Sesame
from .programming_paradigms import ProgrammingParadigms
from .the_programming_process import TheProgrammingProcess


class ProgrammingFundamentals(object):
    """
    Topic: Programming Fundamentals
    """

    PROGRAMMING_PARADIGMS = 0
    THE_PROGRAMMING_PROCESS = 1

    def __init__(self):
        """
        Create a topic.
        """

        result = self.get_information()

        self.title = result['title']['value']
        self.description = result['description']['value']

    def get_information(self):
        """
        Get the information from triple store
        """

        query = """
            PREFIX es: <http://www.semanticweb.org/ontologies/2018/Software_Engineering/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              es:Programming_Fundamentals dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic):
        """
        Get a specific subtopic.
        """

        if subtopic == self.PROGRAMMING_PARADIGMS:
            return ProgrammingParadigms()
        elif subtopic == self.THE_PROGRAMMING_PROCESS:
            return TheProgrammingProcess()
        else:
            return None
