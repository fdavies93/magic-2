import time
from core.registry import Registry
from core.events import Events
from core.components import Components

reg = Registry()
reg.import_scripts("scripts")

components = Components()

ev = Events(reg)
ev.mount_default_events()

context = {
    "events": ev,
    "components": components
}

ev.fire_event("on_mount", **context)

ev.fire_event("on_start", **context)

timestamp = 0
while True:
    ev.fire_event("on_tick", timestamp=timestamp, **context)
    timestamp += 1
    time.sleep(1)