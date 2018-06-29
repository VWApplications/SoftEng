from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import pp

text = """
Courses addressing the fundamentals and specific topics of Software
Engineering, as well as other specific contents aimed at the development of
specific or complementary skills and abilities in the area of programming,
product and software process.

Example: Specific disciplines for software engineering
"""


class CoreSpecificContent(object):
    """
    Core Specific Content
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Core_Specific_Content'),
            subClassOf,
            URIRef(pp + 'Core_Content'),
        ))
        graph.add((
            URIRef(pp + 'Core_Specific_Content'),
            title,
            Literal('Core Specific Content', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Core_Specific_Content'),
            description,
            Literal(text, datatype=XSD.string)
        ))
