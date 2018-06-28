from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class OverviewOfAlgorithms(object):
    """
    Subtopic: Overview of Algorithms
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Overview_of_Algorithms'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Algorithms_and_Complexity'),
        ))
        graph.add((
            URIRef(es + 'Overview_of_Algorithms'),
            URIRef(dc + 'title'),
            Literal('Overview of Algorithms', lang='en')
        ))
        graph.add((
            URIRef(es + 'Overview_of_Algorithms'),
            URIRef(dc + 'description'),
            Literal("""
                Abstractly speaking, algorithms guide the operations of
                computers and consist of a sequence of actions composed to
                solve a problem. Alternative definitions include but are not
                limited to: An algorithm is any well-defined computational
                procedure that takes some value or set of values as input and
                produces some value or set of values as output; An algorithm is
                a sequence of computational steps that transform the input into
                the output; An algorithm is a tool for solving a wellspecified
                computation problem. Of course, different definitions are
                favored by different people. Though there is no universally
                accepted definition, some agreement exists
                that an algorithm needs to be correct, finite (in other words,
                terminate eventually or one must be able to write it in a
                finite number of steps), and unambiguous.
            """, lang='en')
        ))
