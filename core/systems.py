from abc import ABC
from core.events import Events
from core.components import Components

class System(ABC):
    def __init__(self, events : Events, components : Components):
        # it doesn't need direct access to the registry as this can be mediated via events
        self.events = events
        self.components = components