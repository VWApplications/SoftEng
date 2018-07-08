from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf, typeOf
from resource.prefix import knowledge

text = """
Encapsulation is a mechanism used to implement abstraction.  When we are dealing with one level of abstraction, the information concerning the levels below and above that level is encapsulated. This information can be the concept, problem, or observable phenomenon; or it may be the permissible operations on these relevant entities. Encapsulation usually comes with some degree of information hiding in which some or all of the underlying details are hidden from the level above the interface provided by the abstraction. To an object, information hiding means we don’t need to know the details of how the object is represented or how the operations on those objects are implemented.
"""


class Encapsulation(object):
    """
    Subtopic: Encapsulation
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Encapsulation'),
            typeOf,
            URIRef(knowledge + 'Subtopic'),
        ))
        graph.add((
            URIRef(knowledge + 'Encapsulation'),
            subClassOf,
            URIRef(knowledge + 'Abstraction'),
        ))
        graph.add((
            URIRef(knowledge + 'Encapsulation'),
            title,
            Literal('Encapsulation', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Encapsulation'),
            description,
            Literal(text, datatype=XSD.string)
        ))
