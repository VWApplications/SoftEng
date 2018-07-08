from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf, typeOf
from resource.prefix import knowledge
from .algorithmic_analysis import AlgorithmicAnalysis
from .algorithmic_analysis_strategies import AlgorithmicAnalysisStrategies
from .algorithmic_design_strategies import AlgorithmicDesignStrategies
from .attributes_of_algorithms import AttributesOfAlgorithms
from .overview_of_algorithms import OverviewOfAlgorithms

text = """
Programs are not random pieces of code: they are meticulously written to perform user-expected actions. The guide one uses to compose programs are algorithms, which organize various functions into a series of steps and take into consideration the application domain, the solution strategy, and the data structures being used. An algorithm can be very simple or very complex.
"""


class AlgorithmsAndComplexity(object):
    """
    Topic: Algorithms and Complexity
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(knowledge + 'Algorithms_and_Complexity'),
            typeOf,
            URIRef(knowledge + 'Topic'),
        ))
        graph.add((
            URIRef(knowledge + 'Algorithms_and_Complexity'),
            subClassOf,
            URIRef(knowledge + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(knowledge + 'Algorithms_and_Complexity'),
            title,
            Literal('Algorithms and Complexity', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Algorithms_and_Complexity'),
            description,
            Literal(text, datatype=XSD.string)
        ))

        self.graph = graph

        self.create_subtopics()

    def create_subtopics(self):
        """
        Create subtopics.
        """

        AlgorithmicAnalysis(self.graph)
        AlgorithmicAnalysisStrategies(self.graph)
        AlgorithmicDesignStrategies(self.graph)
        AttributesOfAlgorithms(self.graph)
        OverviewOfAlgorithms(self.graph)
