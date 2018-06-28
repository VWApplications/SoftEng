from rdflib import Graph
from .knowledge import Knowledge
# from academic import AcademicDomain


def create_rdf():
    """
    Create SoftEng RDF file
    """

    graph = Graph()
    Knowledge(graph)
    # AcademicDomain(graph)
    graph.serialize("ontology/RDF/softeng.rdf")
