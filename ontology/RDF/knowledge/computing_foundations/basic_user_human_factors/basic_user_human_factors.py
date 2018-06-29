from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge
from .error_messages import ErrorMessages
from .software_robustness import SoftwareRobustness
from .user_input_and_output import UserInputAndOutput

text = """
Software is developed to meet human desires or needs. Thus, all software design and development must take into consideration human-user factors such as how people use software, how people view software, and what humans expect from software. There are numerous factors in the human-machine interaction, and ISO 9241 document series define all the detailed standards of such interactions.  But the basic human-user factors considered here include input/output, the handling of error messages, and the robustness of the software in general.
"""


class BasicUserHumanFactors(object):
    """
    Topic: Basic User Human Factors
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(knowledge + 'Basic_User_Human_Factors'),
            subClassOf,
            URIRef(knowledge + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(knowledge + 'Basic_User_Human_Factors'),
            title,
            Literal('Basic User Human Factors', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Basic_User_Human_Factors'),
            description,
            Literal(text, datatype=XSD.string)
        ))

        self.graph = graph

        self.create_subtopics()

    def create_subtopics(self):
        """
        Create subtopics.
        """

        ErrorMessages(self.graph)
        SoftwareRobustness(self.graph)
        UserInputAndOutput(self.graph)
