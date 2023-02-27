from typing import Union
from abc import ABC
from core.registry import Registry

# Should data be a straight dict or a dataclass?
# Former is easier to use; latter allows code completion and better self-documenting behaviour.
# Or should component be an ABC like Unity's Monobehaviour?
class Component(ABC):
    def __init__(self, obj_id : int, type : str, data : dict):
        self.obj_id = obj_id
        self.type = type
        self.data = data

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __contains__(self, key):
        return key in self.data

class Components:
    def __init__(self):
        # type is primary because the main consumer is systems which operate over types 
        self.components : dict[str, list[Component]] = {}
        self.by_id : dict[int, list[Component]] = {}
        self.cur_id : int = 0

    def add(self, component : Component):
        if not component.type in self.components:
            self.components[component.type] = []
        if not component.obj_id in self.by_id:
            self.by_id[component.obj_id] = []
        self.components[component.type].append(component)
        self.by_id[component.obj_id].append(component)

    def disambiguate_type(self, type_of : Union[str, type]) -> str:
        type_str = type_of
        if not isinstance(type_str, str):
            type_str = type_str.__name__
        return type_str

    def on_object(self, id : int, type_of : Union[str, type] = None):
        comps = self.by_id[id]
        if type_of != None:
            comps = list(filter(lambda comp : comp.type == self.disambiguate_type(type_of), comps))
        return comps

    def of_type(self, type_of : Union[str, type]) -> list[Component]:
        return self.components[self.disambiguate_type(type_of)]
    
    def get_next_id(self) -> int:
        to_return = self.cur_id
        self.cur_id += 1
        return to_return