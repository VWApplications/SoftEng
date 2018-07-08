from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp


class ThirdSemester(object):
    """
    Third Semester
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Third_Semester'),
            subClassOf,
            URIRef(pp + 'Semester'),
        ))
        graph.add((
            URIRef(pp + 'Third_Semester'),
            title,
            Literal('Third Semester', lang='en')
        ))
