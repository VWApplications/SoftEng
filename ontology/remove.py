import urllib
import httplib2

query = """
    PREFIX dc: <http://purl.org/dc/elements/1.1/>
    DELETE { <http://example/egbook> dc:title  "This is an example title" } WHERE {}
"""

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
