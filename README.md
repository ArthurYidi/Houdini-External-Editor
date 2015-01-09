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
Replacing 'Alt + E':
- In 'Edit > Hotkeys...' press 'Search' for 'Open Editor':
    - Remove /Houdini/Panes/Texport/Open Editor
    - Remove /Input Fields/Open Editor

- Then   

Or

- Append the following to HotkeyOverrides in your Houdini home folder:
    h.pane.parms.edit_expression_external	"Edit w/ External Editor"	"Custom Menu Operation: Edit w/ External Editor"	 Alt+E
    h.pane.textport.editor	"Open Editor"	"Open Editor"	
    inputfield.editor	"Open Editor"	"Open editor"	

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

-----------------------------------

### Manual Configuration
Houdini

Go to `Edit > Configure External Editor` and follow the prompts.

System Wide

Mac & Linux

Edit `~/.bash_profile`:
    `export VISUAL=/path/to/editor`

Windows 7+
`setx VISUAL C:\path\to\editor`


### Manual Environment Variable Setup
In `Edit > Configure External Editor` choose `Other` or `Edit Current Setting`.
Then using the following examples to setup your editor.

Sublime

subl -w
"/Applications/Sublime Text 3.app/Contents/SharedSupport/bin/subl" -w
"/Applications/Sublime Text.app/Contents/SharedSupport/bin/subl" -w

MacVim

mvim -f
/Applications/MacVim.app/Contents/MacOS/Vim -gfn

gvim

gvim -f

TextMate

/Applications/TextMate.app/Contents/Resources/mate -w

Emacs

/Applications/Emacs.app/Contents/MacOS/Emacs

TextWrangler

/Applications/TextWrangler.app/Contents/Helpers/edit -w

Xcode

/Applications/Xcode.app/Contents/MacOS/Xcode

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
