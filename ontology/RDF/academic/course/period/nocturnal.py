from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class Nocturnal(object):
    """
    Nocturnal
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Nocturnal'),
            subClassOf,
            URIRef(pp + 'Period'),
        ))
        graph.add((
            URIRef(pp + 'Nocturnal'),
            title,
            Literal('Nocturnal', lang='en')
        ))
