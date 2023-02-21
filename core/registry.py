from os import walk, listdir
from os.path import isfile, splitext, join
from importlib import import_module
from importlib.util import spec_from_file_location, module_from_spec
import sys

class Registry:
    def __init__(self):
        self.scripts = {}

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
            print(f"Caching functions from {script}")
            spec = spec_from_file_location(split_name[0], join(script_path, script))
            module = module_from_spec(spec)
            # sys.modules[split_name[0]] = module
            spec.loader.exec_module(module)
            print(dir(module))