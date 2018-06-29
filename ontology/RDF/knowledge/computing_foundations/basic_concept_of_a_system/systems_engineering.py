from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge

text = """
“Systems engineering is the interdisciplinary approach governing the total
technical and managerial effort required to transform a set of customer needs,
expectations, and constraints into a solution and to support that solution
throughout its life.”. The life cycle stages of systems engineering vary
depending on the system being built but, in general, include system
requirements definition, system design, sub-system development, system
integration, system testing, system installation, system evolution, and system
decommissioning. Many practical guidelines have been produced in the past to
aid people in performing the activities of each phase. For example, system
design can be broken into smaller tasks of identification of subsystems,
assignment of system requirements to subsystems, specification of subsystem
functionality, definition of sub-system interfaces, and so forth.
"""


class SystemsEngineering(object):
    """
    Subtopic: Systems Engineering
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Systems_Engineering'),
            subClassOf,
            URIRef(knowledge + 'Basic_Concept_of_a_System'),
        ))
        graph.add((
            URIRef(knowledge + 'Systems_Engineering'),
            title,
            Literal('Systems Engineering', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Systems_Engineering'),
            description,
            Literal(text, datatype=XSD.string)
        ))
