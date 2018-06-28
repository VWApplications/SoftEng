from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class CoreProfessionalContent(object):
    """
    Core Professional Content
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Core_Professional_Content'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Core_Content'),
        ))
        graph.add((
            URIRef(es + 'Core_Professional_Content'),
            URIRef(dc + 'title'),
            Literal('Core Professional Content', lang='en')
        ))
        graph.add((
            URIRef(es + 'Core_Professional_Content'),
            URIRef(dc + 'description'),
            Literal("""
                Disciplines with basic vocational content that allow to reach
                the basic elements of the professional profile of the egress.

                Example: Programming Logic, Algorithms and Data Structure,
                Digital Circuits, Computing, Programming Language, Database.
            """, lang='en')
        ))
