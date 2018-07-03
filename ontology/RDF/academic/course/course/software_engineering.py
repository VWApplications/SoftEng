from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.prefix import pp
from RDF.object_property import (
    subClassOf, belongsTo, hasPeriod,
    hasStructureCurricular
)

text = """
Software Engineering is an area of computing focused on the specification, development, maintenance and creation of software systems, applying technologies and practices of project management and other disciplines, aiming at organization, productivity and quality. Currently, these technologies and practices encompass programming languages, database, tools, platforms, libraries, standards, processes and the quality of software issue.
"""


class SoftwareEngineering(object):
    """
    Software Engineering
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(pp + 'Software_Engineering'),
            subClassOf,
            URIRef(pp + 'Course'),
        ))
        graph.add((
            URIRef(pp + 'Software_Engineering'),
            hasPeriod,
            URIRef(pp + 'Full_Time'),
        ))
        graph.add((
            URIRef(pp + 'Software_Engineering'),
            title,
            Literal('Software Engineering', lang='en')
        ))
        graph.add((
            URIRef(pp + 'Software_Engineering'),
            hasStructureCurricular,
            URIRef(pp + 'Semi_Serial'),
        ))
        graph.add((
            URIRef(pp + 'Software_Engineering'),
            belongsTo,
            URIRef(pp + 'UnB'),
        ))
        graph.add((
            URIRef(pp + 'Software_Engineering'),
            description,
            Literal(text, datatype=XSD.string)
        ))
