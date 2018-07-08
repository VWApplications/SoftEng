from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class FifthSemester(object):
    """
    Fifth Semester
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Fifth_Semester'),
            subClassOf,
            URIRef(pp + 'Semester'),
        ))
        graph.add((
            URIRef(pp + 'Fifth_Semester'),
            title,
            Literal('Fifth Semester', lang='en')
        ))
