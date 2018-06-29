from rdflib import URIRef, Literal
from RDF.data_property import title
from RDF.object_property import subClassOf
from RDF.prefix import pp


class SeventhSemester(object):
    """
    Seventh Semester
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Seventh_Semester'),
            subClassOf,
            URIRef(pp + 'Semester'),
        ))
        graph.add((
            URIRef(pp + 'Seventh_Semester'),
            title,
            Literal('Seventh Semester', lang='en')
        ))
