from rdflib import URIRef, Literal
from .optional import Optional
from .practical import Practical
from .required import Required
from .theoretical import Theoretical

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Classification(object):
    """
    Discipline classification
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Classification'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Discipline_Domain'),
        ))
        graph.add((
            URIRef(es + 'Classification'),
            URIRef(dc + 'title'),
            Literal('Classification', lang='en')
        ))
        graph.add((
            URIRef(es + 'Classification'),
            URIRef(dc + 'description'),
            Literal("""
                The course is composed of disciplines, classified in the
                required or optional and Practical or Theoretical types
            """, lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        Optional(self.graph)
        Practical(self.graph)
        Required(self.graph)
        Theoretical(self.graph)
