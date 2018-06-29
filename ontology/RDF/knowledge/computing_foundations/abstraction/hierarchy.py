from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge

text = """
When we use abstraction in our problem formulation and solution, we may use
different abstractions at different times in other words, we work on different
levels of abstraction as the situation calls. Most of the time, these different
levels of abstraction are organized in a hierarchy. There are many ways to
structure a particular hierarchy and the criteria used in determining the
specific content of each layer in the hierarchy varies depending on the
individuals performing the work. Sometimes, a hierarchy of abstraction is
sequential, which means that each layer has one and only one predecessor
(lower) layer and one and only one successor (upper) layer except the upmost
layer (which has no successor) and the bottommost layer (which has no
predecessor). Sometimes, however, the hierarchy is organized in a tree-like
structure, which means each layer can have more than one predecessor layer but
only one successor layer. Occasionally, a hierarchy can have a manyto-many
structure, in which each layer can have multiple predecessors and successors.
At no time, shall there be any loop in a hierarchy.
"""


class Hierarchy(object):
    """
    Subtopic: Hierarchy
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Hierarchy'),
            subClassOf,
            URIRef(knowledge + 'Abstraction'),
        ))
        graph.add((
            URIRef(knowledge + 'Hierarchy'),
            title,
            Literal('Hierarchy', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Hierarchy'),
            description,
            Literal(text, datatype=XSD.string)
        ))
