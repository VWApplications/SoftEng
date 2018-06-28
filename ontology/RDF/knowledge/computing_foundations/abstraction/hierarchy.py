from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class Hierarchy(object):
    """
    Subtopic: Hierarchy
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Hierarchy'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Abstraction'),
        ))
        graph.add((
            URIRef(es + 'Hierarchy'),
            URIRef(dc + 'title'),
            Literal('Hierarchy', lang='en')
        ))
        graph.add((
            URIRef(es + 'Hierarchy'),
            URIRef(dc + 'description'),
            Literal("""
                When we use abstraction in our problem formulation and
                solution, we may use different abstractions at different times
                in other words, we work on different levels of abstraction as
                the situation calls. Most of the time, these different levels
                of abstraction are organized in a hierarchy. There are many
                ways to structure a particular hierarchy and the criteria used
                in determining the specific content of each layer in the
                hierarchy varies depending on the individuals performing the
                work. Sometimes, a hierarchy of abstraction is sequential,
                which means that each layer has one and only one predecessor
                (lower) layer and one and only one successor (upper) layer
                except the upmost layer (which has no successor) and the
                bottommost layer (which has no predecessor). Sometimes,
                however, the hierarchy is organized in a tree-like structure,
                which means each layer can have more than one predecessor layer
                but only one successor layer. Occasionally, a hierarchy can
                have a manyto-many structure, in which each layer can have
                multiple predecessors and successors. At no time, shall there
                be any loop in a hierarchy. A hierarchy often forms naturally
                in task decomposition. Often, a task analysis can be decomposed
                in a hierarchical fashion, starting with the larger tasks and
                goals of the organization and breaking each of them down into
                smaller subtasks that can again be further subdivided This
                continuous division of tasks into smaller ones would produce a
                hierarchical structure of tasks-subtasks.
            """, lang='en')
        ))
