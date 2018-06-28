from rdflib import URIRef, Literal
from .UnB import UnB

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class AcademicInstitution(object):
    """
    Academic Institution
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Academic_Institution'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Academic_Domain'),
        ))
        graph.add((
            URIRef(es + 'Academic_Institution'),
            URIRef(dc + 'title'),
            Literal('Academic Institution', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        UnB(self.graph)
