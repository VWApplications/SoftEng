from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp

text = """
Monitoring of course subjects, technical course teacher, etc.
"""


class TeachingActivities(object):
    """
    Teaching Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Teaching_Activities'),
            subClassOf,
            URIRef(pp + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(pp + 'Teaching_Activities'),
            title,
            Literal('Teaching Activities', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Teaching_Activities'),
            description,
            Literal(text, datatype=XSD.string)
        ))
