import urllib
import httplib2
import json


class Query(object):
    """
    Class that run the SPARQL queries
    """

    @classmethod
    def run(cls, endpoint, query):
        """
        Run the query.
        """

        headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'accept': 'application/sparql-results+json'
        }

        (response, content) = httplib2.Http().request(
            endpoint,
            'POST',
            urllib.parse.urlencode({'query': query}),
            headers=headers
        )

        print("Response %s" % response.status)

        results = json.loads(content.decode('utf-8'))

        return results['results']['bindings']

    @classmethod
    def update(cls, query, endpoint=None):
        """
        Insert/Update or Remove triple from triplestore.
        """

        if not endpoint:
            repository = 'softeng'
            context = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"

            params = {'context': '<' + context + '>'}

            endpoint = "http://localhost:8001/openrdf-sesame/repositories/{0}/statements?{1}".format(
                repository,
                urllib.parse.urlencode(params)
            )

        print("POST SPARQL query to %s" % endpoint)

        params = {'update': query}

        headers = {
            'content-type': 'application/x-www-form-urlencoded',
        }

        (response, content) = httplib2.Http().request(
            endpoint,
            'POST',
            urllib.parse.urlencode(params),
            headers=headers
        )

        print("Response %s" % response.status)

        return response.status
