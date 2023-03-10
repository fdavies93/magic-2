from core.registry import Registry

# It might be worthwhile implementing events as a priority queue which accumulates each update
# This should allow better behaviour with more complex systems without having a ton of different
# events messing up the namespace.
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

    def fire_event(self, event_name, context):
        if not event_name in self.triggers:
            return False
        for script in self.triggers[event_name]:
            self.registry.execute(script, context)
        return True

    def mount_default_events(self):
        defaults = { "on_mount", "on_start", "on_tick", "on_shutdown" }
        available_scripts = self.registry.get_script_names()
        for script in available_scripts:
            script_parts = script.split(".")
            func_name = script_parts[-1]
            if func_name in defaults:
                self.add_trigger(func_name, script)
                print(f"Added trigger for {script} on {func_name}")