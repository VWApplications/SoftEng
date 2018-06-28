from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class UserInputAndOutput(object):
    """
    Subtopic: Input and Output
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'User_Input_and_Output'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Basic_User_Human_Factors'),
        ))
        graph.add((
            URIRef(es + 'User_Input_and_Output'),
            URIRef(dc + 'title'),
            Literal('User Input and Output', lang='en')
        ))
        graph.add((
            URIRef(es + 'User_Input_and_Output'),
            URIRef(dc + 'description'),
            Literal("""
                Input and output are the interfaces between users and software.
                Software is useless without input and output. Humans design
                software to process some input and produce desirable output.
                All software engineers must consider input and output as an
                integral part of the software product they engineer or develop.
                Issues considered for input include (but are not limited to):
                What input is required? How is the input passed from users to
                computers? What is the most convenient way for users to
                enter input? What format does the computer require of the input
                data? The designer should request the minimum data from human
                input, only when the data is not already stored in the system.
                The designer should format and edit the data at the time of
                entry to reduce errors arising from incorrect or malicious data
                entry. For output, we need to consider what the users wish to
                see: In what format would users like to see output? What is the
                most pleasing way to display output? If the party interacting
                with the software isn’t human but another software or computer
                or control system, then we need to consider the input/output
                type and format that the software should produce to ensure
                proper data exchange between systems. There are many rules of
                thumb for developers to follow to produce good input/output for
                a software.
            """, lang='en')
        ))
