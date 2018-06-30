from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description, code
from RDF.object_property import (
    subClassOf, hasContent, isInTheFlowOf,
    isPartOf, hasType, belongsTo, isRequiredOf
)
from RDF.prefix import pp, knowledge


class Calculo1(object):
    """
    Calculo 01
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Calculo_1'),
            subClassOf,
            URIRef(pp + 'Discipline'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            belongsTo,
            URIRef(pp + 'Software_Engineering'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            hasType,
            URIRef(pp + 'Required'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            isInTheFlowOf,
            URIRef(pp + 'First_Semester'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            isPartOf,
            URIRef(pp + 'Core_Basic_Content'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            title,
            Literal('Calculo 01', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            code,
            Literal('113034', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            description,
            Literal('Disciplina voltada para calculo diferencial e integrais', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            hasContent,
            URIRef(knowledge + 'Algorithmic_Analysis'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            hasContent,
            URIRef(knowledge + 'Analyze_the_Problem'),
        ))
        graph.add((
            URIRef(pp + 'Calculo_1'),
            isRequiredOf,
            URIRef(pp + 'Calculo_2')
        ))
