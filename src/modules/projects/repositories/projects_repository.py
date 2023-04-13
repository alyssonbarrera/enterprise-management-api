from django.db.utils import IntegrityError
from src.shared.infra.database.models import Project
from django.core.exceptions import ObjectDoesNotExist
from src.utils.error_messages import PROJECT_DUPLICATE_ENTRY
from src.shared.errors.DuplicateEntryError import DuplicateEntryError

ITEMS_PER_PAGE = 20

class ProjectsRepository:
    def create(self, data):
        try:
            project = Project(**data)

            project.save()

            return project
        except IntegrityError as error:
            if 'UNIQUE constraint failed' in str(error):
                return DuplicateEntryError(PROJECT_DUPLICATE_ENTRY)
            else:
                return error

    def get(self, id):
        try:
            return Project.objects.get(id=id)
        except ObjectDoesNotExist:
            return None
        
    def find_by_criteria(self, criteria):
        try:
            project = {}
            for key, value in criteria.items():
                project = Project.objects.get(**{key: value})
                
            return project
        except Exception:
            return None

    def get_all(self, page):
        projects = Project.objects.all()[(page - 1) * ITEMS_PER_PAGE:page * ITEMS_PER_PAGE]

        return list(projects)
    
    def project_already_exists_in_department(self, project_name):
        try:
            project = Project.objects.get(name=project_name)
            
            return project.already_exists_in_department()
        except ObjectDoesNotExist:
            return None
    
    def search(self, name, page):
        projects = Project.objects.filter(name__icontains=name)[(page - 1) * ITEMS_PER_PAGE:page * ITEMS_PER_PAGE]

        return list(projects)

    def update(self, project, data):
        try:            
            for key, value in data.items():
                setattr(project, key, value)

            project.save()

            return project
        except ObjectDoesNotExist:
            return DuplicateEntryError(PROJECT_DUPLICATE_ENTRY)
        
    def delete(self, project):
        return project.delete()