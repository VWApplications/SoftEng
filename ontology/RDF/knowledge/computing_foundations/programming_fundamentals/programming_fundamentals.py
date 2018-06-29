from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge
from .programming_paradigms import ProgrammingParadigms
from .the_programming_process import TheProgrammingProcess

text = """
Programming is composed of the methodologies or activities for creating
computer programs that perform a desired function. It is an indispensible part
in software construction. In general, programming can be considered as the
process of designing, writing, testing, debugging, and maintaining the source
code.  This source code is written in a programming language. The process of
writing source code often requires expertise in many different subject areas
including knowledge of the application domain, appropriate data structures,
specialized algorithms, various language constructs, good programming
techniques, and software engineering.
"""


class ProgrammingFundamentals(object):
    """
    Topic: Programming Fundamentals
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(knowledge + 'Programming_Fundamentals'),
            subClassOf,
            URIRef(knowledge + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(knowledge + 'Programming_Fundamentals'),
            title,
            Literal('Programming Fundamentals', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Programming_Fundamentals'),
            description,
            Literal(text, datatype=XSD.string)
        ))

        self.graph = graph

        self.create_subtopics()

    def create_subtopics(self):
        """
        Create subtopics.
        """

        ProgrammingParadigms(self.graph)
        TheProgrammingProcess(self.graph)
