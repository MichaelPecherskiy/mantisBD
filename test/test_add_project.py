from model.project import Project
import random

def test_add_project(app, db):
    project = Project(name=("Project %s" % random.randrange(1, 100)), description="description1")
    old_project_list = app.soap.get_projects_name_list()
    app.project.create(project)
    new_project_list = app.soap.get_projects_name_list()
    old_project_list.append(project.name)
    assert sorted(old_project_list) == sorted(new_project_list)