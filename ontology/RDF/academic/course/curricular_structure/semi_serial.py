from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class SemiSerial(object):
    """
    Semi Serial System
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Semi_Serial'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Curricular_Structure'),
        ))
        graph.add((
            URIRef(es + 'Semi_Serial'),
            URIRef(dc + 'title'),
            Literal('Semi Serial System', lang='en')
        ))
        graph.add((
            URIRef(es + 'Semi_Serial'),
            URIRef(dc + 'description'),
            Literal("""
                The semi-serial system is an academic structure that combines
                characteristics of the serial system and the credit system.

                This system allows great flexibility in the construction of a
                study plan by the students, but creates a difficulty of
                managing vacancies. In the semi-serial system, the flexibility
                of the credit system is contemplated, but the formative
                trajectory is oriented around a reference flow chart, by means
                of preference of places: the student who fully fulfills the
                disciplines for a semester have their job preferably processed
                in the subjects of the following semester.
            """, lang='en')
        ))
