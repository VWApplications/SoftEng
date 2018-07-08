from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf, typeOf
from resource.prefix import knowledge

text = """
Sometimes it is useful to have multiple alternate abstractions for the same problem so that one can keep different perspectives in mind. For example, we can have a class diagram, a state chart, and a sequence diagram for the same software at the same level of abstraction. These alternate abstractions do not form a hierarchy but rather complement each other in helping understanding the problem and its solution. Though beneficial, it is as times difficult to keep alternate abstractions in sync.
"""


class AlternateAbstractions(object):
    """
    Subtopic: Alternate Abstractions
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Alternate_Abstraction'),
            typeOf,
            URIRef(knowledge + 'Subtopic'),
        ))
        graph.add((
            URIRef(knowledge + 'Alternate_Abstraction'),
            subClassOf,
            URIRef(knowledge + 'Abstraction'),
        ))
        graph.add((
            URIRef(knowledge + 'Alternate_Abstraction'),
            title,
            Literal('Alternate Abstraction', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Alternate_Abstraction'),
            description,
            Literal(text, datatype=XSD.string)
        ))
