from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp

text = """
Students follow pre-determined lists of disciplines per semester or school year.
"""


class SerialSystem(object):
    """
    Serial System
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Serial_System'),
            subClassOf,
            URIRef(pp + 'Curricular_Structure'),
        ))
        graph.add((
            URIRef(pp + 'Serial_System'),
            title,
            Literal('Serial System', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Serial_System'),
            description,
            Literal(text, datatype=XSD.string)
        ))
