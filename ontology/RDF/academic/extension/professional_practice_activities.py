from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class ProfessionalPracticeActivities(object):
    """
    Professional Practice Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Professional_Practice_Activities'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Complementary_and_Extension_Activities'),
        ))
        graph.add((
            URIRef(es + 'Professional_Practice_Activities'),
            URIRef(dc + 'title'),
            Literal('Professional Practice Activities', lang='en')
        ))
        graph.add((
            URIRef(es + 'Professional_Practice_Activities'),
            URIRef(dc + 'description'),
            Literal("""
                Participation in the Executive Board of the Junior Engineering
                Company (EJEL), participation in projects carried out by EJEL,
                extracurricular internships in the technical area,
                technological development projects in companies.
            """, lang='en')
        ))
