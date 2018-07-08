from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp


text = """
Disciplines with basic vocational content that allow to reach the basic elements of the professional profile of the egress.

Example: Programming Logic, Algorithms and Data Structure, Digital Circuits, Computing, Programming Language, Database.
"""


class CoreProfessionalContent(object):
    """
    Core Professional Content
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Core_Professional_Content'),
            subClassOf,
            URIRef(pp + 'Core_Content'),
        ))
        graph.add((
            URIRef(pp + 'Core_Professional_Content'),
            title,
            Literal('Core Professional Content', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Core_Professional_Content'),
            description,
            Literal(text, datatype=XSD.string)
        ))
