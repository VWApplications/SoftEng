from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp
from .calculo_1 import Calculo1
from .calculo_2 import Calculo2


class Discipline(object):
    """
    Discipline Domain
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Discipline'),
            subClassOf,
            URIRef(pp + 'Discipline_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Discipline'),
            title,
            Literal('Discipline', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        Calculo1(self.graph)
        Calculo2(self.graph)
