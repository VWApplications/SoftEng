from django.template.defaultfilters import slugify
from core import Query, Sesame


class Knowledges(object):
    """
    Knowledge area
    """

    @classmethod
    def get_knowledges(self):
        """
        Get all knowledges area.
        """

        query = """
            PREFIX knowledge: <http://www.semanticweb.org/ontologies/2018/Knowledge/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?knowledge ?title ?description
            WHERE {
              ?knowledge rdfs:subClassOf knowledge:Knowledge_Area .
              ?knowledge dc:title ?title .
              ?knowledge dc:description ?description
            }
        """

        results = Query.run(Sesame.endpoint, query)

        knowledges = []
        for result in results:
            knowledge = Knowledge(
                uri=result['knowledge']['value'],
                title=result['title']['value'],
                description=result['description']['value']
            )
            knowledges.append(knowledge)

        return knowledges


class Knowledge(object):
    """
    Knowledge Area
    """

    def __init__(self, uri, title, description=None):
        """
        Constructor
        """

        self.uri = uri
        self.title = title
        self.slug = slugify(title)
        self.description = description
        self.topics = self.get_topics()

    def __str__(self):
        """
        To string method
        """

        return self.slug

    def get_topics(self):
        """
        Get all topics of specific knowledge.
        """

        query = """
            PREFIX knowledge: <http://www.semanticweb.org/ontologies/2018/Knowledge/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?topic ?title ?description
            WHERE {
              ?topic rdfs:subClassOf <%s> .
              ?topic dc:title ?title .
              ?topic dc:description ?description .
            }
        """ % self.uri

        results = Query.run(Sesame.endpoint, query)

        topics = []
        for result in results:
            topic = Topic(
                uri=result['topic']['value'],
                title=result['title']['value'],
                description=result['description']['value'],
                knowledge=self
            )
            topics.append(topic)

        return topics


class Topic(object):
    """
    Topic
    """

    def __init__(self, uri, title, description=None, knowledge=None):
        """
        Constructor
        """

        self.uri = uri
        self.title = title
        self.slug = slugify(title)
        self.description = description
        self.knowledge = knowledge
        self.subtopics = self.get_subtopics()

    def __str__(self):
        """
        To string method
        """

        return self.slug

    def get_subtopics(self):
        """
        Get all subtopics of specific topic.
        """

        query = """
            PREFIX knowledge: <http://www.semanticweb.org/ontologies/2018/Knowledge/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?subtopic ?title ?description
            WHERE {
              ?subtopic rdfs:subClassOf <%s> .
              ?subtopic dc:title ?title .
              ?subtopic dc:description ?description .
            }
        """ % self.uri

        results = Query.run(Sesame.endpoint, query)

        subtopics = []
        for result in results:
            subtopic = Subtopic(
                uri=result['subtopic']['value'],
                title=result['title']['value'],
                description=result['description']['value'],
                knowledge=self.knowledge,
                topic=self
            )
            subtopics.append(subtopic)

        return subtopics


class Subtopic(object):
    """
    Create a subtopic
    """

    def __init__(self, uri, title, topic, knowledge, description=None):
        """
        Constructor
        """

        self.uri = uri
        self.title = title
        self.slug = slugify(title)
        self.description = description
        self.knowledge = knowledge
        self.topic = topic

    def __str__(self):
        return self.slug
