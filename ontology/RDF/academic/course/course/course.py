from rdflib import URIRef, Literal
from .software_engineering import SoftwareEngineering

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Course(object):
    """
    Course
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Course'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Course_Domain'),
        ))
        graph.add((
            URIRef(es + 'Course'),
            URIRef(dc + 'title'),
            Literal('Course', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        SoftwareEngineering(self.graph)
