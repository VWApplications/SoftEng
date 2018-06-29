from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge
from .definition_of_problem_solving import DefinitionOfProblemSolving
from .formulating_the_real_problem import FormulatingTheRealProblem
from .analyze_the_problem import AnalyzeTheProblem
from .design_a_solution_search_strategy import DesignASolutionSearchStrategy
from .problem_solving_using_programs import ProblemSolvingUsingPrograms

text = """
The concepts, notions, and terminology introduced here form an underlying basis for understanding the role and scope of problem solving techniques.
"""


class ProblemSolvingTechniques(object):
    """
    Topic: Problem Solving Techniques
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(knowledge + 'Problem_Solving_Techniques'),
            subClassOf,
            URIRef(knowledge + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(knowledge + 'Problem_Solving_Techniques'),
            title,
            Literal('Problem Solving Techniques', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Problem_Solving_Techniques'),
            description,
            Literal(text, datatype=XSD.string)
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
