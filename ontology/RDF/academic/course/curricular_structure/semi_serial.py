from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import pp

text = """
The semi-serial system is an academic structure that combines characteristics of the serial system and the credit system.

This system allows great flexibility in the construction of a study plan by the students, but creates a difficulty of managing vacancies. In the semi-serial system, the flexibility of the credit system is contemplated, but the formative trajectory is oriented around a reference flow chart, by means of preference of places: the student who fully fulfills the disciplines for a semester have their job preferably processed in the subjects of the following semester.
"""


class SemiSerial(object):
    """
    Semi Serial System
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Semi_Serial'),
            subClassOf,
            URIRef(pp + 'Curricular_Structure'),
        ))
        graph.add((
            URIRef(pp + 'Semi_Serial'),
            title,
            Literal('Semi Serial System', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Semi_Serial'),
            description,
            Literal(text, datatype=XSD.string)
        ))
