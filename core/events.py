from core.registry import Registry

class Events:
    def __init__(self, my_registry : Registry):
        self.registry = my_registry
        self.triggers = {}
    
    def add_trigger(self, event_name, script):
        if not self.registry.has(script):
            raise ValueError("No such script exists in registry.")
        if not event_name in self.triggers:
            self.triggers[event_name] = []
        self.triggers[event_name].append(script)

    def fire_event(self, event_name, **kwargs):
        if not event_name in self.triggers:
            return
        for script in self.triggers[event_name]:
            self.registry.execute(script, **kwargs)