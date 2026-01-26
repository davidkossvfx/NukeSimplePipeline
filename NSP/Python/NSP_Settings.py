# NSP_Settings v003

import nuke
import os

# Import the projects_dir variable from NSP/init.py
from NSP.init import projects_dir, user, show

scriptDir = os.path.dirname(os.path.abspath(__file__))
NSP_Dir = os.path.dirname(scriptDir)
usersDir = os.path.join(NSP_Dir, "Users")
showsDir = os.path.join(NSP_Dir, "Shows")

userList = os.listdir(usersDir)
showList = os.listdir(showsDir)

userList.append("[None]")
showList.append("[None]")

def NSP_Settings():

    settings = nuke.createNode("NSP_Settings.nk", inpanel=False)

    #Set default value for Projects Directory
    if projects_dir != None:
        settings.knob("newDir").setValue(projects_dir)
        settings.knob("currentDir").setValue(projects_dir)

    #Set default value for User
    settings.knob("newUser").setValues(userList)
    if user == None:
        settings.knob("newUser").setValue("[None]")
        settings.knob("currentUser").setValue("[None]")
    else:
        settings.knob("newUser").setValue(user)
        settings.knob("currentUser").setValue(user)

    #Set default value for Show
    settings.knob("newShow").setValues(showList)
    if show == None:
        settings.knob("newShow").setValue("[None]")
        settings.knob("currentShow").setValue("[None]")
    else:
        settings.knob("newShow").setValue(show)
        settings.knob("currentShow").setValue(show)

    settings.showControlPanel()

def update_settings():

    thisNode = nuke.thisNode()

    newDir = thisNode.knob("newDir").value()
    newUser = thisNode.knob("newUser").value()
    newShow = thisNode.knob("newShow").value()

    print (newDir)

    nsp_init = ".nuke/NSP/init.py"

    # Open the file in read mode
    with open(nsp_init, "r") as file:

        # Read the contents of the file
        lines = file.readlines()
        
        # Iterate through the lines
        for i, line in enumerate(lines):
            # Check if the line contains the "projects_dir" variable
            if "projects_dir =" in line:
                # Replace the entire line with the new variable
                lines[i] = "projects_dir = " + '"' + newDir + '"' + "\n"
                if newDir == "":
                    lines[i] = "projects_dir = " + "None" + "\n"

        # Iterate through the lines
        for i, line in enumerate(lines):
            # Check if the line contains the "user" variable
            if "user =" in line:
                # Replace the entire line with the new variable
                lines[i] = "user = " + '"' + newUser + '"' + "\n"
                if newUser == "[None]":
                    lines[i] = "user = " + "None" + "\n"

        # Iterate through the lines
        for i, line in enumerate(lines):
            # Check if the line contains the "show" variable
            if "show =" in line:
                # Replace the entire line with the new variable
                lines[i] = "show = " + '"' + newShow + '"' + "\n"
                if newShow == "[None]":
                    lines[i] = "show = " + "None" + "\n"

    # Open the file in write mode
    with open(nsp_init, "w") as file:
        # Write the modified lines back to the file
        file.writelines(lines)

def update_settings_exit():

    update_settings()
    nuke.scriptClear()
    nuke.scriptExit()
