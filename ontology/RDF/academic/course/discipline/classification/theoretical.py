from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class Theoretical(object):
    """
    Theoretical
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Theoretical'),
            subClassOf,
            URIRef(pp + 'Classification'),
        ))
        graph.add((
            URIRef(pp + 'Theoretical'),
            title,
            Literal('Theoretical', lang='en')
        ))
