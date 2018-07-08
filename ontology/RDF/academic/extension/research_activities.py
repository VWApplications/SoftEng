from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp

text = """
Participation in research centers or projects of scientific initiation Institutional Program of Scientific Initiation Grants (PIBIC), publication of works, participation in seminars and scientific initiation events related to graduation.
"""


class ResearchActivities(object):
    """
    Research Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Research_Activities'),
            subClassOf,
            URIRef(pp + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(pp + 'Research_Activities'),
            title,
            Literal('Research Activities', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Research_Activities'),
            description,
            Literal(text, datatype=XSD.string)
        ))
