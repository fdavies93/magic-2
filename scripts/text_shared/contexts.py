from core.context import Context
from dataclasses import dataclass

@dataclass
class OutputContext(Context):
    output : str

    def __init__(self, output : str, generic : Context):
        self.load_generic(generic)
        self.output = output

@dataclass
class InputContext(Context):
    source : int
    text : str

    def __init__(self, source : int, text : str, generic : Context):
        self.load_generic(generic)
        self.source = source
        self.text = text

@dataclass
class UseSkillContext(Context):
    source : int
    verb : str
    args : list[str]

    def __init__(self, source : int, verb : str, args : list[str], generic : Context):
        self.load_generic(generic)
        self.source = source
        self.verb = verb
        self.args = args