from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp

text = """
Effective participation in the Academic Center and Engineering Academic Directory, student representation in collegiate bodies.
"""


class ActivitiesOfStudentRepresentations(object):
    """
    Activities of Student Representations
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Activities_of_Student_Representations'),
            subClassOf,
            URIRef(pp + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(pp + 'Activities_of_Student_Representations'),
            title,
            Literal('Activities of Student Representations', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Activities_of_Student_Representations'),
            description,
            Literal(text, datatype=XSD.string)
        ))
