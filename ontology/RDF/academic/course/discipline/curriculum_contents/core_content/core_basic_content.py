from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import pp

text = """
Required by opinion CNE / CES 136 of 2012 (Curricular Guidelines for Graduation
in Computing).

Example: Scientific and Technological Methodology, Communication and
Expression, Graphic Expression, Mathematics, Physics, Production, Innovation,
Administration, Economics, Environmental Sciences, Humanities, Social Sciences,
Citizenship.
"""


class CoreBasicContent(object):
    """
    Core Basic Content
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Core_Basic_Content'),
            subClassOf,
            URIRef(pp + 'Core_Content'),
        ))
        graph.add((
            URIRef(pp + 'Core_Basic_Content'),
            title,
            Literal('Core Basic Content', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Core_Basic_Content'),
            description,
            Literal(text, datatype=XSD.string)
        ))
