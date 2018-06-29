from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp


class Morning(object):
    """
    Morning
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Morning'),
            subClassOf,
            URIRef(pp + 'Period'),
        ))
        graph.add((
            URIRef(pp + 'Morning'),
            title,
            Literal('Morning', lang='en')
        ))
