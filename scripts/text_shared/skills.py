from core.registry import Registry
from core.events import Events
from core.components import Components, Component
from scripts.text_shared.utility import make_print
from dataclasses import dataclass

# @dataclass
# class SkillData:
#     verb : str
#     description : 

def on_start(**context):
    global pprint
    pprint = make_print(**context)

    reg : Registry = context["registry"]
    ev : Events = context["events"]
    verbs = reg.get_script_names("verbs")
    for verb in verbs:
        split = verb.split(".")
        if split[-1] == "on_call":
            print(f"Registered script {verb} to event use_skill_{split[-2]}")
            ev.add_trigger(f"use_skill_{split[-2]}", verb)
            ev.add_trigger(f"attempt_{split[-2]}", "skills.on_attempt")

def on_attempt(**context):
    components : Components = context["components"]
    sender = context["sender"]
    skills : list[Component] = components.on_object(sender, "skills")
    verb : str = context["verb"]
    ev : Events = context["events"]
    if len(skills) > 0:
        skills = skills[0]
    if context["verb"] in skills:
        ev.fire_event(f"use_skill_{verb}", **context)
    else:
        pprint(f"You can't use {verb}.")

__register__ = [on_start, on_attempt]