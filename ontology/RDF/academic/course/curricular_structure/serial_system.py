from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class SerialSystem(object):
    """
    Serial System
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Serial_System'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Curricular_Structure'),
        ))
        graph.add((
            URIRef(es + 'Serial_System'),
            URIRef(dc + 'title'),
            Literal('Serial System', lang='en')
        ))
        graph.add((
            URIRef(es + 'Serial_System'),
            URIRef(dc + 'description'),
            Literal("""
                Students follow pre-determined lists of disciplines per
                semester or school year.
            """, lang='en')
        ))
