from fixture.project import Project
import random


def test_delete_project(app, db):
    if db.count_projects() == 0:
        app.project.create(Project(name=("Project %s" % random.randrange(1, 100)), description="description1"))

    old_project_list = app.soap.get_projects_name_list()
    project_name = random.choice(old_project_list)
    app.project.delete_project_by_name(project_name)
    new_project_list = app.soap.get_projects_name_list()
    assert len(old_project_list) - 1 == db.count_projects()
    old_project_list.remove(project_name)
    assert sorted(old_project_list) == sorted(new_project_list)

