from rdflib import URIRef, Literal, XSD
from .comments import Comments
from .structure import Structure

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
Developer human factors refer to the considerations of human factors taken when
developing software. Software is developed by humans, read by humans, and
maintained by humans. If anything is wrong, humans are responsible for
correcting those wrongs. Thus, it is essential to write software in a way that
is easily understandable by humans or, at the very least, by other software
developers. A program that is easy to read and understand exhibits readability.
The means to ensure that software meet this objective are numerous and range
from proper architecture at the macro level to the particular coding style and
variable usage at the micro level. But the two prominent factors are structure
(or program layouts) and comments(documentation).
"""


class BasicDeveloperHumanFactors(object):
    """
    Topic: Basic Developer Human Factors
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(knowledge + 'Basic_Developer_Human_Factors'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(knowledge + 'Basic_Developer_Human_Factors'),
            URIRef(dc + 'title'),
            Literal('Basic Developer Human Factors', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Basic_Developer_Human_Factors'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))

        self.graph = graph

        self.create_subtopics()

    def create_subtopics(self):
        """
        Create subtopics.
        """

        Comments(self.graph)
        Structure(self.graph)
