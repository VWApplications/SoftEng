from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class AnalyzeTheProblem(object):
    """
    Subtopic: Analyze the Problem
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Analyze_the_Problem'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Problem_Solving_Techniques'),
        ))
        graph.add((
            URIRef(es + 'Analyze_the_Problem'),
            URIRef(dc + 'title'),
            Literal('Analyze the Problem', lang='en')
        ))
        graph.add((
            URIRef(es + 'Analyze_the_Problem'),
            URIRef(dc + 'description'),
            Literal("""
                Once the problem statement is available, the next step is to
                analyze the problem statement or situation to help structure
                our search for a solution. Four types of analysis include
                situation analysis, in which the most urgent or critical
                aspects of a
                situation are identified first; problem analysis, in which the
                cause of the problem must be determined; decision analysis, in
                which the action(s) needed to correct the problem or eliminate
                its cause must be determined; and potential problem analysis,
                in which the action(s) needed to prevent any reoccurrences of
                the problem or the development of new problems must be
                determined.
            """, lang='en')
        ))
