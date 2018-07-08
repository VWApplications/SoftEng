from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class NinthSemester(object):
    """
    Ninth Semester
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Ninth_Semester'),
            subClassOf,
            URIRef(pp + 'Semester'),
        ))
        graph.add((
            URIRef(pp + 'Ninth_Semester'),
            title,
            Literal('Ninth Semester', lang='en')
        ))
