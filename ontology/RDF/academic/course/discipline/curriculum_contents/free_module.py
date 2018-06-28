from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class FreeModule(object):
    """
    Free Module
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Free_Module'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Curriculum_Contents'),
        ))
        graph.add((
            URIRef(es + 'Free_Module'),
            URIRef(dc + 'title'),
            Literal('Free Module', lang='en')
        ))
        graph.add((
            URIRef(es + 'Free_Module'),
            URIRef(dc + 'description'),
            Literal("""
                The disciplines that constitute complementary training and free
                training enable the student to be co-responsible for the
                construction of his / her curriculum, with training in his or
                her area of greatest interest, and not only a
                generalized theoretical and practical training. Free training,
                disciplines categorized as free module, consists of activities
                / disciplines developed by the student based on their personal
                interests, which are not part of the activities of the basic
                cycle, nor of the professional, complementary / optional or
                integrative. They can be taken at any of the University's
                campuses.
            """, lang='en')
        ))
