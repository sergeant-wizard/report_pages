import modulefinder
import sys

finder = modulefinder.ModuleFinder(
    path=['.'],
)
this = sys.argv[1]
finder.run_script(this)

for mod in finder.modules.values():
    print(mod.__file__)
