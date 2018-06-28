from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
Once the problem analysis is complete, we can focus on structuring a search
strategy to find the solution. In order to find the “best” solution (here,
“best” could mean different things to different people, such as faster,
cheaper, more usable, different capabilities, etc.), we need to eliminate
paths that do not lead to viable solutions, design tasks in a way that
provides the most guidance in searching for a solution, and use various
attributes of the final solution state to guide our choices in the problem
solving process.
"""


class DesignASolutionSearchStrategy(object):
    """
    Subtopic: Design a Solution Search Strategy
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Design_a_Solution_Search_Strategy'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Problem_Solving_Techniques'),
        ))
        graph.add((
            URIRef(knowledge + 'Design_a_Solution_Search_Strategy'),
            URIRef(dc + 'title'),
            Literal('Design a Solution Search Strategy', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Design_a_Solution_Search_Strategy'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))
