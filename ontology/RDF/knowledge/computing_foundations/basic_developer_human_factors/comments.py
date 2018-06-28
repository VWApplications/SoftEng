from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
To most people, programming is coding. These people do not realize that
programming also includes writing comments and that comments are an integral
part of programming. True, comments are not used by the computer and certainly
do not constitute final instructions for the computer, but they improve the
readability of the programs by explaining the meaning and logic of the
statements or sections of code. It should be remembered that programs are not
only meant for computers, they are also read, written, and modified by humans.
The types of comments include repeat of the code, explanation of the code,
marker of the code, summary of the code, description of the code’s intent, and
information that cannot possibly be expressed by the code itself. Some comments
are good, some are not. The good ones are those that explain the intent of the
code and justify why this code looks the way it does. The bad ones are repeat
of the code and stating irrelevant information. The best comments are
selfdocumenting code. If the code is written in such a clear and precise manner
that its meaning is selfproclaimed, then no comment is needed.  But this is
easier said than done. Most programs are not self-explanatory and are often
hard to read and understand if no comments are given.
"""


class Comments(object):
    """
    Subtopic: Comments
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Comments'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Basic_Developer_Human_Factors'),
        ))
        graph.add((
            URIRef(knowledge + 'Comments'),
            URIRef(dc + 'title'),
            Literal('Comments', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Comments'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))
