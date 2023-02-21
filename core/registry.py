from os import walk, listdir
from os.path import isfile, splitext, join
from importlib import import_module
from importlib.util import spec_from_file_location, module_from_spec
import sys

class Registry:
    def __init__(self):
        self.scripts = {}

    def execute(self, name, **kwargs):
        if not name in self.scripts:
            # should this throw an error?
            raise ValueError(f"No script with name {name} found in registry.")
        return self.scripts[name](**kwargs)
    
    def get_script_names(self):
        return list(self.scripts.keys())

    def has(self, script):
        return script in self.scripts

    def add_from_register(self, path, name):
        print(f"Caching functions from {path}")
        spec = spec_from_file_location(name, path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        if not hasattr(module, "__register__"):
            return
        if not isinstance(module.__register__, (list, dict)):
            return
        if isinstance(module.__register__, list):
            for func in module.__register__:
                print(func.__name__)
                self.scripts[func.__name__] = func
        if isinstance(module.__register__, dict):
            for name, func in module.__register__.items():
                print(f"Import {func.__name__} as {name}")
                self.scripts[name] = func
        print(self.scripts)


    def import_scripts(self, script_path = "./scripts", script_config = None):
        # extra config unused for now, but probably useful for avoiding clashes and lack of clarity later
        # non-recursive implementation for now, could be made recursive later with name fudging
        scripts = listdir(script_path)
        print(scripts)
        for script in scripts:
            if not isfile(join(script_path, script)):
                continue
            if script[:2] == "__":
                continue
            split_name = splitext(script)
            if split_name[1] != ".py":
                continue
            # scan all functions and add to module
            self.add_from_register(join(script_path, script), split_name[0])