from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class CoreBasicContent(object):
    """
    Core Basic Content
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Core_Basic_Content'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Core_Content'),
        ))
        graph.add((
            URIRef(es + 'Core_Basic_Content'),
            URIRef(dc + 'title'),
            Literal('Core Basic Content', lang='en')
        ))
        graph.add((
            URIRef(es + 'Core_Basic_Content'),
            URIRef(dc + 'description'),
            Literal("""
                Required by opinion CNE / CES 136 of 2012 (Curricular
                Guidelines for Graduation in Computing).

                Example: Scientific and Technological Methodology,
                Communication and Expression, Graphic Expression, Mathematics,
                Physics, Production, Innovation, Administration, Economics,
                Environmental Sciences, Humanities, Social Sciences,
                Citizenship
            """, lang='en')
        ))
