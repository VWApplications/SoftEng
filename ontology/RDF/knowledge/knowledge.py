from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge
from .computing_foundations import ComputingFoundations

text = """
A body of knowledge or Knowledge area is the complete set of concepts, terms
and activities that make up a professional domain, as defined by the relevant
learned society or professional association. It is a type of knowledge
representation by any knowledge organization. A BOK/KA is the accepted ontology
for a specific domain. A BOK/KA is more than simply a collection of terms; a
professional reading list; a library; a website or a collection of websites; a
description of professional functions; or even a collection of information.
"""


class Knowledge(object):

    def __init__(self, graph):
        graph.add((
            URIRef(knowledge + 'Knowledge_Area'),
            subClassOf,
            URIRef(knowledge + 'Knowledge_Domain')
        ))
        graph.add((
            URIRef(knowledge + 'Knowledge_Area'),
            title,
            Literal('Knowledge Area', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Knowledge_Area'),
            description,
            Literal(text, datatype=XSD.string)
        ))

        self.graph = graph

        self.create_knowledges()

    def create_knowledges(self):
        """
        Create knowledges.
        """

        ComputingFoundations(self.graph)
