from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.prefix import pp
from resource.object_property import (
    subClassOf, hasCampus, hasCourse,
    hasExtensionActivitie
)


class UnB(object):
    """
    University of Brasilia - UnB
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'UnB'),
            subClassOf,
            URIRef(pp + 'Academic_Institution')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            hasCampus,
            URIRef(pp + 'FGA')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            hasCourse,
            URIRef(pp + 'Software_Engineering')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            hasExtensionActivitie,
            URIRef(pp + 'Activities_of_Social')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            hasExtensionActivitie,
            URIRef(pp + 'Activities_of_Student_Representations')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            hasExtensionActivitie,
            URIRef(pp + 'Extension_Activities')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            hasExtensionActivitie,
            URIRef(pp + 'Mobility_and_Exchange_Activities')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            hasExtensionActivitie,
            URIRef(pp + 'Professional_Practice_Activities')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            hasExtensionActivitie,
            URIRef(pp + 'Research_Activities')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            hasExtensionActivitie,
            URIRef(pp + 'Teaching_Activities')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            title,
            Literal('University of Brasilia', lang='en')
        ))
        graph.add((
            URIRef(pp + 'UnB'),
            description,
            Literal("University of Brasilia - UnB", datatype=XSD.string)
        ))
