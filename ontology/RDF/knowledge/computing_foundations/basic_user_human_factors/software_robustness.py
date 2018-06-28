from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class SoftwareRobustness(object):
    """
    Subtopic: Software Robustness
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Software_Robustness'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Basic_User_Human_Factors'),
        ))
        graph.add((
            URIRef(es + 'Software_Robustness'),
            URIRef(dc + 'title'),
            Literal('Software Robustness', lang='en')
        ))
        graph.add((
            URIRef(es + 'Software_Robustness'),
            URIRef(dc + 'description'),
            Literal("""
                Software robustness refers to the ability of software to
                tolerate erroneous inputs. Software is said to be robust if it
                continues to function even when erroneous inputs are given.
                Thus, it is unacceptable for software to simply crash when
                encountering
                an input problem as this may cause unexpected consequences,
                such as the loss of valuable data. Software that exhibits such
                behavior is considered to lack robustness. Nielsen gives a
                simpler description of software robustness: “The software
                should have a low error rate, so that users make few errors
                during the use of the system and so that if they do make errors
                they can easily recover from them. Further,
                catastrophic errors must not occur”. There are many ways to
                evaluate the robustness of software and just as many ways to
                make software more robust. For example, to improve robustness,
                one should always check the validity of the inputs and return
                values before progressing further; one should always throw an
                exception
                when something unexpected occurs, and one should never quit a
                program without first giving users/applications a chance to
                correct the condition.
            """, lang='en')
        ))
