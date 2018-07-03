from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf, typeOf
from RDF.prefix import knowledge

text = """
The analysis strategies of algorithms include basic counting analysis, in which one actually counts the number of steps an algorithm takes to complete its task; asymptotic analysis, in which one only considers the order of magnitude of the number of steps an algorithm takes to complete its task; probabilistic analysis, in which one makes use of probabilities in analyzing the average performance of an algorithm; amortized analysis, in which one uses the methods of aggregation, potential, and accounting to analyze the worst performance of an algorithm on a sequence of operations; and competitive analysis, in which one uses methods such as potential and accounting to analyze the relative performance of an algorithm to the optimal algorithm. For complex problems and algorithms, one may need to use a combination of the aforementioned analysis strategies.
"""


class AlgorithmicAnalysisStrategies(object):
    """
    Subtopic: Algorithmic Analysis Strategies
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Algorithmic_Analysis_Strategies'),
            typeOf,
            URIRef(knowledge + 'Subtopic'),
        ))
        graph.add((
            URIRef(knowledge + 'Algorithmic_Analysis_Strategies'),
            subClassOf,
            URIRef(knowledge + 'Algorithms_and_Complexity'),
        ))
        graph.add((
            URIRef(knowledge + 'Algorithmic_Analysis_Strategies'),
            title,
            Literal('Algorithmic Analysis Strategies', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Algorithmic_Analysis_Strategies'),
            description,
            Literal(text, datatype=XSD.string)
        ))
