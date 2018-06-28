from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
Well-structured programs are easier to understand and modify.  If a program is
poorly structured, then no amount of explanation or comments is sufficient to
make it understandable. The ways to organize a program are numerous and range
from the proper use of white space, indentation, and parentheses to nice
arrangements of groupings, blank lines, and braces. Whatever style one chooses,
it should be consistent across the entire program.
"""


class Structure(object):
    """
    Subtopic: Structure
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Structure'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Basic_Developer_Human_Factors'),
        ))
        graph.add((
            URIRef(knowledge + 'Structure'),
            URIRef(dc + 'title'),
            Literal('Structure', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Structure'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))
