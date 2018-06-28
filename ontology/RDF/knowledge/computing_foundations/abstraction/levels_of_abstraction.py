from rdflib import URIRef, Literal

# PREFIX
dc = "http://purl.org/dc/elements/1.1/"
rdfs = "http://www.w3.org/2000/01/rdf-schema#"
es = "http://www.semanticweb.org/ontologies/2018/Software_Engineering/"


class LevelsOfAbstraction(object):
    """
    Subtopic: Levels of Abstration
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(es + 'Levels_of_Abstraction'),
            URIRef(rdfs + 'subClassOf'),
            URIRef(es + 'Abstraction'),
        ))
        graph.add((
            URIRef(es + 'Levels_of_Abstraction'),
            URIRef(dc + 'title'),
            Literal('Levels of Abstraction', lang='en')
        ))
        graph.add((
            URIRef(es + 'Levels_of_Abstraction'),
            URIRef(dc + 'description'),
            Literal("""
                When abstracting, we concentrate on one “level” of the
                big picture at a time with confidence that we can then
                connect effectively with levels above and below. Although
                we focus on one level, abstraction does not mean knowing
                nothing about the neighboring levels. Abstraction levels
                do not necessarily correspond to discrete components in
                reality or in the problem domain, but to welldefined
                standard interfaces such as programming APIs. The advantages
                that standard interfaces provide include portability, easier
                software/hardware integration and wider usage.
            """, lang='en')
        ))
