from rdflib import URIRef, Literal
from .credit_system import CreditSystem
from .semi_serial import SemiSerial
from .serial_system import SerialSystem

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class CurricularStructure(object):
    """
    Curricular Structure
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Curricular_Structure'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Course_Domain'),
        ))
        graph.add((
            URIRef(es + 'Curricular_Structure'),
            URIRef(dc + 'title'),
            Literal('Curricular Structure', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        CreditSystem(self.graph)
        SemiSerial(self.graph)
        SerialSystem(self.graph)
