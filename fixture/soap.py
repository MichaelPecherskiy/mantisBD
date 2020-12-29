from suds.client import Client
from suds import WebFault


class SoapHelper:

    def __init__(self, app):
        self.app = app

    api = "api/soap/mantisconnect.php?wsdl"

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseURL'] + self.api)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_id(self, project_name ):
        username = "administrator"
        password = "root"
        client = Client(self.app.config['web']['baseURL'] + self.api)
        try:
            return client.service.mc_project_get_id_from_name(username, password, project_name)
        except WebFault:
            return False

    def get_projects_name_list(self):
        username = "administrator"
        password = "root"
        client = Client(self.app.config['web']['baseURL'] + self.api)
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            list_id = []
            for pr in projects:
                list_id.append(pr['name'])
            return list_id
        except WebFault:
            return False
