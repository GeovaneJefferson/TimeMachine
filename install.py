import subprocess as sub
import os
import pathlib
import shutil
from pathlib import Path


class CLI:
    def __init__(self):
        # Folders
        self.home_user = str(Path.home())
        self.getCurrentLocation = pathlib.Path().resolve()  # Current folder

        # Compatible system
        self.ubuntu = False
        self.opensuse = False

        # Terminal commands
        self.createCmd = "mkdir"

        # Default
        # Current folder
        self.src_backup_check = "src/desktop/backup_check.desktop"
        self.src_timemachine_desktop = "src/desktop/timemachine.desktop"
        self.src_service = "src/desktop/service.desktop"

        # Destination folder
        self.dst_venv_loc = f"{self.home_user}/.local/share/timemachine/venv"
        self.dst_folder_timemachine = f"{self.home_user}/.local/share/timemachine"
        self.dst_timemachine_desktop = f"{self.home_user}/.local/share/applications/timemachine.desktop"
        self.dst_kde_service = f"{self.home_user}/.local/share/kservices5/ServiceMenus"
        self.restore_icon = f"{self.home_user}/.local/share/timemachine/src/icons/restore_48.png"
        self.create_autostart_folder = f"{self.home_user}/.config/autostart"

        self.check_system()

    def check_system(self):
        ################################################################################
        ## Check system (Ubuntu, Opensuse etc.)
        ################################################################################
        sub.run("pkexec")
        output = os.popen("cat /etc/os-release") # uname -v
        output = output.read()

        if "ubuntu" in output:
            self.ubuntu = True

        elif "opensuse" in output:
            self.opensuse = True

        self.requeriments()

    def requeriments(self):
        ################################################################################
        ## Install pip (Python3)
        ################################################################################
        if self.ubuntu:
            try:
                sub.run("pkexec apt install python3-pip libnotify-bin", shell=True)
                print("Python3-pip was installed.")

            except :
                print("Error trying to install python3-pip!")
                exit()

        ################################################################################
        ## Install pip (Python3)
        ################################################################################
        elif self.opensuse:
            try:
                sub.run("pkexec zypper install python3-pip", shell=True)
                print("Python3-pip was installed.")

            except:
                print("Error trying to install python3-pip!")
                exit()

        ################################################################################
        ## Install PySide6
        ################################################################################
        if self.ubuntu or self.opensuse:
            try:
                sub.run("pip install pyside6", shell=True)
                print("PySide6 was installed.")

            except :
                print("Error trying to install PySide6!")
                exit()

        else:
            print("None compatible system found.")
            print("Could not install python3-pip and PySide6.")
            print("You have to install manually..")

        self.begin_to_install()

    def begin_to_install(self):
        ################################################################################
        ## Create autostart folder
        ################################################################################
        try:
            if os.path.exists(self.create_autostart_folder):
                pass
            else:
                sub.run(f"{self.createCmd} {self.create_autostart_folder}", shell=True)

        except FileNotFoundError:
            print("Error trying to create autostart folders insise users home!")

        ################################################################################
        ## Create Kservices folder
        ################################################################################
        try:
            if os.path.exists(f"{self.home_user}/.local/share/kservices5/"):
                pass
            else:
                sub.run(f"{self.createCmd} {self.home_user}/.local/share/kservices5/", shell=True)
        
        except FileNotFoundError:
            print("Error trying to create KDE services folder! (Needs for the restore feature)")
            pass
        ################################################################################
        ## Create Services Menus folder
        ################################################################################
        try:
            if os.path.exists(f"{self.home_user}/.local/share/kservices5/ServiceMenus/"):
                pass
            else:
                sub.run(f"{self.createCmd} {self.home_user}/.local/share/kservices5/ServiceMenus/", shell=True)
        
        except FileNotFoundError:
            print("Error trying to create KDE services folder! (Needs for the restore feature)")
            pass

        ################################################################################
        ## Create applications folder
        ################################################################################
        try:
            # Kdeservices extensions
            if os.path.exists(f"{self.home_user}/.local/share/applications/"):
                pass
            else:
                sub.run(f"{self.createCmd} {self.home_user}/.local/share/applications/", shell=True)
                
        except FileNotFoundError:
            print("Error trying to create applications folder inside users home!")
            pass

        ################################################################################
        ## Copy all .desktop 
        ################################################################################
        with open(self.src_backup_check, "w") as writer:    # Modify backup_check.desktop and add username to it
            writer.write(
                f"[Desktop Entry]\n "
                f"Type=Application\n "
                f"Exec=/bin/python3 {self.home_user}/.local/share/timemachine/src/backup_check.py\n "
                f"Hidden=false\n "
                f"NoDisplay=false\n "
                f"Name=Time Machine\n "
                f"Comment=Backup your files\n "
                f"Icon={self.restore_icon}")

        with open(self.src_timemachine_desktop, "w") as writer:     # Modify timemachine.desktop and add username to it
            writer.write(
                f"[Desktop Entry]\n "
                f"Version=1.0\n "
                f"Type=Application\n "
                f"Name=Time Machine\n "
                f"Comment=Backup your files\n "
                f"Icon={self.home_user}/.local/share/timemachine/src/icons/restore.png\n "
                f"Exec=python3 {self.home_user}/.local/share/timemachine/src/gui.py\n "
                f"Path={self.home_user}/.local/share/timemachine/\n "
                f"Categories=System\n "
                f"StartupWMClass=Gui.py\n "
                f"Terminal=false")
        
        with open(self.src_service, "w") as writer:     # Modify service.desktop and add username to it
            writer.write(
                f"[Desktop Entry]\n "
                f"Version=1.0\n "
                f"Type=Service\n "
                f"ServiceTypes=KonqPopupMenu/Plugin\n "
                f"MimeType=application/octet-stream;\n "
                f"Actions=EnterTimeMachine;\n "
                f"X-KDE-Priority=TopLevel\n "
                f"X-KDE-StartupNotify=false\n "
                f"Icon={self.home_user}/.local/share/timemachine/src/icons/restore.png\n\n "
                
                f"[Desktop Action "
                f"EnterTimeMachine]\n "
                f"Icon={self.home_user}/.local/share/timemachine/src/icons/restore.png\n "
                f"Name=Enter Time Machine\n "
                f"Exec=sh {self.home_user}/.local/share/timemachine/src/scripts/getDir.sh")

        try:
            # Copy current Time Machine folder to user
            shutil.copytree(self.getCurrentLocation, self.dst_folder_timemachine)       # Copy current folder to destination folder
            shutil.copy(self.src_timemachine_desktop, self.dst_timemachine_desktop)     # Copy .desktop and .timemachine.desktop to destination folder
            shutil.copy(self.src_service, self.dst_kde_service)     # Copy service.desktop

            sub.run(f"rm -rf {self.dst_venv_loc}", shell=True)        # Remove venv folder from user

            print("Program was installed!")
 
        except FileExistsError:
            print("Program is already installed!")

        exit()


app = CLI()
