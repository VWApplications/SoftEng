from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import knowledge
from .abstraction import Abstraction
from .algorithms_and_complexity import AlgorithmsAndComplexity
from .basic_concept_of_a_system import BasicConceptOfASystem
from .basic_developer_human_factors import BasicDeveloperHumanFactors
from .basic_user_human_factors import BasicUserHumanFactors
from .problem_solving_techniques import ProblemSolvingTechniques
from .programming_fundamentals import ProgrammingFundamentals

text = """
The scope of the Computing Foundations knowledge area (KA) encompasses the development and operational environment in which software evolves and executes.  Because no software can exist in a vacuum or run without a computer, the core of such an environment is the computer and its various components.  Knowledge about the computer and its underlying principles of hardware and software serves as a framework on which software engineering is anchored.  Thus, all software engineers must have good understanding of the Computing Foundations KA. It is generally accepted that software engineering builds on top of computer science.  For example, Software Engineering 2004: Curriculum Guidelines for Undergraduate Degree Programs in Software Engineering clearly states, One particularly important aspect is that software engineering builds on computer science and mathematics (italics added).
"""


class ComputingFoundations(object):
    """
    Computing Foundations Knowledge Area.
    """

    def __init__(self, graph):
        """
        Create the Computing Foundations knowledge
        """

        graph.add((
            URIRef(knowledge + 'Computing_Foundations'),
            subClassOf,
            URIRef(knowledge + 'Knowledge_Area'),
        ))
        graph.add((
            URIRef(knowledge + 'Computing_Foundations'),
            title,
            Literal('Computing Foundations', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Computing_Foundations'),
            description,
            Literal(text, datatype=XSD.string)
        ))

        self.graph = graph

        self.create_topics()

    def create_topics(self):
        """
        Create all topics
        """

        Abstraction(self.graph)
        AlgorithmsAndComplexity(self.graph)
        BasicConceptOfASystem(self.graph)
        BasicDeveloperHumanFactors(self.graph)
        BasicUserHumanFactors(self.graph)
        ProblemSolvingTechniques(self.graph)
        ProgrammingFundamentals(self.graph)
