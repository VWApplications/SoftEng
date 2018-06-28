from rdflib import URIRef, Literal
from .campus import AcademicCampus
from .institution import AcademicInstitution
from .extension import ComplementaryAndExtensionActivities
from .course import CourseDomain

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class AcademicDomain(object):
    """
    Academic Domain
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Academic_Domain'),
            URIRef(dc + 'title'),
            Literal('Academic Domain', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        AcademicCampus(self.graph)
        AcademicInstitution(self.graph)
        ComplementaryAndExtensionActivities(self.graph)
        CourseDomain(self.graph)