from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf, typeOf
from RDF.prefix import knowledge

text = """
It is understandable that most software contains faults and fails from time to time. But users should be notified if there is anything that impedes the smooth execution of the program.  Nothing is more frustrating than an unexpected termination or behavioral deviation of software without any warning or explanation. To be user friendly, the software should report all error conditions to the users or upper-level applications so that some measure can be taken to rectify the situation or to exit gracefully. There are several guidelines that define what constitutes a good error message: error messages should be clear, to the point, and timely. First, error messages should clearly explain what is happening so that users know what is going on in the software.  Second, error messages should pinpoint the cause of the error, if at all possible, so that proper actions can be taken. Third, error messages should be displayed right when the error condition occurs. According to Jakob Nielsen, “Good error messages should be expressed in plain language (no codes), precisely indicate the problem, and constructively suggest a solution”. Fourth, error messages should not overload the users with too much information and cause them to ignore the messages all together. However, messages relating to security access errors should not provide extra information that would help unauthorized persons break in.
"""


class ErrorMessages(object):
    """
    Subtopic: Error Messages
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Error_Messages'),
            typeOf,
            URIRef(knowledge + 'Subtopic'),
        ))
        graph.add((
            URIRef(knowledge + 'Error_Messages'),
            subClassOf,
            URIRef(knowledge + 'Basic_User_Human_Factors'),
        ))
        graph.add((
            URIRef(knowledge + 'Error_Messages'),
            title,
            Literal('Error Messages', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Error_Messages'),
            description,
            Literal(text, datatype=XSD.string)
        ))
