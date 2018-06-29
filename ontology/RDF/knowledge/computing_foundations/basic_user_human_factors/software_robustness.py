from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge

text = """
Software robustness refers to the ability of software to tolerate erroneous
inputs. Software is said to be robust if it continues to function even when
erroneous inputs are given.  Thus, it is unacceptable for software to simply
crash when encountering an input problem as this may cause unexpected
consequences, such as the loss of valuable data. Software that exhibits such
behavior is considered to lack robustness.  Nielsen gives a simpler description
of software robustness: “The software should have a low error rate, so that
users make few errors during the use of the system and so that if they do make
errors they can easily recover from them. Further, catastrophic errors must not
occur”. There are many ways to evaluate the robustness of software and just as
many ways to make software more robust. For example, to improve robustness, one
should always check the validity of the inputs and return values before
progressing further; one should always throw an exception when something
unexpected occurs, and one should never quit a program without first giving
users/applications a chance to correct the condition.
"""


class SoftwareRobustness(object):
    """
    Subtopic: Software Robustness
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Software_Robustness'),
            subClassOf,
            URIRef(knowledge + 'Basic_User_Human_Factors'),
        ))
        graph.add((
            URIRef(knowledge + 'Software_Robustness'),
            title,
            Literal('Software Robustness', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Software_Robustness'),
            description,
            Literal(text, datatype=XSD.string)
        ))
