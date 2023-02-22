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
ev.fire_event("on_mount", context=Context(ev, components))

while True:
    ev.fire_event("on_tick", text="Hello there!", context=Context(ev,components))
    time.sleep(1)