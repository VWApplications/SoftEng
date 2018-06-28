from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class FormulatingTheRealProblem(object):
    """
    Subtopic: Formulating the Real Problem
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Formulating_the_Real_Problem'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Problem_Solving_Techniques'),
        ))
        graph.add((
            URIRef(es + 'Formulating_the_Real_Problem'),
            URIRef(dc + 'title'),
            Literal('Formulating the Real Problem', lang='en')
        ))
        graph.add((
            URIRef(es + 'Formulating_the_Real_Problem'),
            URIRef(dc + 'description'),
            Literal("""
                Gerard Voland writes, “It is important to recognize that a
                specific problem should be formulated if one is to develop a
                specific solution”. This formulation is called the problem
                statement, which explicitly specifies what both the problem and
                the desired outcome are. Although there is no universal way of
                stating a problem, in general a problem should be expressed in
                such a way as to facilitate the development of solutions. Some
                general techniques to help one formulate the real problem
                include statement-restatement, determining the source and the
                cause, revising the statement, analyzing present and desired
                state, and using the fresh eye
                approach.
            """, lang='en')
        ))
