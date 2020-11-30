### Requirements and dependencies:
* Linux computer (Windows support planned, Cygwin might work)
* Python 3
* PyQt5

### How to use these scripts:
* myjson.py is a supporting library and does not get used directly
* decompile_bas.py is run directly with no arguments and attempts to find ALL *.bas files (not *.Bas or *.BAS etc) and will convert it to JSON.
* compile.py is run directly with no arguments and will find all *.json files (not *.Json or *.JSON or *.JsOn etc) and will convert them to .bas or ilb. These files are then compiled into a single "set_compiled.bas" file which you can use as a custom set in your mod

### How to mod using these scripts:
* If you add a new building, you need to update set*/scripts/set.sdf
* If you add a new vehicle/explosion, you need to update set*/scripts/visproto.lst
* New bitmaps/animations/skeletons are found automatically and added to the output set
* Use GIMP to edit the BMP files. Choose File -> Overwrite *.bmp option. Make sure the output file size is still 66,614 bytes.

### Notes:
* Single load mode is when UA trys to load each model from its own file.
* Single load compilation can be enabled if you uncomment "# compile_single_files(set_number)" in compile.py
* Slurps is another name for the list of ground skeletons/wireframes/objects


### Things to change:
* The Windows 10 Subsystem for Linux might let the script work on Windows
