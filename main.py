import time
from core.registry import Registry
from core.events import Events

reg = Registry()
reg.import_scripts("scripts")

ev = Events(reg)
ev.add_trigger("tick", "hello")

while True:
    ev.fire_event("tick")
    time.sleep(1)