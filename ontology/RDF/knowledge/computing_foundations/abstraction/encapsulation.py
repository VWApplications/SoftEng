from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
Encapsulation is a mechanism used to implement abstraction.  When we are
dealing with one level of abstraction, the information concerning the levels
below and above that level is encapsulated. This information can be the
concept, problem, or observable phenomenon; or it may be the permissible
operations on these relevant entities. Encapsulation usually comes with some
degree of information hiding in which some or all of the underlying details are
hidden from the level above the interface provided by the abstraction. To an
object, information hiding means we don’t need to know the details of how the
object is represented or how the operations on those objects are implemented.
"""


class Encapsulation(object):
    """
    Subtopic: Encapsulation
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Encapsulation'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Abstraction'),
        ))
        graph.add((
            URIRef(knowledge + 'Encapsulation'),
            URIRef(dc + 'title'),
            Literal('Encapsulation', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Encapsulation'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))
