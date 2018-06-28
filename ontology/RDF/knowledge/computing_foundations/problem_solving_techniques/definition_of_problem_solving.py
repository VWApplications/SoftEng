from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class DefinitionOfProblemSolving(object):
    """
    Subtopic: Definition of problem solving
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Definition_of_Problem_Solving'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Problem_Solving_Techniques'),
        ))
        graph.add((
            URIRef(es + 'Definition_of_Problem_Solving'),
            URIRef(dc + 'title'),
            Literal('Definition of Problem Solving', lang='en')
        ))
        graph.add((
            URIRef(es + 'Definition_of_Problem_Solving'),
            URIRef(dc + 'description'),
            Literal("""
                Problem solving refers to the thinking and activities conducted
                to answer or derive a solution to a problem. There are many
                ways to approach a problem, and each way employs different
                tools and uses different processes. These different ways of
                approaching problems gradually expand and define themselves and
                finally give rise to different disciplines. For example,
                software engineering focuses on solving problems using
                computers and software. While different problems warrant
                different solutions and may require different tools and
                processes, the methodology and techniques used in solving
                problems do follow some guidelines and can often be generalized
                as problem solving techniques. For example, a general guideline
                for solving a generic engineering problem is to use the three-step
                process given below: Formulate the real problem; Analyze the
                problem; Design a solution search strategy.
            """, lang='en')
        ))
