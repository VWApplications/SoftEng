from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class ErrorMessages(object):
    """
    Subtopic: Error Messages
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Error_Messages'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Basic_User_Human_Factors'),
        ))
        graph.add((
            URIRef(es + 'Error_Messages'),
            URIRef(dc + 'title'),
            Literal('Error Messages', lang='en')
        ))
        graph.add((
            URIRef(es + 'Error_Messages'),
            URIRef(dc + 'description'),
            Literal("""
                It is understandable that most software contains faults and
                fails from time to time. But users should be notified if there
                is anything that impedes the smooth execution of the program.
                Nothing is more frustrating than an unexpected termination or
                behavioral deviation of software without any warning or
                explanation. To be user friendly, the software should report
                all error conditions to the users or upper-level applications
                so that some measure can be taken to rectify the situation or
                to exit gracefully. There are several guidelines that define
                what constitutes a good error message: error messages should be
                clear, to the point, and timely. First, error messages should
                clearly explain what is happening so that users know what is
                going on in the software. Second, error messages should
                pinpoint the cause of the error, if at all possible, so that
                proper actions can be taken. Third, error messages should be
                displayed right when the error condition occurs. According to
                Jakob Nielsen, “Good error messages should be expressed in
                plain language (no codes), precisely indicate the problem, and
                constructively suggest a solution”. Fourth, error messages
                should not overload the users with too much information and
                cause them to ignore the messages all together. However,
                messages relating to security access errors should not provide
                extra information that would help unauthorized persons break
                in.
            """, lang='en')
        ))