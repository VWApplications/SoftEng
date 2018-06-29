from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge

text = """
The attributes of algorithms are many and often include modularity, correctness, maintainability, functionality, robustness, user-friendliness (i.e. easy to be understood by people), programmer time, simplicity, and extensibility. A commonly emphasized attribute is “performance” or “efficiency” by which we mean both time and resource-usage efficiency while generally emphasizing the time axis.  To some degree, efficiency determines if an algorithm is feasible or impractical. For example, an algorithm that takes one hundred years to terminate is virtually useless and is even considered incorrect.
"""


class AttributesOfAlgorithms(object):
    """
    Subtopic: Attributes of Algorithms
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Attributes_of_Algorithms'),
            subClassOf,
            URIRef(knowledge + 'Algorithms_and_Complexity'),
        ))
        graph.add((
            URIRef(knowledge + 'Attributes_of_Algorithms'),
            title,
            Literal('Attributes of Algorithms', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Attributes_of_Algorithms'),
            description,
            Literal(text, datatype=XSD.string)
        ))
