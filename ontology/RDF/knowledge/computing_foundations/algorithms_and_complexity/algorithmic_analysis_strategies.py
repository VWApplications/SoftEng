from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class AlgorithmicAnalysisStrategies(object):
    """
    Subtopic: Algorithmic Analysis Strategies
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Algorithmic_Analysis_Strategies'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Algorithms_and_Complexity'),
        ))
        graph.add((
            URIRef(es + 'Algorithmic_Analysis_Strategies'),
            URIRef(dc + 'title'),
            Literal('Algorithmic Analysis Strategies', lang='en')
        ))
        graph.add((
            URIRef(es + 'Algorithmic_Analysis_Strategies'),
            URIRef(dc + 'description'),
            Literal("""
                The analysis strategies of algorithms include basic counting
                analysis, in which one actually counts the number of steps an
                algorithm takes to complete its task; asymptotic analysis, in
                which one only considers the order of magnitude of the number
                of steps an algorithm takes to complete its task; probabilistic
                analysis, in which one makes use of probabilities in analyzing
                the average performance of an algorithm; amortized analysis, in
                which one uses the methods of aggregation, potential, and
                accounting to analyze the worst performance of an algorithm on
                a sequence of operations; and competitive analysis, in which
                one uses methods such as potential and accounting to analyze
                the relative performance of an algorithm to the optimal
                algorithm. For complex problems and algorithms, one may need to
                use a combination of the aforementioned analysis strategies.
            """, lang='en')
        ))
