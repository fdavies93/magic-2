from core.registry import Registry

class Component:
    def __init__(self, obj_id : int, type : str, data : dict):
        self.obj_id = obj_id
        self.type = type
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

class Components:
    def __init__(self):
        # type is primary because the main consumer is systems which operate over types 
        self.components : dict[str, list[Components]] = {}
        self.by_id : dict[int, list[Component]] = {}
        self.cur_id : int = 0

    def add(self, component : Component):
        if not component.type in self.components:
            self.components[component.type] = []
        if not component.obj_id in self.by_id:
            self.by_id[component.obj_id] = []
        self.components[component.type].append(component)
        self.by_id[component.obj_id].append(component)

    def on_object(self, id : int, type : str = None):
        comps = self.by_id[id]
        if type != None:
            comps = list(filter(lambda comp : comp.type == type, comps))
        return comps

    def of_type(self, type : str) -> list[Component]:
        return self.components[type]
    
    def get_next_id(self) -> int:
        to_return = self.cur_id
        self.cur_id += 1
        return to_return