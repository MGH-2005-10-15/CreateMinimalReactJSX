"""
Setting up MERN Client side
Using Vite React, Tailwindcss, Bootstrap icons
Created by @MGH2005
https://github.com/MGH-2005-10-15/CreateMinimalReactJSX
Last Update : 2025-09-19
"""
import os
import platform
import subprocess
from subprocess import CompletedProcess
from sys import exit
import reactfiles
import time

os_name = platform.system()
if not(os_name == "Windows") and not(os_name == "Linux") and not(os_name == "Darwin"):
    print(f"Sorry this program cannot run on {os_name}")
    exit(0) # exit the program

__dirname = os.getcwd()

class ReactFolders:
    def __init__(self, root):
        self.root = ''
        if(os.path.isdir(root)):
            self.root = os.path.abspath(root)
        self.public = os.path.join(self.root, 'public')
        self.src = os.path.join(self.root, 'src')
        self.assets = os.path.join(self.src, 'assets')

    def checkfolders(self) -> bool:
        return (
            os.path.exists(self.root)
            and os.path.exists(self.public)
            and os.path.exists(self.src)
            and os.path.exists(self.assets)
            )

def introduction():
    print(f"Creating Vite React Client in {__dirname}")
    print("Executing commands in powershell")
    print("Vite@Latest, Tailwind css, Bootstrap icons")
    print("===========================================")

def execute_command_powershell(cmd:str, dir):
    if not(os.path.exists(dir)):
        return CompletedProcess(
            args='',
            returncode=1,
            stdout='',
            stderr=f"Error {dir} not defined"
        )
    try:
        results = subprocess.run(
            args=["powershell", "-Command", cmd],
            cwd=dir,
            check=False,  # We check exception ourselves
            text=True,
            capture_output=True
        )
        return results
    except Exception as e:
        return CompletedProcess(
            args=["powershell", "-Command", cmd],
            returncode=1,
            stdout='',
            stderr=f"Exception: {str(e)}"
        )

def execute_command_bash(cmd:str, dir) -> CompletedProcess:
    if not(os.path.exists(dir)):
        return CompletedProcess(
            args='',
            returncode=1,
            stdout='',
            stderr=f"Error {dir} not defined"
        )
    try:
        results = subprocess.run(
            args=["bash","-c",cmd],
            cwd=dir,
            check=False,  # We check exception ourselves
            text=True,
            capture_output=True
        )
        return results
    except Exception as e:
        return CompletedProcess(
            args=["bash","-c",cmd],
            returncode=1,
            stdout='',
            stderr=f"Exception: {str(e)}"
        )

def execute_command(cmd:str, dir) -> CompletedProcess:
    OS = platform.system()
    if(OS == "Windows"):
        return execute_command_powershell(cmd, dir)
    elif(OS == "Linux") or (OS == "Darwin"):
        return execute_command_bash(cmd, dir)
    else:
        return CompletedProcess(
            args='',
            returncode=1,
            stdout='',
            stderr=f"Error program cannot run on {OS}"
        )

def overwrite_file(filename, data) -> bool:
    try:
        file = open(filename, "w+")
        file.write(data)
    except:
        return False
    file.close()
    return True

def delete_file(filename):
    if not(os.path.exists(filename)):
        return False
    try:
        os.remove(filename)
    except:
        return False
    return True

def automate_process():
    cwd = os.getcwd()
    print(f"Process in {cwd}")
    if (os.path.exists(os.path.join(cwd, "client"))):
        print("Directory client already exists, please rename client folder or delete it")
        return
    #------------------------------------------------------------
    cmd = "npm create vite@latest client -- --template react" # first command
    result = execute_command(cmd, cwd)
    if (result.returncode != 0):
        print("Error: " + str(result.stderr))
        return
    print("Vite React created")
    # ------------------------------------------------------------
    try:
        os.chdir("client")
    except:
        print("Error changing directory exiting process...")
        return
    cwd = os.getcwd()  # ./client/
    react = ReactFolders(cwd)
    if not(react.checkfolders()):
        print("Error some folders missing in ./client")
        return
    # ------------------------------------------------------------
    cmd="npm install" # install npm
    result = execute_command(cmd, react.root)
    if (result.returncode != 0):
        print("Error: " + str(result.stderr))
        return
    print("npm installed")
    # ------------------------------------------------------------
    cmd = "npm install react-router-dom"
    result = execute_command(cmd, react.root)
    if (result.returncode != 0):
        print("Error: " + str(result.stderr))
        return
    print("react-router-dom installed")
    # ------------------------------------------------------------
    cmd = "npm install bootstrap-icons"
    result = execute_command(cmd, react.root)
    if (result.returncode != 0):
        print("Error: " + str(result.stderr))
        return
    print("bootstrap icons installed")
    # ------------------------------------------------------------
    cmd = "npm install -D tailwindcss@3 postcss autoprefixer"
    result = execute_command(cmd, react.root)
    if (result.returncode != 0):
        print("Error: " + str(result.stderr))
        return
    print("Tailwind css installed")
    # ------------------------------------------------------------
    cmd = "npx tailwindcss init -p"
    result = execute_command(cmd, react.root)
    if (result.returncode != 0):
        print("Error: " + str(result.stderr))
        return
    # ------------------------------------------------------------
    cwd = os.getcwd() # ./client/
    if(overwrite_file("tailwind.config.js", reactfiles.tailwindconfigjs)):
        print("tailwind.config.js modified")
    else:
        print("Error modifying tailwind.config.js")
        return
    # ------------------------------------------------------------
    if (overwrite_file("index.html", reactfiles.indexhtml)):
        print("index.html modified")
    else:
        print("Error modifying index.html")
        return
    # ------------------------------------------------------------
    if not(delete_file(os.path.join(react.public, "vite.svg"))):
        print("Error deleting vite.svg client/public")
        return
    # ------------------------------------------------------------
    if not(delete_file(os.path.join(react.assets, "react.svg"))):
        print("Error deleting react.svg client/src/assets")
        return
    # ------------------------------------------------------------
    try:
        components = os.path.join(react.src, "components")
        pages = os.path.join(react.src, "pages")
        os.mkdir(components)
        os.mkdir(pages)
    except:
        print("Error creating directories components, pages at client/src")
        return
    # ------------------------------------------------------------
    if (overwrite_file(os.path.join(react.src, "index.css"), reactfiles.indexcss)):
        print("index.css modified")
    else:
        print("Error modifying client/src/index.css")
        return
    # ------------------------------------------------------------
    if (overwrite_file(os.path.join(react.src, "App.css"), reactfiles.appcss)):
        print("App.css modified")
    else:
        print("Error modifying client/src/App.css")
        return
    # ------------------------------------------------------------
    if (overwrite_file(os.path.join(react.src, "main.jsx"), reactfiles.mainjsx)):
        print("main.jsx modified")
    else:
        print("Error modifying client/src/main.jsx")
        return
    # ------------------------------------------------------------
    if (overwrite_file(os.path.join(pages, "Home.jsx"), reactfiles.homejsx)):
        print("Home.jsx created")
    else:
        print("Error creating client/src/pages/Home.jsx")
        return
    # ------------------------------------------------------------
    if (overwrite_file(os.path.join(pages, "Home.module.css"), reactfiles.homemodulecss)):
        print("Home.module.css created")
    else:
        print("Error creating client/src/pages/Home.module.css")
        return
    # ------------------------------------------------------------
    if (overwrite_file(os.path.join(pages, "Signup.jsx"), reactfiles.signupjsx)):
        print("Signup.jsx created")
    else:
        print("Error creating client/src/pages/Signup.jsx")
        return
    # ------------------------------------------------------------
    if (overwrite_file(os.path.join(pages, "Signup.module.css"), reactfiles.signupmodulecss)):
        print("Signup.module.css created")
    else:
        print("Error creating client/src/pages/Signup.module.css")
        return
    # ------------------------------------------------------------
    if (overwrite_file(os.path.join(pages, "Login.jsx"), reactfiles.loginjsx)):
        print("Login.jsx created")
    else:
        print("Error creating client/src/pages/Login.jsx")
        return
    # ------------------------------------------------------------
    if (overwrite_file(os.path.join(react.src, "App.jsx"), reactfiles.appjsx)):
        print("App.jsx modified")
    else:
        print("Error modifying client/src/App.jsx")
        return

    print("React client project successfully created")
    print("Now run 'npm run dev' and enjoy developing")


if __name__=="__main__":
    start = time.perf_counter()
    introduction()
    automate_process()
    end = time.perf_counter()
    elapsed = end - start
    print(f"[{round(elapsed, 3)} seconds]")


