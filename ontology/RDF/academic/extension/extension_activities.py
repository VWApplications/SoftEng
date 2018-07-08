from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp

text = """
Courses in the technical or business management area, foreign language courses, extension projects with the community Institutional Program of Extension Scholarships (PIBEX), Continuous Action Extension Projects (PEAC), participation in Engineering Week.
"""


class ExtensionActivities(object):
    """
    Extension Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Extension_Activities'),
            subClassOf,
            URIRef(pp + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(pp + 'Extension_Activities'),
            title,
            Literal('Extension Activities', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Extension_Activities'),
            description,
            Literal(text, datatype=XSD.string)
        ))
