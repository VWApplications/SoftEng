from rdflib import URIRef, Literal
from .core_content import CoreContent
from .free_module import FreeModule
from .multidisciplinary import Multidisciplinary

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class CurriculumContents(object):
    """
    Curriculum Contents
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Curriculum_Contents'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Discipline_Domain'),
        ))
        graph.add((
            URIRef(es + 'Curriculum_Contents'),
            URIRef(dc + 'title'),
            Literal('Curriculum Contents', lang='en')
        ))
        graph.add((
            URIRef(es + 'Curriculum_Contents'),
            URIRef(dc + 'description'),
            Literal('Curriculum disciplines to specific course', lang='en')
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
