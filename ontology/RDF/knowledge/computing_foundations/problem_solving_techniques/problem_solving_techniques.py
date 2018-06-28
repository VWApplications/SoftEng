from rdflib import URIRef, Literal
from .definition_of_problem_solving import DefinitionOfProblemSolving
from .formulating_the_real_problem import FormulatingTheRealProblem
from .analyze_the_problem import AnalyzeTheProblem
from .design_a_solution_search_strategy import DesignASolutionSearchStrategy
from .problem_solving_using_programs import ProblemSolvingUsingPrograms

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class ProblemSolvingTechniques(object):
    """
    Topic: Problem Solving Techniques
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(es + 'Problem_Solving_Techniques'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(es + 'Problem_Solving_Techniques'),
            URIRef(dc + 'title'),
            Literal('Problem Solving Techniques', lang='en')
        ))
        graph.add((
            URIRef(es + 'Problem_Solving_Techniques'),
            URIRef(dc + 'description'),
            Literal("""
                The concepts, notions, and terminology introduced here form an
                underlying basis for understanding the role and scope of
                problem solving techniques.
            """, lang='en')
        ))

        self.graph = graph

        self.create_subtopics()

    def create_subtopics(self):
        """
        Create subtopics.
        """

        DefinitionOfProblemSolving(self.graph)
        FormulatingTheRealProblem(self.graph)
        AnalyzeTheProblem(self.graph)
        DesignASolutionSearchStrategy(self.graph)
        ProblemSolvingUsingPrograms(self.graph)
