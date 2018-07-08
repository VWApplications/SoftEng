from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class FirstSemester(object):
    """
    First Semester
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'First_Semester'),
            subClassOf,
            URIRef(pp + 'Semester'),
        ))
        graph.add((
            URIRef(pp + 'First_Semester'),
            title,
            Literal('First Semester', lang='en')
        ))
