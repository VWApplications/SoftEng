from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class SoftwareEngineering(object):
    """
    Software Engineering
    """

    def __init__(self, graph):
        """
        Create triples
        """

        graph.add((
            URIRef(es + 'Software_Engineering'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Course'),
        ))
        graph.add((
            URIRef(es + 'Software_Engineering'),
            URIRef(es + 'belongsTo'),
            URIRef(es + 'UnB'),
        ))
        graph.add((
            URIRef(es + 'Software_Engineering'),
            URIRef(es + 'hasPeriod'),
            URIRef(es + 'Full_Time'),
        ))
        graph.add((
            URIRef(es + 'Software_Engineering'),
            URIRef(es + 'hasStructureCurricular'),
            URIRef(es + 'Semi_Serial'),
        ))
        graph.add((
            URIRef(es + 'Software_Engineering'),
            URIRef(dc + 'title'),
            Literal('Software Enginnering', lang='en')
        ))
        graph.add((
            URIRef(es + 'Software_Engineering'),
            URIRef(dc + 'description'),
            Literal("""
                Software Engineering is an area of computing focused on the
                specification, development, maintenance and creation of
                software systems, applying technologies and practices of
                project management and other disciplines, aiming at
                organization, productivity and quality. Currently, these
                technologies and practices encompass programming languages,
                database, tools, platforms, libraries, standards, processes and
                the quality of software issue.
            """, lang='en')
        ))
