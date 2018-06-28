from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class ActivitiesOfStudentRepresentations(object):
    """
    Activities of Student Representations
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Activities_of_Student_Representations'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(es + 'Activities_of_Student_Representations'),
            URIRef(dc + 'title'),
            Literal('Activities of Student Representations', lang='en')
        ))
        graph.add((
            URIRef(es + 'Activities_of_Student_Representations'),
            URIRef(dc + 'description'),
            Literal("""
                Effective participation in the Academic Center and Engineering
                Academic Directory, student representation in collegiate
                bodies.
            """, lang='en')
        ))
