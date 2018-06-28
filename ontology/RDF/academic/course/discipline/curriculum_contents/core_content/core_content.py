from rdflib import URIRef, Literal
from .core_basic_content import CoreBasicContent
from .core_professional_content import CoreProfessionalContent
from .core_specific_content import CoreSpecificContent

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class CoreContent(object):
    """
    Core Contents
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Core_Content'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Curriculum_Contents'),
        ))
        graph.add((
            URIRef(es + 'Core_Content'),
            URIRef(dc + 'title'),
            Literal('Core Content', lang='en')
        ))
        graph.add((
            URIRef(es + 'Core_Content'),
            URIRef(dc + 'description'),
            Literal('Core content of pedagogical project', lang='en')
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
