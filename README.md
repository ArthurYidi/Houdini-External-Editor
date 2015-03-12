# Houdini Edit in External Editor

![parm-menu](https://raw.githubusercontent.com/wiki/ArthurYidi/Houdini-External-Editor/images/parm-menu.png)

### Features
- Quickly edit parameters and snippets with your favorite editor.
- No manual setup required. Looks for popular editors installed in your computer and
  automatically sets them up for you.
- No longer a five step process to edit a parameter with an external editor.
- When deleting a parameter value it doesn't leave it in an error state.
- Works with Houdini 13 and 14

### Quick Installation

- [Download](https://github.com/ArthurYidi/Houdini-External-Editor/archive/master.zip)

Add the following files to your [Houdini home folder](#houdini-home-folder):
- `PARMmenu.xml`
- `MainMenuCommon.xml`

To try out the plugin without editing your home folder: Add the files where your `.hip` file is located.

If your current editor configuration is not working go to `Edit > Configure External Editor`.

-----------------------------------

### Hotkeys

**Houdini 14**

- In `Edit > Hotkeys...`:
    - `Search` for `Edit in External Editor`
    - Set your hotkey to `Cmd + E`

**Houdini 13**

- In `Edit > Hotkeys...`:
    - `Search` for `Edit in External Editor`
    - Set your hotkey to `Alt + E`

__Note__: Don't disable the other `Alt + E` or `Cmd + E` hotkeys, since that will disable the hotkey for opening with external editor inside `Edit Operator Type Properties`.


### Caveat
- Problem: Hotkey doesn't work when editing snippets (multiple line strings) such
  as Wrangle nodes. <sup>[1]</sup>
- Solution: Click outside the text input and hover the parameter name then
  use your hotkey, or use the right click menu.

![hotkey-bug](https://raw.githubusercontent.com/wiki/ArthurYidi/Houdini-External-Editor/images/hotkey-bug.png)

<sup>[1] Houdini 14 & 13 switches the context (grabbing the keyboard) when inside a text input therefore disabling the hotkeys of the parameter menu.</sup>

### Troubleshooting 
- Go to `Edit > Configure External Editor` to edit your configuration.

- If manually configuring the editor make sure to add a wait or no-fork command
  if necessary. 

-----------------------------------

### Tips
The best editors allow you to close the window and not the application to
return to Houdini, and feature fast start up times.

If using Sublime add the following options to disable opening old unsaved edits:

    "hot_exit": false,
    "remember_open_files": false,

Houdini only supports ASCII paths.

Make sure to quote your path if it contains spaces or arguments, refer to [wiki](https://github.com/ArthurYidi/Houdini-External-Editor/wiki/Manual-External-Editor-Configuration) for help.

If you use TextEdit make sure to quit the application and not the window. If you accidently close the window, open TextEdit again and quit the application.

----------------------------------
### Manual Setup

[Refer to wiki for more information and examples.](https://github.com/ArthurYidi/Houdini-External-Editor/wiki/Manual-External-Editor-Configuration)

----------------------------------
### Editor Configuration

[Refer to wiki for configuring your editor to support `VEX`, `HScript`, and `HOM`](https://github.com/ArthurYidi/Houdini-External-Editor/wiki/Editor-Configuration)

----------------------------------

### Uninstall
In your Houdini home folder:
- Go to `Edit > Configure External Editor` and set `Use System Setting`
- Quit Houdini.
- Remove `PARMmenu.xml` and `MainMenuCommon.xml`

----------------------------------

### Upcoming Features
- Watching for changes and not halting the main thread! (Also removes confusion)
- Editing multiple parameters at the same time.
- If the parameter is a file provide option to open the file instead.
- Submit ideas or pull requests!

----------------------------------
### Houdini Home Folder

The default location of your Houdini home folder:

- Mac: `~/Library/Preferences/houdini/13.0`
- Linux: `~/houdini13.0`
- Windows: `~/Documents/houdini13.0`

Also accessed by:

`>>> hou.homeHoudiniDirectory()`

[Refer to docs for more help.](http://www.sidefx.com/docs/current/basics/config_env)

----------------------------------

### License
Copyright (C) 2015  Arthur Yidi

BSD Simplified
