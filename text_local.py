import time
from core.registry import Registry
from core.events import Events
from core.components import Components
from core.interfaces.CursesIO import CursesIO
from core.context import Context, TickContext

reg = Registry()
reg.import_scripts("scripts/text_shared")
reg.import_scripts("scripts/text_local")

components = Components()

ev = Events(reg)
ev.mount_default_events()

context = Context(ev, components, reg)

ev.fire_event("on_mount", context)
ev.fire_event("on_start", context)

timestamp = 0

try:
    while True:
        ev.fire_event("on_tick", TickContext(timestamp, context))
        timestamp += 1
        time.sleep(1.0 / 32)
finally:
    ev.fire_event("on_shutdown", context)