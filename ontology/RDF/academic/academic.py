from rdflib import URIRef, Literal
from .campus import AcademicCampus
from .institution import AcademicInstitution
from .extension import ComplementaryAndExtensionActivities
from .course import CourseDomain
from RDF.data_property import title
from RDF.prefix import pp


class AcademicDomain(object):
    """
    Academic Domain
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Academic_Domain'),
            title,
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
