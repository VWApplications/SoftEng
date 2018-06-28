from rdflib import URIRef, Literal
from .programming_paradigms import ProgrammingParadigms
from .the_programming_process import TheProgrammingProcess

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class ProgrammingFundamentals(object):
    """
    Topic: Programming Fundamentals
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(es + 'Programming_Fundamentals'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(es + 'Programming_Fundamentals'),
            URIRef(dc + 'title'),
            Literal('Programming Fundamentals', lang='en')
        ))
        graph.add((
            URIRef(es + 'Programming_Fundamentals'),
            URIRef(dc + 'description'),
            Literal("""
                Programming is composed of the methodologies or activities for
                creating computer programs that perform a desired function. It
                is an indispensible part in software construction. In general,
                programming can be considered as the process of designing,
                writing, testing, debugging, and maintaining the source code.
                This source code is written in a programming language. The
                process of writing source code often requires expertise in many
                different subject areas including knowledge of the application
                domain, appropriate data structures, specialized algorithms,
                various language constructs, good programming techniques, and
                software engineering.
            """, lang='en')
        ))

        self.graph = graph

        self.create_subtopics()

    def create_subtopics(self):
        """
        Create subtopics.
        """

        ProgrammingParadigms(self.graph)
        TheProgrammingProcess(self.graph)