from core import Query, Sesame
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
              OPTIONAL {?core_content_uri dc:title ?core_content .}
            }
        """ % (predicate, obj)

        result = Query.run(Sesame.endpoint, query)

        disciplines = []
        for discipline in result:
            disciplines.append({
                'uri': discipline['disciplines']['value'],
                'title': discipline['title']['value'],
                'description': discipline['description']['value'],
                'type': discipline['type']['value'],
                'core_content': discipline['core_content']['value'],
                'slug': slugify(discipline['title']['value']),
            })

        return disciplines
