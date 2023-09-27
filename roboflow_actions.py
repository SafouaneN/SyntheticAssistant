from roboflow import Roboflow

def get_model():
    rf = Roboflow(api_key="Y18RQthIRyxa4YA8TMWE")
    project = rf.workspace("cvproject-kkozk").project("cv-1siqc")
    return project.version(1).model