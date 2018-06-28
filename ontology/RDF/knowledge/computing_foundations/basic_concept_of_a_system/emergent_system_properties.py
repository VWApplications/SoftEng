from rdflib import URIRef, Literal, XSD

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
knowledge = "http://www.semanticweb.org/ontologies/2018/Knowledge/"

description = """
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
            URIRef(rdfs + 'subClassOf'),
            URIRef(knowledge + 'Basic_Concept_of_a_System'),
        ))
        graph.add((
            URIRef(knowledge + 'Emergent_System_Properties'),
            URIRef(dc + 'title'),
            Literal('Emergent System Properties', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Emergent_System_Properties'),
            URIRef(dc + 'description'),
            Literal(description, datatype=XSD.string)
        ))
