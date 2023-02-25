# Magic 2 Engine

## Technical Notes

### Where to Store Data
* For readily-serialised game data such as object positions, throw them onto a component by using the components system from context.
* For game systems included in scripts, such as input and output systems, store them in a module-level variable. This means they will be loaded at *runtime* and avoids having to flag certain types of component as unserialisable.
* For complex config of the framework itself, consider creating a data file including any config options.