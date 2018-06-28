from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class TeachingActivities(object):
    """
    Teaching Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Teaching_Activities'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(es + 'Teaching_Activities'),
            URIRef(dc + 'title'),
            Literal('Teaching Activities', lang='en')
        ))
        graph.add((
            URIRef(es + 'Teaching_Activities'),
            URIRef(dc + 'description'),
            Literal("""
                Monitoring of course subjects, technical course teacher, etc.
            """, lang='en')
        ))
