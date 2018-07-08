from rdflib import URIRef, Literal, XSD
from resource.data_property import title, description
from resource.object_property import subClassOf, typeOf
from resource.prefix import knowledge

text = """
Gerard Voland writes, “It is important to recognize that a specific problem should be formulated if one is to develop a specific solution”. This formulation is called the problem statement, which explicitly specifies what both the problem and the desired outcome are. Although there is no universal way of stating a problem, in general a problem should be expressed in such a way as to facilitate the development of solutions. Some general techniques to help one formulate the real problem include statement-restatement, determining the source and the cause, revising the statement, analyzing present and desired state, and using the fresh eye approach.
"""


class FormulatingTheRealProblem(object):
    """
    Subtopic: Formulating the Real Problem
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Formulating_the_Real_Problem'),
            typeOf,
            URIRef(knowledge + 'Subtopic'),
        ))
        graph.add((
            URIRef(knowledge + 'Formulating_the_Real_Problem'),
            subClassOf,
            URIRef(knowledge + 'Problem_Solving_Techniques'),
        ))
        graph.add((
            URIRef(knowledge + 'Formulating_the_Real_Problem'),
            title,
            Literal('Formulating the Real Problem', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Formulating_the_Real_Problem'),
            description,
            Literal(text, datatype=XSD.string)
        ))
