from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge

text = """
The uniqueness of computer software gives problem solving a flavor that is distinct from general engineering problem solving. To solve a problem using computers, we must answer the following questions. How do we figure out what to tell the computer to do? How do we convert the problem statement into an algorithm? How do we convert the algorithm into machine instructions? The first task in solving a problem using a computer is to determine what to tell the computer to do. There may be many ways to tell the story, but all should take the perspective of a computer such that the computer can eventually solve the problem. In general, a problem should be expressed in such a way as to facilitate the development of algorithms and data structures for solving it.  The result of the first task is a problem statement. The next step is to convert the problem statement into algorithms that solve the problem. Once an algorithm is found, the final step converts the algorithm into machine instructions that form the final solution: software that solves the problem.  Abstractly speaking, problem solving using a computer can be considered as a process of problem transformation in other words, the step-bystep transformation of a problem statement into a problem solution.  To the discipline of software engineering, the ultimate objective of problem solving is to transform a problem expressed in natural language into electrons running around a circuit.
"""


class ProblemSolvingUsingPrograms(object):
    """
    Subtopic: Problem Solving Using Programs
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Problem_Solving_Using_Programs'),
            subClassOf,
            URIRef(knowledge + 'Problem_Solving_Techniques'),
        ))
        graph.add((
            URIRef(knowledge + 'Problem_Solving_Using_Programs'),
            title,
            Literal('Problem Solving Using Programs', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Problem_Solving_Using_Programs'),
            description,
            Literal(text, datatype=XSD.string)
        ))
