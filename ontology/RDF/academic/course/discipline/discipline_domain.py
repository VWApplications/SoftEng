from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp
from .classification import Classification
from .curriculum_contents import CurriculumContents
from .discipline import Discipline
from .semester import Semester


class DisciplineDomain(object):
    """
    Discipline Domain
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Discipline_Domain'),
            subClassOf,
            URIRef(pp + 'Course_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Discipline_Domain'),
            title,
            Literal('Discipline Domain', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        Classification(self.graph)
        CurriculumContents(self.graph)
        Discipline(self.graph)
        Semester(self.graph)
