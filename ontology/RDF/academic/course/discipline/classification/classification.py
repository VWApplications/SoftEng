from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp
from .optional import Optional
from .practical import Practical
from .required import Required
from .theoretical import Theoretical


class Classification(object):
    """
    Discipline classification
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Classification'),
            subClassOf,
            URIRef(pp + 'Discipline_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Classification'),
            title,
            Literal('Classification', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        Optional(self.graph)
        Practical(self.graph)
        Required(self.graph)
        Theoretical(self.graph)
