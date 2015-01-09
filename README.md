# Houdini Edit w/ External Editor

### Features
- Quickly edit parameters and snippets with your favorite editor.
- No manual setup required. Looks for popular editors installed in your computer and
  automatically sets them up for you.
- No longer a five step process to edit a parameter with an external editor.
- When deleting a parameter value it is doesn't leave the parameter in an error state.

### Quick Installation
Add the files `PARMmenu.xml`, `MainMenuCommon.xml`, and `extEditor.py` to your Houdini home folder:
    Mac
    `$HOME/Library/Preferences/houdini/13.0`

    Linux & Windows
    `$HOME/houdini13.0`

To try out the plugin without editing your home folder:
    Add the files where your `.hip` file is located.

- If your current editor configuration is not working go to `Edit > Configure
  External Editor` to set it up.

-----------------------------------

### Hotkeys
Replacing `Alt + E`:
- In `Edit > Hotkeys...` press `Search` for `Open Editor`:
    - Remove `/Houdini/Panes/Texport/Open Editor`
    - Remove `/Input Fields/Open Editor`

- Finally, set your custom hotkey for `Edit w/ External Editor`.

- Example setting is provied in (HotKeyOverride)[HotKeyOverride.example].

### Caveat
- Problem: Hotkey doesn't work when editing snippets (multiple line strings) such
  as Wrangle nodes. [1]
- Solution: Click outside the text editor and hover the parameter name then
  click your hotkey.

[1] Houdini has a bug that disables hotkeys of the parameter menu when the
context is inside the snippet text editor.

### Troubleshooting 
- Go to `Edit > Configure External Editor` to edit your configuration.

- If manually configuring the editor make sure to add a wait or no-fork command
  if necessary. 

-----------------------------------

### Tips
The best editors allow you to close the window and not the application to
return to Houdini, and feature fast start up times.

If using Sublime add the following options to disable opening old unsaved edits:

    `"hot_exit": false,`
    `"remember_open_files": false,`

Houdini only supports ASCII paths.

Make sure to quote your path if it contains spaces or arguments, see manual
setup examples below.

If you use TextEdit make sure to quit the application and not the window.
If you accidently close the window, open TextEdit again and quit the application.

----------------------------------
### Manual Setup

[Refer to wiki for more information and examples.](wiki/Manual-External-Editor-Configuration)

----------------------------------
### Uninstall
In your Houdini home folder:
- Quit Houdini.
- Remove `PARMmenu.xml`, `Main.xml`, and `extEditorParm.py`
- Remove any lines starting with `VISUAL` in `houdini.env`

----------------------------------

### Upcoming Features
- Watching for changes and not halting the main thread! (Also removes confusion)
- Editing multiple parameters at the same time.
- Submit ideas or pull requests!

### License
Copyright (C) 2015  Arthur Yidi
BSD Simplified
