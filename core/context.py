from dataclasses import dataclass
from core.events import Events
from core.components import Components
from core.components import Registry

@dataclass
class Context:
    events : Events
    components : Components
    registry : Registry

    def make_generic(self):
        return Context(self.events, self.components, self.registry)
    
    def load_generic(self, context : "Context"):
        self.events = context.events
        self.components = context.components
        self.registry = context.registry

@dataclass
class TickContext(Context):
    timestamp : int

    def __init__(self, timestamp : int, generic : Context):
        self.load_generic(generic)
        self.timestamp = timestamp