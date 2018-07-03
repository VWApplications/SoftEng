from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf, typeOf
from RDF.prefix import knowledge

text = """
When abstracting, we concentrate on one “level” of the big picture at a time with confidence that we can then connect effectively with levels above and below. Although we focus on one level, abstraction does not mean knowing nothing about the neighboring levels. Abstraction levels do not necessarily correspond to discrete components in reality or in the problem domain, but to welldefined standard interfaces such as programming APIs. The advantages that standard interfaces provide include portability, easier software/hardware integration and wider usage.
"""


class LevelsOfAbstraction(object):
    """
    Subtopic: Levels of Abstration
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Levels_of_Abstraction'),
            typeOf,
            URIRef(knowledge + 'Subtopic'),
        ))
        graph.add((
            URIRef(knowledge + 'Levels_of_Abstraction'),
            subClassOf,
            URIRef(knowledge + 'Abstraction'),
        ))
        graph.add((
            URIRef(knowledge + 'Levels_of_Abstraction'),
            title,
            Literal('Levels of Abstraction', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Levels_of_Abstraction'),
            description,
            Literal(text, datatype=XSD.string)
        ))
