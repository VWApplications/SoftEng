from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp
from .software_engineering import SoftwareEngineering


class Course(object):
    """
    Course
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Course'),
            subClassOf,
            URIRef(pp + 'Course_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Course'),
            title,
            Literal('Course', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        SoftwareEngineering(self.graph)
