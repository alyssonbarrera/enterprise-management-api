from ...repositories.projects_repository import ProjectsRepository

class GetAllProjectsUseCase:
    def __init__(self, projects_repository: ProjectsRepository):
        self.projects_repository = projects_repository

    def execute(self, page=1):
        projects = self.projects_repository.get_all(int(page))

        projects_list = []

        for project in projects:
            projects_list.append(project.to_dict())

        return projects_list
