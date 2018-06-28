from rdflib import URIRef, Literal
from .classification import Classification
from .curriculum_contents import CurriculumContents
from .discipline import Discipline
from .semester import Semester

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class DisciplineDomain(object):
    """
    Discipline Domain
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Discipline_Domain'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Course_Domain'),
        ))
        graph.add((
            URIRef(es + 'Discipline_Domain'),
            URIRef(dc + 'title'),
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
