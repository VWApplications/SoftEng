from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Theoretical(object):
    """
    Theoretical
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Theoretical'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Classification'),
        ))
        graph.add((
            URIRef(es + 'Theoretical'),
            URIRef(dc + 'title'),
            Literal('Theoretical', lang='en')
        ))
