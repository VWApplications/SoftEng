from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import pp

text = """
The disciplines that constitute complementary training and free training enable
the student to be co-responsible for the construction of his / her curriculum,
with training in his or her area of greatest interest, and not only a
generalized theoretical and practical training. Free training, disciplines
categorized as free module, consists of activities / disciplines developed by
the student based on their personal interests, which are not part of the
activities of the basic cycle, nor of the professional, complementary /
optional or integrative. They can be taken at any of the University's campuses.
"""


class FreeModule(object):
    """
    Free Module
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Free_Module'),
            subClassOf,
            URIRef(pp + 'Curriculum_Contents'),
        ))
        graph.add((
            URIRef(pp + 'Free_Module'),
            title,
            Literal('Free Module', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Free_Module'),
            description,
            Literal(text, datatype=XSD.string)
        ))
