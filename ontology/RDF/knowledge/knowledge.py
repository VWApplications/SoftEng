from rdflib import URIRef, Literal
from .computing_foundations import ComputingFoundations

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Knowledge(object):

    def __init__(self, graph):
        graph.add((
            URIRef(es + 'Knowledge_Area'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Knowledge_Domain')
        ))
        graph.add((
            URIRef(es + 'Knowledge_Area'),
            URIRef(dc + 'title'),
            Literal('Knowledge Area', lang='en')
        ))
        graph.add((
            URIRef(es + 'Knowledge_Area'),
            URIRef(dc + 'description'),
            Literal("""
                A body of knowledge or Knowledge area is the complete set of concepts,
                terms and activities that make up a professional domain, as defined by the
                relevant learned society or professional association. It is a type of
                knowledge representation by any knowledge organization. A BOK/KA is the
                accepted ontology for a specific domain. A BOK/KA is more than simply a
                collection of terms; a professional reading list; a library; a website or a
                collection of websites; a description of professional functions; or even a
                collection of information.
            """, lang='en')
        ))

        self.graph = graph

        self.create_knowledges()

    def create_knowledges(self):
        """
        Create knowledges.
        """

        ComputingFoundations(self.graph)