from core import Query, Sesame
from django.template.defaultfilters import slugify
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

        self.uri = "http://www.semanticweb.org/ontologies/2018/Knowledge/Programming_Fundamentals"
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
              knowledge:Programming_Fundamentals dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic=None):
        """
        Get a specific subtopic.
        """

        if subtopic == self.PROGRAMMING_PARADIGMS:
            return ProgrammingParadigms()
        elif subtopic == self.THE_PROGRAMMING_PROCESS:
            return TheProgrammingProcess()
        else:
            return [
                ProgrammingParadigms(),
                TheProgrammingProcess()
            ]
