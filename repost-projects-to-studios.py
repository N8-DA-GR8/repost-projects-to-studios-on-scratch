import scratchattach as sa

studios = [1,2,3]#enter studio ids
projects = [1,2,3]#enter project ids

session = sa.login("username", "password")#enter username and password

for studio_element in studios:
    studio = session.connect_studio(studio_element)
    for project_element in projects:
        try:
            studio.remove_project(project_element)
        except:
            print(f"could not remove project {project_element} from {studio_element}")
        try:
            studio.add_project(project_element)
        except:
            print(f"could not add project {project_element} to {studio_element}")
