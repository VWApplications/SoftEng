from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf, typeOf
from RDF.prefix import knowledge

text = """
Once the problem statement is available, the next step is to analyze the problem statement or situation to help structure our search for a solution.  Four types of analysis include situation analysis, in which the most urgent or critical aspects of a situation are identified first; problem analysis, in which the cause of the problem must be determined; decision analysis, in which the action(s) needed to correct the problem or eliminate its cause must be determined; and potential problem analysis, in which the action(s) needed to prevent any reoccurrences of the problem or the development of new problems must be determined.
"""


class AnalyzeTheProblem(object):
    """
    Subtopic: Analyze the Problem
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Analyze_the_Problem'),
            typeOf,
            URIRef(knowledge + 'Subtopic'),
        ))
        graph.add((
            URIRef(knowledge + 'Analyze_the_Problem'),
            subClassOf,
            URIRef(knowledge + 'Problem_Solving_Techniques'),
        ))
        graph.add((
            URIRef(knowledge + 'Analyze_the_Problem'),
            title,
            Literal('Analyze the Problem', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Analyze_the_Problem'),
            description,
            Literal(text, datatype=XSD.string)
        ))
