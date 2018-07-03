from core import Query, Sesame
from knowledge.models import Subtopic
from django.template.defaultfilters import slugify


class Disciplines(object):
    """
    Discipline model
    """

    def __init__(self):
        """
        Create disciplines
        """

        self.first_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:First_Semester")
        self.second_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:Second_Semester")
        self.third_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:Third_Semester")
        self.fourth_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:Fourth_Semester")
        self.fifth_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:Fifth_Semester")
        self.sixth_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:Sixth_Semester")
        self.seventh_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:Seventh_Semester")
        self.eighth_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:Eighth_Semester")
        self.ninth_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:Ninth_Semester")
        self.tenth_semester = self.get_disciplines("pp:isInTheFlowOf", "pp:Tenth_Semester")
        self.all = self.get_disciplines("rdfs:subClassOf", "pp:Discipline")

    def get_disciplines(self, predicate, obj):
        """
        Get the data from triple store.
        """

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?disciplines ?code ?title ?description ?type ?semester ?core_content
            WHERE {
              ?disciplines %s %s .
              ?disciplines dc:title ?title .
              OPTIONAL {?disciplines dc:description ?description .}
              OPTIONAL {?disciplines pp:code ?code .}
              OPTIONAL {?disciplines pp:hasType ?type_uri .}
              OPTIONAL {?type_uri dc:title ?type .}
              OPTIONAL {?disciplines pp:isInTheFlowOf ?semester_uri .}
              OPTIONAL {?semester_uri dc:title ?semester .}
              OPTIONAL {?disciplines pp:isPartOf ?core_content_uri}
              OPTIONAL {?core_content_uri dc:title ?core_content}
            }
        """ % (predicate, obj)

        result = Query.run(Sesame.endpoint, query)

        disciplines = []
        for discipline in result:
            obj = Discipline(
                uri=discipline['disciplines']['value'],
                title=discipline['title']['value'],
                code=discipline['code']['value'],
                description=discipline['description']['value'],
                classification=discipline['type']['value'],
                semester=discipline['semester']['value'],
                core_content=discipline['core_content']['value']
            )
            disciplines.append(obj)

        return disciplines

    @classmethod
    def get_is_required_of(cls, discipline_uri):
        """
        Get required that the disciplines is required from triple store.
        """

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?is_required_of
            WHERE {
              <%s> pp:isRequiredOf ?is_required_of_uri .
              ?is_required_of_uri dc:title ?is_required_of
            }
        """ % (discipline_uri)

        result = Query.run(Sesame.endpoint, query)

        disciplines = []
        for discipline in result:
            discipline = Discipline(discipline['is_required_of']['value'])
            disciplines.append(discipline)

        return disciplines

    @classmethod
    def get_requireds(cls, discipline_uri):
        """
        Get required disciplines from triple store.
        """

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?required
            WHERE {
              <%s> pp:hasRequired ?required_uri .
              ?required_uri dc:title ?required
            }
        """ % (discipline_uri)

        result = Query.run(Sesame.endpoint, query)

        disciplines = []
        for discipline in result:
            discipline = Discipline(discipline['required']['value'])
            disciplines.append(discipline)

        return disciplines

    @classmethod
    def get_contents(cls, discipline_uri):
        """
        Get content disciplines from triple store.
        """

        query = """
            PREFIX pp: <http://www.semanticweb.org/ontologies/2018/Pedagogical_Project/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?content_uri ?title ?topic ?knowledge
            WHERE {
              <%s> pp:hasContent ?content_uri .
              ?content_uri rdfs:subClassOf ?knowledge_uri .
              ?knowledge_uri dc:title ?knowledge .
              ?content_uri dc:title ?title .
              ?content_uri rdfs:subClassOf ?topic_uri .
              ?topic_uri dc:title ?topic
            }
        """ % (discipline_uri)

        result = Query.run(Sesame.endpoint, query)

        contents = []
        for content in result:
            subtopic = Subtopic(
                content['content_uri']['value'],
                content['title']['value'],
                content['topic']['value'],
                content['knowledge']['value']
            )
            contents.append(subtopic)

        return contents


class Discipline(object):
    """
    Create a discipline.
    """

    def __init__(self,
                 title,
                 uri=None,
                 code=None,
                 description=None,
                 classification=None,
                 semester=None,
                 core_content=None):
        """
        Constructor
        """

        self.title = title
        self.slug = slugify(title)
        self.uri = uri
        self.code = code
        self.description = description
        self.classification = classification
        self.semester = semester
        self.core_content = core_content
