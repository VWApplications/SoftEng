from core import Query, Sesame
from django.template.defaultfilters import slugify
from .alternate_abstractions import AlternateAbstractions
from .encapsulation import Encapsulation
from .hierarchy import Hierarchy
from .levels_of_abstraction import LevelsOfAbstraction


class Abstraction(object):
    """
    Topic: Abstraction
    """

    ALTERNATE_ABSTRACTIONS = 0
    ENCAPSULATION = 1
    HIERARCHY = 2
    LEVELS_OF_ABSTRACTION = 3

    def __init__(self):
        """
        Create a topic.
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
            PREFIX knowledge: <http://www.semanticweb.org/ontologies/2018/Knowledge/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              knowledge:Abstraction dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic=None):
        """
        Get a specific subtopic.
        """

        if subtopic == self.ALTERNATE_ABSTRACTIONS:
            return AlternateAbstractions()
        elif subtopic == self.ENCAPSULATION:
            return Encapsulation()
        elif subtopic == self.HIERARCHY:
            return Hierarchy()
        elif subtopic == self.LEVELS_OF_ABSTRACTION:
            return LevelsOfAbstraction()
        else:
            return [
                AlternateAbstractions(),
                Encapsulation(),
                Hierarchy(),
                LevelsOfAbstraction()
            ]
