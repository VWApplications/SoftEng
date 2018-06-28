from rdflib import URIRef, Literal
from .evening import Evening
from .full_time import FullTime
from .morning import Morning
from .nocturnal import Nocturnal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Period(object):
    """
    Course Period
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Period'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Course_Domain'),
        ))
        graph.add((
            URIRef(es + 'Period'),
            URIRef(dc + 'title'),
            Literal('Course Period', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        Evening(self.graph)
        FullTime(self.graph)
        Morning(self.graph)
        Nocturnal(self.graph)
