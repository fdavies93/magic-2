import time
from core.registry import Registry
from core.events import Events
from core.context import Context
from core.components import Components

reg = Registry()
reg.import_scripts("scripts")

components = Components()

ev = Events(reg)
ev.mount_default_events()

global_context = Context(ev,components)
ev.fire_event("on_mount", context=global_context)

ev.fire_event("on_start", context=global_context)

timestamp = 0
while True:
    ev.fire_event("on_tick", timestamp=timestamp, context=global_context)
    timestamp += 1
    time.sleep(1)