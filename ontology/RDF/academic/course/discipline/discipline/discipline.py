from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp


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
