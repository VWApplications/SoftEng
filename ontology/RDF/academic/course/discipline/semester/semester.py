from rdflib import URIRef, Literal
from resource.data_property import title
from resource.object_property import subClassOf
from resource.prefix import pp
from .first_semester import FirstSemester
from .second_semester import SecondSemester
from .third_semester import ThirdSemester
from .fourth_semester import FourthSemester
from .fifth_semester import FifthSemester
from .sixth_semester import SixthSemester
from .seventh_semester import SeventhSemester
from .eighth_semester import EighthSemester
from .ninth_semester import NinthSemester
from .tenth_semester import TenthSemester


class Semester(object):
    """
    Discipline Semester
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Semester'),
            subClassOf,
            URIRef(pp + 'Discipline_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Semester'),
            title,
            Literal('Semester', lang='en')
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        FirstSemester(self.graph)
        SecondSemester(self.graph)
        ThirdSemester(self.graph)
        FourthSemester(self.graph)
        FifthSemester(self.graph)
        SixthSemester(self.graph)
        SeventhSemester(self.graph)
        EighthSemester(self.graph)
        NinthSemester(self.graph)
        TenthSemester(self.graph)
