from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp


class Required(object):
    """
    Required
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Required'),
            subClassOf,
            URIRef(pp + 'Classification'),
        ))
        graph.add((
            URIRef(pp + 'Required'),
            title,
            Literal('Required', lang='en')
        ))
