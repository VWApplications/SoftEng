from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class Evening(object):
    """
    Evening period
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Evening'),
            subClassOf,
            URIRef(pp + 'Period'),
        ))
        graph.add((
            URIRef(pp + 'Evening'),
            title,
            Literal('Evening', lang='en')
        ))
