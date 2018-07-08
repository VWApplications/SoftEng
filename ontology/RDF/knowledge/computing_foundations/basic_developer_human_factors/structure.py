from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf, typeOf
from resource.prefix import knowledge

text = """
Well-structured programs are easier to understand and modify.  If a program is poorly structured, then no amount of explanation or comments is sufficient to make it understandable. The ways to organize a program are numerous and range from the proper use of white space, indentation, and parentheses to nice arrangements of groupings, blank lines, and braces. Whatever style one chooses, it should be consistent across the entire program.
"""


class Structure(object):
    """
    Subtopic: Structure
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Structure'),
            typeOf,
            URIRef(knowledge + 'Subtopic'),
        ))
        graph.add((
            URIRef(knowledge + 'Structure'),
            subClassOf,
            URIRef(knowledge + 'Basic_Developer_Human_Factors'),
        ))
        graph.add((
            URIRef(knowledge + 'Structure'),
            title,
            Literal('Structure', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Structure'),
            description,
            Literal(text, datatype=XSD.string)
        ))
