from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
Among all the systems, one that is obviously relevant to the software
engineering community is the computer system. A computer is a machine that
executes programs or software. It consists of a purposeful collection of
mechanical, electrical, and electronic components with each component
performing a preset function. Jointly, these components are able to execute the
instructions that are given by the program. Abstractly speaking, a computer
receives some input, stores and manipulates some data, and provides some
output. The most distinct feature of a computer is its ability to store and
execute sequences of instructions called programs. An interesting phenomenon
concerning the computer is the universal equivalence in functionality.
According to Turing, all computers with a certain minimum capability are
equivalent in their ability to perform computation tasks. In other words, given
enough time and memory, all computers ranging from a netbook to a supercomputer
are capable of computing exactly the same things, irrespective of speed, size,
cost, or anything else. Most computer systems have a structure that is known as
the “von Neumann model,” which consists of five components: a memory for
storing instructions and data, a central processing unit for performing
arithmetic and logical operations, a control unit for sequencing and
interpreting instructions, input for getting external information into the
memory, and output for producing results for the user.
"""


class OverviewOfAComputerSystem(object):
    """
    Subtopic: Overview of a Computer System
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Overview_of_a_Computer_System'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Basic_Concept_of_a_System'),
        ))
        graph.add((
            URIRef(knowledge + 'Overview_of_a_Computer_System'),
            URIRef(dc + 'title'),
            Literal('Overview of a Computer System', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Overview_of_a_Computer_System'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))
