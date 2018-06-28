from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class SystemsEngineering(object):
    """
    Subtopic: Systems Engineering
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Systems_Engineering'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Basic_Concept_of_a_System'),
        ))
        graph.add((
            URIRef(es + 'Systems_Engineering'),
            URIRef(dc + 'title'),
            Literal('Systems Engineering', lang='en')
        ))
        graph.add((
            URIRef(es + 'Systems_Engineering'),
            URIRef(dc + 'description'),
            Literal("""
                “Systems engineering is the interdisciplinary approach
                governing the total technical and managerial effort required to
                transform a set of customer needs, expectations, and
                constraints into a solution and to support that solution
                throughout its life.”. The life cycle stages of systems
                engineering vary depending on the system being
                built but, in general, include system requirements definition,
                system design, sub-system development, system integration,
                system testing, system installation, system evolution, and
                system decommissioning. Many practical guidelines have been
                produced in the past to aid people in performing the activities
                of each phase. For example, system design can be broken into
                smaller tasks of identification of subsystems, assignment of
                system requirements to subsystems, specification of subsystem
                functionality, definition of sub-system interfaces, and so
                forth.
            """, lang='en')
        ))
