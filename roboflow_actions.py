from roboflow import Roboflow

def get_model():
    rf = Roboflow(api_key="iOzMHe7qLC5Vkt5ApTKc")
    project = rf.workspace("synthass").project("snyth_assis")
    return project.version(1).model