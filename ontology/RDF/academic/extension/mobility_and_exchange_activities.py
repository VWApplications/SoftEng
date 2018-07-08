from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp

text = """
Permanent exchange with national and international institutions and companies.
"""


class MobilityAndExchangeActivities(object):
    """
    Mobility and Exchange Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Mobility_and_Exchange_Activities'),
            subClassOf,
            URIRef(pp + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(pp + 'Mobility_and_Exchange_Activities'),
            title,
            Literal('Mobility and Exchange Activities', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Mobility_and_Exchange_Activities'),
            description,
            Literal(text, datatype=XSD.string)
        ))
