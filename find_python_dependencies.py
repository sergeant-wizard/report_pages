import modulefinder
import sys

finder = modulefinder.ModuleFinder(
    path=['.'],
)
this = sys.argv[1]
finder.run_script(this)

print(this)

for mod in finder.modules.values():
    if mod.__file__ != this:
        print(mod.__file__)
