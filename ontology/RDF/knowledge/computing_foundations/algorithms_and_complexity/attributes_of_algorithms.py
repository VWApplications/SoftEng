from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
The attributes of algorithms are many and often include modularity,
correctness, maintainability, functionality, robustness, user-friendliness
(i.e. easy to be understood by people), programmer time, simplicity, and
extensibility. A commonly emphasized attribute is “performance” or “efficiency”
by which we mean both time and resource-usage efficiency while generally
emphasizing the time axis.  To some degree, efficiency determines if an
algorithm is feasible or impractical. For example, an algorithm that takes one
hundred years to terminate is virtually useless and is even considered
incorrect.
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
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Algorithms_and_Complexity'),
        ))
        graph.add((
            URIRef(knowledge + 'Attributes_of_Algorithms'),
            URIRef(dc + 'title'),
            Literal('Attributes of Algorithms', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Attributes_of_Algorithms'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))
