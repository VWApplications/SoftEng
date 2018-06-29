from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp


class SixthSemester(object):
    """
    Sixth Semester
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Sixth_Semester'),
            subClassOf,
            URIRef(pp + 'Semester'),
        ))
        graph.add((
            URIRef(pp + 'Sixth_Semester'),
            title,
            Literal('Sixth Semester', lang='en')
        ))
