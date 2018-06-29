from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import pp

text = """
Participation in programs or NGOs related to social action, exercise of citizenship and defense of the environment.
"""


class ActivitiesOfSocial(object):
    """
    Campus Activities of Social
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Activities_of_Social'),
            subClassOf,
            URIRef(pp + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(pp + 'Activities_of_Social'),
            title,
            Literal('Activities of Social Action, Citizenship and Environment', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Activities_of_Social'),
            description,
            Literal(text, datatype=XSD.string)
        ))
