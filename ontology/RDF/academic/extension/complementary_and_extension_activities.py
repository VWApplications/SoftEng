from rdflib import URIRef, Literal
from .activities_of_social import ActivitiesOfSocial
from .activities_of_student_representations import ActivitiesOfStudentRepresentations
from .extension_activities import ExtensionActivities
from .mobility_and_exchange_activities import MobilityAndExchangeActivities
from .professional_practice_activities import ProfessionalPracticeActivities
from .research_activities import ResearchActivities
from .teaching_activities import TeachingActivities

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class ComplementaryAndExtensionActivities(object):
    """
    Complementary and Extension Activities
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Complementary_and_Extension_Activities'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Academic_Domain'),
        ))
        graph.add((
            URIRef(es + 'Complementary_and_Extension_Activities'),
            URIRef(dc + 'title'),
            Literal('Complementary and Extension Activities', lang='en')
        ))
        graph.add((
            URIRef(es + 'Complementary_and_Extension_Activities'),
            URIRef(dc + 'description'),
            Literal("""
                In addition to the subjects of free choice of the student, it
                also contemplates the completion of complementary and extension
                activities such as: scientific initiation, multidisciplinary
                projects, participation in events, participation in a junior
                company, etc. All these programs provide for paid scholarships;
                proof of participation as a volunteer, in addition to credits
                in free module.
            """, lang='en')
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
