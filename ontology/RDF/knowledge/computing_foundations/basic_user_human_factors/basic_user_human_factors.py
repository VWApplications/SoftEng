from rdflib import URIRef, Literal
from .error_messages import ErrorMessages
from .software_robustness import SoftwareRobustness
from .user_input_and_output import UserInputAndOutput

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class BasicUserHumanFactors(object):
    """
    Topic: Basic User Human Factors
    """

    def __init__(self, graph):
        """
        Create topic
        """

        graph.add((
            URIRef(es + 'Basic_User_Human_Factors'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Computing_Foundations'),
        ))
        graph.add((
            URIRef(es + 'Basic_User_Human_Factors'),
            URIRef(dc + 'title'),
            Literal('Basic User Human Factors', lang='en')
        ))
        graph.add((
            URIRef(es + 'Basic_User_Human_Factors'),
            URIRef(dc + 'description'),
            Literal("""
                Software is developed to meet human desires or needs. Thus, all
                software design and development must take into consideration
                human-user factors such as how people use software, how people
                view software, and what humans expect from software. There are
                numerous factors in the human-machine interaction, and ISO 9241
                document series define all the detailed standards of such
                interactions. But the basic human-user factors considered
                here include input/output, the handling of error messages, and
                the robustness of the software in general.
            """, lang='en')
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
