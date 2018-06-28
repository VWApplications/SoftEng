from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class FGA(object):
    """
    Campus FGA
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'FGA'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Academic_Campus'),
        ))
        graph.add((
            URIRef(es + 'FGA'),
            URIRef(es + 'belongsTo'),
            URIRef(es + 'UnB'),
        ))
        graph.add((
            URIRef(es + 'FGA'),
            URIRef(dc + 'title'),
            Literal('Faculty of Engineering of Gama', lang='en')
        ))
        graph.add((
            URIRef(es + 'FGA'),
            URIRef(dc + 'description'),
            Literal("Faculty of Engineering of Gama - FGA", lang='en')
        ))
