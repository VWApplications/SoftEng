from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf, typeOf
from RDF.prefix import knowledge
from .alternate_abstractions import AlternateAbstractions
from .encapsulation import Encapsulation
from .hierarchy import Hierarchy
from .levels_of_abstraction import LevelsOfAbstraction

text = """
Abstraction is an indispensible technique associated with problem solving. It refers to both the process and result of generalization by reducing the information of a concept, a problem, or an observable phenomenon so that one can focus on the “big picture.” One of the most important skills in any engineering undertaking is framing the levels of abstraction appropriately.  “Through abstraction,” according to Voland, “we view the problem and its possible solution paths from a higher level of conceptual understanding.  As a result, we may become better prepared to recognize possible relationships between different aspects of the problem and thereby generate more creative design solutions”. This is particularly true in computer science in general (such as hardware vs.  software) and in software engineering in particular (data structure vs. data flow, and so forth).
"""


class Abstraction(object):
    """
    Topic: Abstraction
    """

    def __init__(self, graph):
        """
        Create the Abstraction Topic of Computing Foundations.
        """

        graph.add((
            URIRef(knowledge + 'Abstraction'),
            typeOf,
            URIRef(knowledge + 'Topic'),
        ))
        graph.add((
            URIRef(knowledge + 'Abstraction'),
            subClassOf,
            URIRef(knowledge + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(knowledge + 'Abstraction'),
            title,
            Literal('Abstraction', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Abstraction'),
            description,
            Literal(text, datatype=XSD.string)
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
