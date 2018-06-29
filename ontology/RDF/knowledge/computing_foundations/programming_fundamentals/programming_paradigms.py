from rdflib import URIRef, Literal, XSD
from RDF.data_property import title, description
from RDF.object_property import subClassOf
from RDF.prefix import knowledge

text = """
Programming is highly creative and thus somewhat personal.  Different people often write different programs for the same requirements. This diversity of programming causes much difficulty in the construction and maintenance of large complex software. Various programming paradigms have been developed over the years to put some standardization into this highly creative and personal activity. When one programs, he or she can use one of several programming paradigms to write the code.  Unstructured Programming: In unstructured programming, a programmer follows his/her hunch to write the code in whatever way he/she likes as long as the function is operational. Often, the practice is to write code to fulfill a specific utility without regard to anything else.  Programs written this way exhibit no particular structure thus the name “unstructured programming.” Unstructured programming is also sometimes called ad hoc programming. Structured/Procedural/ Imperative Programming: A hallmark of structured programming is the use of well-defined control structures, including procedures (and/or functions) with each procedure (or function) performing a specific task. Object-Oriented Programming: While procedural programming organizes programs around procedures, object-oriented programming (OOP) organize a program around objects, which are abstract data structures that combine both data and methods used to access or manipulate the data.
"""


class ProgrammingParadigms(object):
    """
    Subtopic: Programming Paradigms
    """

    def __init__(self, graph):
        """
        Create a subtopic.
        """

        graph.add((
            URIRef(knowledge + 'Programming_Paradigms'),
            subClassOf,
            URIRef(knowledge + 'Programming_Fundamentals'),
        ))
        graph.add((
            URIRef(knowledge + 'Programming_Paradigms'),
            title,
            Literal('Programming Paradigms', lang='en')
        ))
        graph.add((
            URIRef(knowledge + 'Programming_Paradigms'),
            description,
            Literal(text, datatype=XSD.string)
        ))
