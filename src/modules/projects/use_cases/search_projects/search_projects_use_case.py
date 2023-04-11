from ...repositories.projects_repository import ProjectsRepository

class SearchProjectsUseCase:
    def __init__(self, projects_repository: ProjectsRepository):
        self.projects_repository = projects_repository

    def execute(self, query, page):
        projects = self.projects_repository.search(query, page)

        projects_list = []

        for project in projects:
            projects_list.append(project.to_dict())

        return projects_list