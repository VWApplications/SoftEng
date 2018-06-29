from rdflib import URIRef, Literal
from RDF.data_property import title, description, code
from RDF.object_property import (
    subClassOf, hasContent, isInTheFlowOf,
    isPartOf, hasType, belongsTo, hasRequired
)
from RDF.prefix import pp, knowledge


class Calculo2(object):
    """
    Calculo 02
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Calculo_2'),
            subClassOf,
            URIRef(pp + 'Discipline'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            belongsTo,
            URIRef(pp + 'Software_Engineering'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            hasType,
            URIRef(pp + 'Required'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            isInTheFlowOf,
            URIRef(pp + 'Second_Semester'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            isPartOf,
            URIRef(pp + 'Core_Basic_Content'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            title,
            Literal('Calculo 02', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            code,
            Literal('113042', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            description,
            Literal('Disciplina voltada para calculo diferencial e integrais duplas', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            hasContent,
            URIRef(knowledge + 'Algorithmic_Analysis'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            hasContent,
            URIRef(knowledge + 'Analyze_the_Problem'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_2'),
            hasRequired,
            URIRef(pp + 'Calculo_1')
        ))
