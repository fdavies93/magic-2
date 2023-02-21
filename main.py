from core.registry import Registry

reg = Registry()
reg.import_scripts("scripts")
reg.execute("hello")