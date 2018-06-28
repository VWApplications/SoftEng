from rdflib import URIRef, Literal
from .course import Course
from .curricular_structure import CurricularStructure
from .discipline import DisciplineDomain
from .period import Period

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class CourseDomain(object):
    """
    Couse Domain
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Course_Domain'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Academic_Domain'),
        ))
        graph.add((
            URIRef(es + 'Course_Domain'),
            URIRef(dc + 'title'),
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
