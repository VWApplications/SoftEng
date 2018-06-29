from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp
from .evening import Evening
from .full_time import FullTime
from .morning import Morning
from .nocturnal import Nocturnal


class Period(object):
    """
    Course Period
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Period'),
            subClassOf,
            URIRef(pp + 'Course_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Period'),
            title,
            Literal('Course Period', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        Evening(self.graph)
        FullTime(self.graph)
        Morning(self.graph)
        Nocturnal(self.graph)
