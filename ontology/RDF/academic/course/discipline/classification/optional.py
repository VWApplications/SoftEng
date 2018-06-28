from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Optional(object):
    """
    Optional
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Optional'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Classification'),
        ))
        graph.add((
            URIRef(es + 'Optional'),
            URIRef(dc + 'title'),
            Literal('Optional', lang='en')
        ))
        graph.add((
            URIRef(es + 'Optional'),
            URIRef(dc + 'description'),
            Literal("""
                The optional disciplines are those students' free choice to
                compose their curriculum in order to attend a more personalized
                training of the professional being graduated.
            """, lang='en')
        ))
