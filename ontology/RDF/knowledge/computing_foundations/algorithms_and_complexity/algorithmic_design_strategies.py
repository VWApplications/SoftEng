from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class AlgorithmicDesignStrategies(object):
    """
    Subtopic: Algorithmic Design Strategies
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Algorithmic_Design_Strategies'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Algorithms_and_Complexity'),
        ))
        graph.add((
            URIRef(es + 'Algorithmic_Design_Strategies'),
            URIRef(dc + 'title'),
            Literal('Algorithmic Design Strategies', lang='en')
        ))
        graph.add((
            URIRef(es + 'Algorithmic_Design_Strategies'),
            URIRef(dc + 'description'),
            Literal("""
                The design of algorithms generally follows one of the following
                strategies: brute force, divide and conquer, dynamic
                programming, and greedy selection. The brute force strategy is
                actually a no-strategy. It exhaustively tries every possible
                way to tackle a problem. If a problem has a solution, this
                strategy is guaranteed to find it; however, the time expense
                may be too high. The divide and conquer strategy improves on
                the brute force strategy by dividing a big problem into
                smaller, homogeneous problems. It solves the big problem by
                recursively solving the smaller problems and combing the
                solutions to the smaller problems to form the solution to the
                big problem. The underlying assumption for divide and conquer
                is that smaller problems are easier to solve. The dynamic
                programming strategy improves on the divide and conquer
                strategy by recognizing that some of the sub-problems produced
                by division may be the same and thus avoids solving the same
                problems again and again. This elimination of redundant
                subproblems can dramatically improve efficiency. The greedy
                selection strategy further improves
                on dynamic programming by recognizing that not all of the
                sub-problems contribute to the solution of the big problem. By
                eliminating all but one sub-problem, the greedy selection
                strategy achieves the highest efficiency among all algorithm
                design strategies. Sometimes the use of randomization can
                improve on the greedy selection strategy by eliminating the
                complexity in determining the greedy choice through coin
                flipping or randomization.
            """, lang='en')
        ))
