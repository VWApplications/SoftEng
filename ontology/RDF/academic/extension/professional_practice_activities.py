from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp

text = """
Participation in the Executive Board of the Junior Engineering Company (EJEL), participation in projects carried out by EJEL, extracurricular internships in the technical area, technological development projects in companies.
"""


class ProfessionalPracticeActivities(object):
    """
    Professional Practice Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Professional_Practice_Activities'),
            subClassOf,
            URIRef(pp + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(pp + 'Professional_Practice_Activities'),
            title,
            Literal('Professional Practice Activities', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Professional_Practice_Activities'),
            description,
            Literal(text, datatype=XSD.string)
        ))
