from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf, belongsTo
from RDF.prefix import pp


class FGA(object):
    """
    Campus FGA
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'FGA'),
            subClassOf,
            URIRef(pp + 'Academic_Campus'),
        ))
        graph.add((
            URIRef(pp + 'FGA'),
            belongsTo,
            URIRef(pp + 'UnB'),
        ))
        graph.add((
            URIRef(pp + 'FGA'),
            title,
            Literal('Faculty of Engineering of Gama', lang='en')
        ))
        graph.add((
            URIRef(pp + 'FGA'),
            description,
            Literal("Faculty of Engineering of Gama - FGA", datatype=XSD.string)
        ))
