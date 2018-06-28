from rdflib import URIRef, Literal
from .FGA import FGA

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class AcademicCampus(object):
    """
    Academic Campus
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Academic_Campus'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Academic_Domain'),
        ))
        graph.add((
            URIRef(es + 'Academic_Campus'),
            URIRef(dc + 'title'),
            Literal('Academic Campus', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        FGA(self.graph)
