from os import walk, listdir
from os.path import isfile, splitext, join, isdir
from importlib import import_module
from importlib.util import spec_from_file_location, module_from_spec
import sys

class Registry:
    def __init__(self):
        self.scripts = {}

    def execute(self, name, **kwargs):
        # Should be able to disable scripts in registry so they can't execute
        # For convenience, config, and testing purposes
        if not name in self.scripts:
            # should this throw an error?
            raise ValueError(f"No script with name {name} found in registry.")
        return self.scripts[name](**kwargs)
    
    def get_script_names(self, path = "") -> list[str]:
        script_names = list(self.scripts.keys())
        script_names = list(filter(lambda name : name[:len(path)] == path, script_names))
        return script_names

    def has(self, script):
        return script in self.scripts

    def add_from_register(self, path, module_name):
        print(f"Caching functions from {path}")
        spec = spec_from_file_location(module_name, path)
        module = module_from_spec(spec)        
        spec.loader.exec_module(module)
        if not hasattr(module, "__register__"):
            return
        if not isinstance(module.__register__, (list, dict)):
            return
        if isinstance(module.__register__, list):
            for func in module.__register__:
                script_name = ".".join((module_name,func.__name__))
                print(f"Import {func.__name__} as {script_name}")
                self.scripts[script_name] = func
        if isinstance(module.__register__, dict):
            for name, func in module.__register__.items():
                script_name = ".".join((module_name,name))
                print(f"Import {func.__name__} as {script_name}")
                self.scripts[script_name] = func
        print(self.scripts)


    def import_scripts(self, script_path = "./scripts", base_name = None, script_config = None):
        # TODO:
        # - Add recursive imports
        # - Config option to disable scripts / specify default state
        modules = listdir(script_path)
        print(modules)
        for module in modules:
            if base_name != None:
                cur_name = ".".join((base_name, module))
            else:
                cur_name = module

            if isdir(join(script_path, module)):
                self.import_scripts(join(script_path, module), cur_name, script_config)
                continue
            elif not isfile(join(script_path, module)):
                # unclear if this will ever trigger, but possibly guards against symbolic link weirdness
                continue
            if module[:2] == "__":
                continue
            split_name = splitext(cur_name)
            if split_name[1] != ".py":
                continue
            # scan all functions and add to module
            self.add_from_register(join(script_path, module), split_name[0])