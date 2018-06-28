from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class UnB(object):
    """
    University of Brasilia - UnB
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'UnB'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Academic_Institution'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(es + 'hasCampus'),
            URIRef(es + 'FGA'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(es + 'hasCourse'),
            URIRef(es + 'Software_Engineering'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(es + 'hasExtensionActivitie'),
            URIRef(es + 'Activities_of_Social'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(es + 'hasExtensionActivitie'),
            URIRef(es + 'Activities_of_Student_Representations'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(es + 'hasExtensionActivitie'),
            URIRef(es + 'Extension_Activities'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(es + 'hasExtensionActivitie'),
            URIRef(es + 'Mobility_and_Exchange_Activities'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(es + 'hasExtensionActivitie'),
            URIRef(es + 'Professional_Practice_Activities'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(es + 'hasExtensionActivitie'),
            URIRef(es + 'Research_Activities'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(es + 'hasExtensionActivitie'),
            URIRef(es + 'Teaching_Activities'),
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(dc + 'title'),
            Literal('University of Brasilia', lang='en')
        ))
        graph.add((
            URIRef(es + 'UnB'),
            URIRef(dc + 'description'),
            Literal("University of Brasilia - UnB", lang='en')
        ))
