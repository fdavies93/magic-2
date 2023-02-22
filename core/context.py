from core.events import Events
from core.components import Components

class Context:
    def __init__(self, event_system : Events, component_system : Components):
        self.events = event_system
        self.components = component_system