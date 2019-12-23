import modulefinder
import sys

finder = modulefinder.ModuleFinder(
    path=['.'],
)
finder.run_script(sys.argv[1])

for mod in finder.modules.values():
    print(mod.__file__)
