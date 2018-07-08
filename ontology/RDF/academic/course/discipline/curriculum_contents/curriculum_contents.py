from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp
from .core_content import CoreContent
from .free_module import FreeModule
from .multidisciplinary import Multidisciplinary


class CurriculumContents(object):
    """
    Curriculum Contents
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Curriculum_Contents'),
            subClassOf,
            URIRef(pp + 'Discipline_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Curriculum_Contents'),
            title,
            Literal('Curriculum Contents', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        CoreContent(self.graph)
        FreeModule(self.graph)
        Multidisciplinary(self.graph)
