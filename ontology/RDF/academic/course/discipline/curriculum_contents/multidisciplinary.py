from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import pp

text = """
Multidisciplinary Projects, that is, there is the participation of other courses.
"""


class Multidisciplinary(object):
    """
    Multidisciplinary
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Multidisciplinary'),
            subClassOf,
            URIRef(pp + 'Curriculum_Contents'),
        ))
        graph.add((
            URIRef(pp + 'Multidisciplinary'),
            title,
            Literal('Multidisciplinary', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Multidisciplinary'),
            description,
            Literal(text, datatype=XSD.string)
        ))
