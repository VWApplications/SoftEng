from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class ActivitiesOfSocial(object):
    """
    Campus Activities of Social
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Activities_of_Social'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(es + 'Activities_of_Social'),
            URIRef(dc + 'title'),
            Literal('Activities of Social Action, Citizenship and Environment', lang='en')
        ))
        graph.add((
            URIRef(es + 'Activities_of_Social'),
            URIRef(dc + 'description'),
            Literal("""
                Participation in programs or NGOs related to social
                action, exercise of citizenship and defense of the
                environment.
            """, lang='en')
        ))
