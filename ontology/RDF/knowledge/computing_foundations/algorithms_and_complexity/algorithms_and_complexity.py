from rdflib import URIRef, Literal
from .algorithmic_analysis import AlgorithmicAnalysis
from .algorithmic_analysis_strategies import AlgorithmicAnalysisStrategies
from .algorithmic_design_strategies import AlgorithmicDesignStrategies
from .attributes_of_algorithms import AttributesOfAlgorithms
from .overview_of_algorithms import OverviewOfAlgorithms

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class AlgorithmsAndComplexity(object):
    """
    Topic: Algorithms and Complexity
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(es + 'Algorithms_and_Complexity'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(es + 'Algorithms_and_Complexity'),
            URIRef(dc + 'title'),
            Literal('Algorithms and Complexity', lang='en')
        ))
        graph.add((
            URIRef(es + 'Algorithms_and_Complexity'),
            URIRef(dc + 'description'),
            Literal("""
                Programs are not random pieces of code: they are meticulously
                written to perform user-expected actions. The guide one uses to
                compose programs are algorithms, which organize various
                functions into a series of steps and take into consideration
                the application domain, the solution strategy, and the data
                structures being used. An algorithm can be very simple or very
                complex.
            """, lang='en')
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
