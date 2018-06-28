from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Calculo1(object):
    """
    Calculo 01
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Calculo_1'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Discipline'),
        ))
        graph.add((
            URIRef(es + 'Calculo_1'),
            URIRef(es + 'hasType'),
            URIRef(es + 'Required'),
        ))
        graph.add((
            URIRef(es + 'Calculo_1'),
            URIRef(es + 'isInTheFlowOf'),
            URIRef(es + 'First_Semester'),
        ))
        graph.add((
            URIRef(es + 'Calculo_1'),
            URIRef(es + 'isPartOf'),
            URIRef(es + 'Core_Basic_Content'),
        ))
        graph.add((
            URIRef(es + 'Calculo_1'),
            URIRef(dc + 'code'),
            Literal('123456', datatype=XSD.integer)
        ))
        graph.add((
            URIRef(es + 'Calculo_1'),
            URIRef(dc + 'title'),
            Literal('Calculo 01', lang='en')
        ))
        graph.add((
            URIRef(es + 'Calculo_1'),
            URIRef(es + 'hasContent'),
            URIRef(es + 'Algorithmic_Analysis'),
        ))
        graph.add((
            URIRef(es + 'Calculo_1'),
            URIRef(es + 'hasContent'),
            URIRef(es + 'Analyze_the_Problem'),
        ))
