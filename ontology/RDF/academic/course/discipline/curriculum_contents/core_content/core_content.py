from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf
from resource.prefix import pp
from .core_basic_content import CoreBasicContent
from .core_professional_content import CoreProfessionalContent
from .core_specific_content import CoreSpecificContent


class CoreContent(object):
    """
    Core Contents
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Core_Content'),
            subClassOf,
            URIRef(pp + 'Curriculum_Contents'),
        ))
        graph.add((
            URIRef(pp + 'Core_Content'),
            title,
            Literal('Core Content', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Core_Content'),
            description,
            Literal('Core content of pedagogical project', datatype=XSD.string)
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        CoreBasicContent(self.graph)
        CoreProfessionalContent(self.graph)
        CoreSpecificContent(self.graph)
