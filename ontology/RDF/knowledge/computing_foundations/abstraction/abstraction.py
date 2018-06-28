from rdflib import URIRef, Literal
from .alternate_abstractions import AlternateAbstractions
from .encapsulation import Encapsulation
from .hierarchy import Hierarchy
from .levels_of_abstraction import LevelsOfAbstraction

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Abstraction(object):
    """
    Topic: Abstraction
    """

    def __init__(self, graph):
        """
        Create the Abstraction Topic of Computing Foundations.
        """

        graph.add((
            URIRef(es + 'Abstraction'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(es + 'Abstraction'),
            URIRef(dc + 'title'),
            Literal('Abstraction', lang='en')
        ))
        graph.add((
            URIRef(es + 'Abstraction'),
            URIRef(dc + 'description'),
            Literal("""
                Abstraction is an indispensible technique associated
                with problem solving. It refers to both the process
                and result of generalization by reducing the information
                of a concept, a problem, or an observable phenomenon so
                that one can focus on the “big picture.” One of the most
                important skills in any engineering undertaking is framing
                the levels of abstraction appropriately. “Through abstraction,”
                according to Voland, “we view the problem and its possible
                solution paths from a higher level of conceptual understanding.
                As a result, we may become better prepared to recognize possible
                relationships between different aspects of the problem and thereby
                generate more creative design solutions”. This is particularly
                true in computer science in general (such as hardware vs.
                software) and in software engineering in particular (data structure
                vs. data flow, and so forth).
            """, lang='en')
        ))

        self.graph = graph

        self.create_subtopics()

    def create_subtopics(self):
        """
        Create subtopics.
        """

        AlternateAbstractions(self.graph)
        Encapsulation(self.graph)
        Hierarchy(self.graph)
        LevelsOfAbstraction(self.graph)
