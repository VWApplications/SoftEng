from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Multidisciplinary(object):
    """
    Multidisciplinary
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Multidisciplinary'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Curriculum_Contents'),
        ))
        graph.add((
            URIRef(es + 'Multidisciplinary'),
            URIRef(dc + 'title'),
            Literal('Multidisciplinary', lang='en')
        ))
        graph.add((
            URIRef(es + 'Multidisciplinary'),
            URIRef(dc + 'description'),
            Literal("""
                Multidisciplinary Projects, that is, there is the participation
                of other courses.
            """, lang='en')
        ))
