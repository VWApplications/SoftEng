from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class ExtensionActivities(object):
    """
    Extension Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Extension_Activities'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(es + 'Extension_Activities'),
            URIRef(dc + 'title'),
            Literal('Extension Activities', lang='en')
        ))
        graph.add((
            URIRef(es + 'Extension_Activities'),
            URIRef(dc + 'description'),
            Literal("""
                Courses in the technical or business management area, foreign
                language courses, extension projects with the community
                Institutional Program of Extension Scholarships (PIBEX),
                Continuous Action Extension Projects (PEAC), participation in
                Engineering Week;
            """, lang='en')
        ))
