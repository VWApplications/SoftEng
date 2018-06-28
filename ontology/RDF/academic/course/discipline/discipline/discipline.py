from rdflib import URIRef, Literal
from .calculo_1 import Calculo1

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Discipline(object):
    """
    Discipline Domain
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Discipline'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Discipline_Domain'),
        ))
        graph.add((
            URIRef(es + 'Discipline'),
            URIRef(dc + 'title'),
            Literal('Discipline', lang='en')
        ))
        graph.add((
            URIRef(es + 'Discipline'),
            URIRef(dc + 'description'),
            Literal("""
                Discipline designate a particular branch of knowledge.
            """, lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        Calculo1(self.graph)
