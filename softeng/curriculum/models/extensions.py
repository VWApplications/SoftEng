from django.template.defaultfilters import slugify
from core import Query, Sesame
from .extension import (
    ActivitiesOfSocialAction, ActivitiesOfStudentRepresentations,
    ExtensionActivities, MobilityAndExchangeActivities,
    ProfessionalPracticeActivities, ResearchActivities,
    TeachingActivities
)


class Extension(object):
    """
    Extensions.
    """

    ACTIVITIES_OF_SOCIAL_ACTION = 0
    ACTIVITIES_OF_STUDENT_REPRESENTATIONS = 1
    EXTENSION_ACTIVITIES = 2
    MOBILITY_AND_EXCHANGE_ACTIVITIES = 3
    PROFESSIONAL_PRACTICE_ACTIVITIES = 4
    RESEARCH_ACTIVITIES = 5
    TEACHING_ACTIVITIES = 6

    def __init__(self):
        """
        Create a knowledge area.
        """

        result = self.get_information()

        self.title = result['title']['value']
        self.description = result['description']['value']
        self.slug = slugify(self.title)

    def get_information(self):
        """
        Get the information from triple store
        """

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              pp:Complementary_and_Extension_Activities dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_instance(self, instance=None):
        """
        Get extension.
        """

        if instance == self.ACTIVITIES_OF_SOCIAL_ACTION:
            return ActivitiesOfSocialAction()
        elif instance == self.ACTIVITIES_OF_STUDENT_REPRESENTATIONS:
            return ActivitiesOfStudentRepresentations()
        elif instance == self.EXTENSION_ACTIVITIES:
            return ExtensionActivities()
        elif instance == self.MOBILITY_AND_EXCHANGE_ACTIVITIES:
            return MobilityAndExchangeActivities()
        elif instance == self.PROFESSIONAL_PRACTICE_ACTIVITIES:
            return ProfessionalPracticeActivities()
        elif instance == self.RESEARCH_ACTIVITIES:
            return ResearchActivities()
        elif instance == self.TEACHING_ACTIVITIES:
            return TeachingActivities()
        else:
            return [
                ActivitiesOfSocialAction(),
                ActivitiesOfStudentRepresentations(),
                ExtensionActivities(),
                MobilityAndExchangeActivities(),
                ProfessionalPracticeActivities(),
                ResearchActivities(),
                TeachingActivities()
            ]
