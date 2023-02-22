from core.context import Context
from core.events import Events
from core.components import Components

def test_1(**kwargs):
    context : Context = kwargs["context"]
    print(kwargs["text"])

def test_2(**kwargs):
    print("Mounted successfully!")

__register__ = {
    "on_tick": test_1,
    "on_mount": test_2
}