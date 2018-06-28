import urllib
import httplib2
import json

query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    SELECT ?subject ?predicate ?object
    WHERE {
        ?subject ?predicate ?object .
        ?subject dc:title ?title .
        ?subject dc:description ?description
    }
"""

repository = 'softeng'
endpoint = "http://localhost:8001/openrdf-sesame/repositories/{0}".format(repository)

print("POST SPARQL query to %s" % endpoint)

params = {'query': query}

headers = {
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/sparql-results+json'
}

(response, content) = httplib2.Http().request(
    endpoint,
    'POST',
    urllib.parse.urlencode(params),
    headers=headers
)

print("Response %s" % response.status)

results = json.loads(content.decode('utf-8'))

for result in results['results']['bindings']:
    print("Subject: " + str(result['subject']['value']))
    print("Predicate: " + str(result['predicate']['value']))
    print("Object: " + str(result['object']['value']))
    print("")
