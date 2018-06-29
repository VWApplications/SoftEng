from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge

text = """
A system is more than simply the sum of its parts.  Thus, the properties of a
system are not simply the sum of the properties of its components. Instead, a
system often exhibits properties that are properties of the system as a whole.
These properties are called emergent properties because they develop only after
the integration of constituent parts in the system.  Emergent system properties
can be either functional or nonfunctional. Functional properties describe the
things that a system does. For example, an aircraft’s functional properties
include flotation on air, carrying people or cargo, and use as a weapon of mass
destruction. Nonfunctional properties describe how the system behaves in its
operational environment. These can include such qualities as consistency,
capacity, weight, security, etc.
"""


class EmergentSystemProperties(object):
    """
    Subtopic: Emergent System Properties
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Emergent_System_Properties'),
            subClassOf,
            URIRef(knowledge + 'Basic_Concept_of_a_System'),
        ))
        graph.add((
            URIRef(knowledge + 'Emergent_System_Properties'),
            title,
            Literal('Emergent System Properties', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Emergent_System_Properties'),
            description,
            Literal(text, datatype=XSD.string)
        ))
