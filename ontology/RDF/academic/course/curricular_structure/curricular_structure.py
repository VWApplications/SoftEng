from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp
from .credit_system import CreditSystem
from .semi_serial import SemiSerial
from .serial_system import SerialSystem


class CurricularStructure(object):
    """
    Curricular Structure
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Curricular_Structure'),
            subClassOf,
            URIRef(pp + 'Course_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Curricular_Structure'),
            title,
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
