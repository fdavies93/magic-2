from abc import ABC
from core.events import Events
from core.components import Components

# A system is interested in certain component types only
# Because it generally does things with them each frame, it consumes events to achieve this
class System(ABC):
    def __init__(self, events : Events, components : Components):
        # it doesn't need direct access to the registry as this can be mediated via events
        self.events = events
        self.components = components