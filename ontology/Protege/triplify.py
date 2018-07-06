# BUG - Do not remove the rdf:nodeID
import rdflib

graph = rdflib.Graph()

query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dc: <http://purl.org/dc/elements/1.1/>

    SELECT ?subject ?predicate ?object ?title ?description
    WHERE {
        ?subject rdfs:subClassOf ?restriction .
        ?restriction owl:onProperty ?predicate .
        ?restriction owl:someValuesFrom ?object .
        ?subject dc:title ?title .
        ?subject dc:description ?description

        FILTER NOT EXISTS { ?subject rdf:nodeID ?node }
    }
"""

graph.parse("ontology/RDF/ontology.rdf", format="xml")
results = graph.query(query)

SUBJECT = 0
PREDICATE = 1
OBJECT = 2
TITLE = 3
DESCRIPTION = 4

dc_title = rdflib.URIRef('http://purl.org/dc/elements/1.1/title')
dc_description = rdflib.URIRef('http://purl.org/dc/elements/1.1/description')

for result in results:
    print("URI: " + str(result[0]))
    print("Predicado: " + result[1])
    print("Objeto: " + result[2])
    print("Titulo: " + result[3])
    print("Descrição: " + result[4])
    print("")
    graph.add((result[SUBJECT], result[PREDICATE], result[OBJECT]))
    graph.add((result[SUBJECT], dc_title, result[TITLE]))
    graph.add((result[SUBJECT], dc_description, result[DESCRIPTION]))

graph.serialize("ontology/RDF/softeng.rdf")
