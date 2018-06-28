from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class MobilityAndExchangeActivities(object):
    """
    Mobility and Exchange Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Mobility_and_Exchange_Activities'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(es + 'Mobility_and_Exchange_Activities'),
            URIRef(dc + 'title'),
            Literal('Mobility and Exchange Activities', lang='en')
        ))
        graph.add((
            URIRef(es + 'Mobility_and_Exchange_Activities'),
            URIRef(dc + 'description'),
            Literal("""
                Permanent exchange with national and international institutions
                and companies;
            """, lang='en')
        ))
