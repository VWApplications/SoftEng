from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class ResearchActivities(object):
    """
    Research Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Research_Activities'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(es + 'Research_Activities'),
            URIRef(dc + 'title'),
            Literal('Research Activities', lang='en')
        ))
        graph.add((
            URIRef(es + 'Research_Activities'),
            URIRef(dc + 'description'),
            Literal("""
                Participation in research centers or projects of scientific
                initiation Institutional Program of Scientific Initiation
                Grants (PIBIC), publication of works, participation in seminars
                and scientific initiation events related to graduation;
            """, lang='en')
        ))
