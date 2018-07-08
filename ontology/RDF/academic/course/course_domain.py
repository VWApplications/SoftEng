from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp
from .course import Course
from .curricular_structure import CurricularStructure
from .discipline import DisciplineDomain
from .period import Period


class CourseDomain(object):
    """
    Couse Domain
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Course_Domain'),
            subClassOf,
            URIRef(pp + 'Academic_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Course_Domain'),
            title,
            Literal('Course Domain', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        Course(self.graph)
        CurricularStructure(self.graph)
        DisciplineDomain(self.graph)
        Period(self.graph)
