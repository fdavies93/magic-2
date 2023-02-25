from core.registry import Registry
from core.events import Events
from scripts.utility import make_print

def on_start(**context):
    reg : Registry = context["registry"]
    ev : Events = context["events"]
    verbs = reg.get_script_names("verbs")
    for verb in verbs:
        split = verb.split(".")
        if split[-1] == "on_call":
            print(f"Registered script {verb} to event use_skill_{split[-2]}")
            ev.add_trigger(f"use_skill_{split[-2]}", verb)

__register__ = [on_start]