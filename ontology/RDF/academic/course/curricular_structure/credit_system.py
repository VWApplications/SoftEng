from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class CreditSystem(object):
    """
    Credit Systen
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Credit_System'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Curricular_Structure'),
        ))
        graph.add((
            URIRef(es + 'Credit_System'),
            URIRef(dc + 'title'),
            Literal('Credit System', lang='en')
        ))
        graph.add((
            URIRef(es + 'Credit_System'),
            URIRef(dc + 'description'),
            Literal("""
                The students can study subjects at any time,
                observing the prerequisites.
            """, lang='en')
        ))
