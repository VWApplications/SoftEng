from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
The design of algorithms generally follows one of the following strategies:
brute force, divide and conquer, dynamic programming, and greedy selection.
The brute force strategy is actually a no-strategy. It exhaustively tries
every possible way to tackle a problem. If a problem has a solution, this
strategy is guaranteed to find it; however, the time expense may be too
high.  The divide and conquer strategy improves on the brute force strategy
by dividing a big problem into smaller, homogeneous problems. It solves the
big problem by recursively solving the smaller problems and combing the
solutions to the smaller problems to form the solution to the big problem.
The underlying assumption for divide and conquer is that smaller problems
are easier to solve. The dynamic programming strategy improves on the
divide and conquer strategy by recognizing that some of the sub-problems
produced by division may be the same and thus avoids solving the same
problems again and again.
"""


class AlgorithmicDesignStrategies(object):
    """
    Subtopic: Algorithmic Design Strategies
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Algorithmic_Design_Strategies'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Algorithms_and_Complexity'),
        ))
        graph.add((
            URIRef(knowledge + 'Algorithmic_Design_Strategies'),
            URIRef(dc + 'title'),
            Literal('Algorithmic Design Strategies', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Algorithmic_Design_Strategies'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))
