from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class FullTime(object):
    """
    Full Time
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Full_Time'),
            subClassOf,
            URIRef(pp + 'Period'),
        ))
        graph.add((
            URIRef(pp + 'Full_Time'),
            title,
            Literal('Full Time', lang='en')
        ))
