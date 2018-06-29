from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge

text = """
Analysis of algorithms is the theoretical study of computer-program performance
and resource usage; to some extent it determines the goodness of an algorithm.
Such analysis usually abstracts away the particular details of a specific
computer and focuses on the asymptotic, machine-independent analysis. There are
three basic types of analysis.  In worst-case analysis, one determines the
maximum time or resources required by the algorithm on any input of size n. In
average-case analysis, one determines the expected time or resources required
by the algorithm over all inputs of size n; in performing average-case
analysis, one often needs to make assumptions on the statistical distribution
of inputs. The third type of analysis is the best-case analysis, in which one
determines the minimum time or resources required by the algorithm on any input
of size n.  Among the three types of analysis, average-case analysis is the
most relevant but also the most difficult to perform.
"""


class AlgorithmicAnalysis(object):
    """
    Subtopic: Algorithmic Analysis
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Algorithmic_Analysis'),
            subClassOf,
            URIRef(knowledge + 'Algorithms_and_Complexity'),
        ))
        graph.add((
            URIRef(knowledge + 'Algorithmic_Analysis'),
            title,
            Literal('Algorithmic Analysis', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Algorithmic_Analysis'),
            description,
            Literal(text, datatype=XSD.string)
        ))
