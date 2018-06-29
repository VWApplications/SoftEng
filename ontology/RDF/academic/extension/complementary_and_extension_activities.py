from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import pp
from .activities_of_social import ActivitiesOfSocial
from .activities_of_student_representations import ActivitiesOfStudentRepresentations
from .extension_activities import ExtensionActivities
from .mobility_and_exchange_activities import MobilityAndExchangeActivities
from .professional_practice_activities import ProfessionalPracticeActivities
from .research_activities import ResearchActivities
from .teaching_activities import TeachingActivities

text = """
In addition to the subjects of free choice of the student, it also contemplates
the completion of complementary and extension activities such as: scientific
initiation, multidisciplinary projects, participation in events, participation
in a junior company, etc. All these programs provide for paid scholarships;
proof of participation as a volunteer, in addition to credits in free module.
"""


class ComplementaryAndExtensionActivities(object):
    """
    Complementary and Extension Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Complementary_and_Extension_Activities'),
            subClassOf,
            URIRef(pp + 'Academic_Domain'),
        ))
        graph.add((
            URIRef(pp + 'Complementary_and_Extension_Activities'),
            title,
            Literal('Complementary and Extension Activities', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Complementary_and_Extension_Activities'),
            description,
            Literal(text, datatype=XSD.string)
        ))

        self.graph = graph

        self.create()

    def create(self):
        """
        Insert subclasses
        """

        ActivitiesOfSocial(self.graph)
        ActivitiesOfStudentRepresentations(self.graph)
        ExtensionActivities(self.graph)
        MobilityAndExchangeActivities(self.graph)
        ProfessionalPracticeActivities(self.graph)
        ResearchActivities(self.graph)
        TeachingActivities(self.graph)
