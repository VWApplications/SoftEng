from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp

text = """
The students can study subjects at any time, observing the prerequisites.
"""


class CreditSystem(object):
    """
    Credit Systen
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Credit_System'),
            subClassOf,
            URIRef(pp + 'Curricular_Structure'),
        ))
        graph.add((
            URIRef(pp + 'Credit_System'),
            title,
            Literal('Credit System', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Credit_System'),
            description,
            Literal(text, datatype=XSD.string)
        ))
