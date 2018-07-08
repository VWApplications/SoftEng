from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


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
