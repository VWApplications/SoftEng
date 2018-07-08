from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp
from .UnB import UnB


class AcademicInstitution(object):
    """
    Academic Institution
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Academic_Institution'),
            subClassOf,
            URIRef(pp + 'Academic_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Academic_Institution'),
            title,
            Literal('Academic Institution', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        UnB(self.graph)
