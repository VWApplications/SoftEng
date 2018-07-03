from core import Query, Sesame
from django.template.defaultfilters import slugify
from .definition_of_problem_solving import DefinitionOfProblemSolving
from .formulating_the_real_problem import FormulatingTheRealProblem
from .analyze_the_problem import AnalyzeTheProblem
from .design_a_solution_search_strategy import DesignASolutionSearchStrategy
from .problem_solving_using_programs import ProblemSolvingUsingPrograms


class ProblemSolvingTechniques(object):
    """
    Topic: Problem Solving Techniques
    """

    ANALYZE_THE_PROBLEM = 0
    DEFINITION_OF_PROBLEM_SOLVING = 1
    DESIGN_A_SOLUTION_SEARCH_STRATEGY = 2
    FORMULATING_THE_REAL_PROBLEM = 3
    PROBLEM_SOLVING_USING_PROGRAMS = 4

    def __init__(self):
        """
        Create a topic.
        """

        result = self.get_information()

        self.uri = "http://www.semanticweb.org/ontologies/2018/Knowledge/Problem_Solving_Techniques"
        self.title = result['title']['value']
        self.description = result['description']['value']
        self.slug = slugify(self.title)

    def get_information(self):
        """
        Get the information from triple store
        """

        query = """
            PREFIX knowledge: <http://www.semanticweb.org/ontologies/2018/Knowledge/>
            PREFIX dc: <http://purl.org/dc/elements/1.1/>

            SELECT DISTINCT ?title ?description
            WHERE {
              knowledge:Problem_Solving_Techniques dc:title ?title ;
              dc:description ?description
            }
        """

        result = Query.run(Sesame.endpoint, query)

        return result[0]

    def get_subtopic(self, subtopic=None):
        """
        Get a specific subtopic.
        """

        if subtopic == self.ANALYZE_THE_PROBLEM:
            return AnalyzeTheProblem()
        elif subtopic == self.DEFINITION_OF_PROBLEM_SOLVING:
            return DefinitionOfProblemSolving()
        elif subtopic == self.DESIGN_A_SOLUTION_SEARCH_STRATEGY:
            return DesignASolutionSearchStrategy()
        elif subtopic == self.FORMULATING_THE_REAL_PROBLEM:
            return FormulatingTheRealProblem()
        elif subtopic == self.PROBLEM_SOLVING_USING_PROGRAMS:
            return ProblemSolvingUsingPrograms()
        else:
            return [
                AnalyzeTheProblem(),
                DefinitionOfProblemSolving(),
                DesignASolutionSearchStrategy(),
                FormulatingTheRealProblem(),
                ProblemSolvingUsingPrograms()
            ]
