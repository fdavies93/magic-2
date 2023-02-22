from core.registry import Registry

class Component:
    def __init__(self, obj_id : int, type : str, data : dict):
        self.obj_id = obj_id
        self.type = type
        self.data = data

class Components:
    def __init__(self):
        # type is primary because the main consumer is systems which operate over types 
        self.components = {}

    def add_component(self, component : Component):
        if not component.type in self.components:
            self.components[component.type] = []
        self.components[component.type].append(component)

    def get_type(self, type : str):
        return self.components[type]