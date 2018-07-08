from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class Practical(object):
    """
    Practical
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Practical'),
            subClassOf,
            URIRef(pp + 'Classification'),
        ))
        graph.add((
            URIRef(pp + 'Practical'),
            title,
            Literal('Required', lang='en')
        ))
