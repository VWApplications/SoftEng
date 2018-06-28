from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class CoreSpecificContent(object):
    """
    Core Specific Content
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Core_Specific_Content'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Core_Content'),
        ))
        graph.add((
            URIRef(es + 'Core_Specific_Content'),
            URIRef(dc + 'title'),
            Literal('Core Specific Content', lang='en')
        ))
        graph.add((
            URIRef(es + 'Core_Specific_Content'),
            URIRef(dc + 'description'),
            Literal("""
                Courses addressing the fundamentals and specific topics of
                Software Engineering, as well as other specific contents aimed
                at the development of specific or complementary skills and
                abilities in the area of programming, product and software
                process

                Example: Specific disciplines for software engineering
            """, lang='en')
        ))
