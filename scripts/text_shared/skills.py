from core.registry import Registry
from core.events import Events
from core.components import Components, Component
from scripts.text_shared.utility import make_print
from scripts.text_shared.contexts import UseSkillContext
from dataclasses import dataclass
from core.context import Context

# @dataclass
# class SkillData:
#     verb : str
#     description : 

def on_start(context : Context):
    global pprint
    pprint = make_print(context)

    reg : Registry = context.registry
    ev : Events = context.events
    verbs = reg.get_script_names("verbs")
    for verb in verbs:
        split = verb.split(".")
        if split[-1] == "on_call":
            print(f"Registered script {verb} to event use_skill_{split[-2]}")
            ev.add_trigger(f"use_skill_{split[-2]}", verb)
            ev.add_trigger(f"attempt_{split[-2]}", "skills.on_attempt")

def on_attempt(context : UseSkillContext):
    skills : list[Component] = context.components.on_object(context.source, "skills")
    if len(skills) > 0:
        skills = skills[0]
    if context.verb in skills:
        context.events.fire_event(f"use_skill_{context.verb}", context)
    else:
        pprint(f"You can't use {context.verb}.")

__register__ = [on_start, on_attempt]