#! /usr/bin/python3
from setup import *

# QTimer
timer = QtCore.QTimer()

################################################################
# Window management
################################################################
windowXSize = 900
windowYSize = 600

################################################################################
# Read file
################################################################################
config = configparser.ConfigParser()
config.read(src_user_config)

# Read INI file
iniExternalName = config['EXTERNAL']['name']
iniExternalLocation = config['EXTERNAL']['hd']
iniHDName = config['EXTERNAL']['name']
iniApplicationsPackages = config['RESTORE']['applications_packages']
iniApplicationData = config['RESTORE']['applications_data']
iniFilesAndsFolders = config['RESTORE']['files_and_folders']

iniIsRestoreRunning = config['RESTORE']['is_restore_running']
iniApplicationsPackages = config['RESTORE']['applications_packages']
iniApplicationData = config['RESTORE']['applications_data']
iniFilesAndsFolders = config['RESTORE']['files_and_folders']
# Current backup information
iniCurrentBackupInfo = config['INFO']['feedback_status']
# Get current notification ID
iniNotificationID = config['INFO']['notification_id']
# INFO
packageManager = config['INFO']['packageManager']

# Base folder
createBaseFolder = f"{iniExternalLocation}/{baseFolderName}"
# Backup folder
createBackupFolder = f"{iniExternalLocation}/{baseFolderName}/{backupFolderName}"
# Wallpaper main folder
wallpaperMainFolder = f"{iniExternalLocation}/{baseFolderName}/{wallpaperFolderName}"
# Application main folder
applicationMainFolder = f"{iniExternalLocation}/{baseFolderName}/{applicationFolderName}"
# Application main Var folder
applicationVarFolder = f"{iniExternalLocation}/{baseFolderName}/{applicationFolderName}/{varFolderName}"
# Application main Local folder
applicationLocalFolder = f"{iniExternalLocation}/{baseFolderName}/{applicationFolderName}/{localFolderName}"
# Check date inside backup folder
checkDateInsideBackupFolder = f"{iniExternalLocation}/{baseFolderName}/{backupFolderName}"

# PACKAGES
# RPM main folder
rpmMainFolder = f"{iniExternalLocation}/{baseFolderName}/{applicationFolderName}/{rpmFolderName}"
# DEB main folder
debMainFolder = f"{iniExternalLocation}/{baseFolderName}/{applicationFolderName}/{debFolderName}"

# Icons users folder
iconsMainFolder = f"{iniExternalLocation}/{baseFolderName}/{iconFolderName}"
# Themes users folder
themeMainFolder = f"{iniExternalLocation}/{baseFolderName}/{themeFolderName}"
# Cursosr users folder
cursorMainFolder = f"{iniExternalLocation}/{baseFolderName}/{cursorFolderName}"

# Flatpak txt file
flatpakTxtFile = f"{iniExternalLocation}/{baseFolderName}/{flatpakTxt}"


class WELCOMESCREEN(QWidget):
    def __init__(self, parent=None):
        super(WELCOMESCREEN, self).__init__(parent)
        self.widgets()

    def widgets(self):
        # Title layout
        self.titlelLayout = QVBoxLayout()
        self.titlelLayout.setSpacing(20)
        self.titlelLayout.setContentsMargins(20, 20, 20, 20)
        
        # Image       
        image = QLabel()
        image.setFixedSize(140, 140)
        image.setStyleSheet(
            "QLabel"
            "{"
            f"background-image: url({src_migration_assistant_96px});"
            "background-repeat: no-repeat;"
            "background-color: transparent;"
            "background-position: center;"
            "}")
        
        # Welcome
        self.title = QLabel()
        self.title.setFont(QFont("Arial", 34))
        self.title.setText("Migration Assistant")
        self.title.setAlignment(QtCore.Qt.AlignHCenter)
        self.title.setStyleSheet("""
        font-weight: Bold;
        """)

       # More description
        self.moreDescription = QLabel()
        self.moreDescription.setFont(QFont("Arial", 11))
        self.moreDescription.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.moreDescription.setText("Use Migration Assistant to restore information such as "
            "Applications, Files, Folders and more to this PC.") 

        ################################################################################
        # Buttons
        ################################################################################
        # Continue button
        self.continueButton = QPushButton(self)
        self.continueButton.setText("Continue")
        self.continueButton.setFont(QFont("Arial", 10))
        self.continueButton.adjustSize()
        self.continueButton.move(800, 555)
        self.continueButton.clicked.connect(self.on_continueButton_clicked)
        # self.continueButton.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex()+1))

        ###########################################################################
        # Add layouts and widgets
        ################################################################################
        self.titlelLayout.addWidget(self.title, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.titlelLayout.addWidget(image, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.titlelLayout.addWidget(self.moreDescription, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.setLayout(self.titlelLayout)

    def on_continueButton_clicked(self):
        widget.addWidget(main3) 
        widget.setCurrentIndex(widget.currentIndex()+1)


class OPTIONS(QWidget):
    def __init__(self):
        super().__init__()
        self.outputBox = ()
        self.initUI()

    def initUI(self):
        ################################################################################
        # Layouts
        ################################################################################
        # Vertical layout
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        # Grid layout
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        # Title
        self.title = QLabel()
        self.title.setFont(QFont("Arial", 18))
        self.title.setText("Apps & Data")
        self.title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.title.setStyleSheet("""
        font-weight: Bold;
        """)

        # Question
        self.question = QLabel()
        self.question.setFont(QFont("Arial", 24))
        self.question.setAlignment(QtCore.Qt.AlignHCenter)
        self.question.setText("What are you planning to do?")
        self.question.setStyleSheet("""
        font-weight: Bold;
        """)

        # Description
        self.description = QLabel()
        self.description.setFont(QFont("Arial", 11))
        self.description.setAlignment(QtCore.Qt.AlignHCenter)
        self.description.setText(
            f"If you already have back up with {appName}\n"
            "You can use the restore option.")

        ################################################################################
        # Restore from
        ################################################################################
        imagePosX = 38
        imagePosy = 20
        self.restoreOption = QPushButton()
        pixmap = QPixmap(f'{src_migration_assistant_96px}')
        image = QLabel(self.restoreOption)
        image.setPixmap(pixmap)
        image.setFixedSize(pixmap.width(),pixmap.height())
        image.move(imagePosX, imagePosy)
        # pixmap = pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.restoreOption.setText(
            "\n\n\n\n\n\n\n\nRestore\n"
            f"from {appName}")
        self.restoreOption.setFont(QFont("Arial", 11))
        self.restoreOption.setCheckable(True)
        self.restoreOption.setAutoExclusive(True)
        self.restoreOption.setFixedSize(200, 200)
        self.restoreOption.setStyleSheet("""
            font: bold;
        """)
        self.restoreOption.clicked.connect(lambda *args: self.on_device_clicked("restore"))

        ################################################################################
        # Set up as new
        ################################################################################
        self.startAsNew = QPushButton()
        pixmap = QPixmap(f'{src_migration_assistant_96px}')
        image = QLabel(self.startAsNew)
        image.setPixmap(pixmap)
        image.setFixedSize(pixmap.width(),pixmap.height())
        image.move(imagePosX, imagePosy)
        # pixmap = pixmap.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
        self.startAsNew.setFont(QFont("Arial", 11))
        self.startAsNew.setText(
            "\n\n\n\n\n\n\nSet Up as New")
        self.startAsNew.setCheckable(True)
        self.startAsNew.setAutoExclusive(True)
        self.startAsNew.setFixedSize(200, 200)
        self.startAsNew.setStyleSheet("""
            font: bold;
        """)
        self.startAsNew.clicked.connect(lambda *args: self.on_device_clicked("new"))
       
        ################################################################################
        # Buttons
        ################################################################################
        # Back button
        self.backButton = QPushButton(self)
        self.backButton.setText("Back")
        self.backButton.setFont(QFont("Arial", 10))
        self.backButton.adjustSize()
        self.backButton.move(700, 555)
        self.backButton.clicked.connect(lambda *args: widget.setCurrentIndex(widget.currentIndex()-1))

        # Continue button
        self.continueButton = QPushButton(self)
        self.continueButton.setText("Continue")
        self.continueButton.setFont(QFont("Arial", 10))
        self.continueButton.adjustSize()
        self.continueButton.move(800, 555)
        self.continueButton.setEnabled(False)
        self.continueButton.clicked.connect(self.on_continue_clicked)

        ################################################################################
        # Add layout and widgets
        ################################################################################
        self.verticalLayout.addWidget(self.title, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.question, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.description, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        # Grid layout
        self.gridLayout.addWidget(self.restoreOption, 1, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.startAsNew, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout, 0)
        
        self.setLayout(self.verticalLayout)

    def on_device_clicked(self, output):
        # Add output to self.outputBox
        self.outputBox = output
        # Enable or disable continue button
        if self.restoreOption.isChecked() or self.startAsNew.isChecked():
            # Enable continue
            self.continueButton.setEnabled(True)

        else:
            # Clean self.ouputBox
            self.outputBox = ""
            # Disable continue
            self.continueButton.setEnabled(False)
    
    def on_continue_clicked(self):
        # If user clicked on restore from...
        if self.outputBox == "restore":
            widget.addWidget(main3) 
            widget.setCurrentIndex(widget.currentIndex()+1)

        else:
            exit()
            # widget.setCurrentWidget(main6)


class CHOOSEDEVICE(QWidget):
    def __init__(self):
        super().__init__()
        self.foundInMedia = None
        self.outputBox = ()
        self.captureDevices = []

        self.widgets()

    def widgets(self):
        ################################################################################
        # Layouts
        ################################################################################
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)

        # Title
        self.title = QLabel()
        self.title.setFont(QFont("Arial Bold", 28))
        self.title.setText("Transfer information to this pc")
        self.title.setAlignment(QtCore.Qt.AlignHCenter)
        self.title.setStyleSheet("""
        font-weight: Bold;
        """)

        # Description
        self.description = QLabel()
        self.description.setFont(QFont("Arial", 11))
        self.description.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.description.setText(f"Select a {appName} " 
            "backup disk to transfer it's information to this PC.")

        # More description
        self.moreDescription = QLabel()
        self.moreDescription.setFont(QFont("Arial", 11))
        self.moreDescription.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.moreDescription.setText(f"Make sure that your External device " 
            f"with a {appName}'s backup is connected to this PC.")

        ################################################################################
        # Devices Area
        ################################################################################
        self.devicesAreadWidget = QWidget()
        self.devicesAreadWidget.setFixedSize(700, 200)

        # Device layout
        self.devicesAreaLayout = QHBoxLayout(self.devicesAreadWidget)
        
        ################################################################################
        # Buttons
        ################################################################################
        # Back button
        self.backButton = QPushButton(self)
        self.backButton.setText("Back")
        self.backButton.setFont(QFont("Arial", 10))
        self.backButton.adjustSize()
        self.backButton.move(700, 555)
        self.backButton.clicked.connect(lambda *args: widget.setCurrentIndex(widget.currentIndex()-1))
        
        # Continue button
        self.continueButton = QPushButton(self)
        self.continueButton.setText("Continue")
        self.continueButton.setFont(QFont("Arial", 10))
        self.continueButton.adjustSize()
        self.continueButton.move(800, 555)
        self.continueButton.setEnabled(False)
        self.continueButton.clicked.connect(self.on_continue_clicked)
        
        self.check_connection()

    def check_connection(self):
        ################################################################################
        # Search external inside media
        ################################################################################
        try:
            if os.listdir(f'{media}/{userName}'):
                self.foundInMedia = True
                self.show_on_screen(media)

            else:
                for i in range(len(self.captureDevices)):
                    item = self.devicesAreaLayout.itemAt(i)
                    widget = item.widget()
                    widget.deleteLater()
                    i -= 1
                
        except FileNotFoundError:
            try:
                if os.listdir(f'{run}/{userName}'):
                    self.foundInMedia = False
                    self.show_on_screen(run)
                else:
                    for i in range(len(self.captureDevices)):
                        item = self.devicesAreaLayout.itemAt(i)
                        widget = item.widget()
                        widget.deleteLater()
                        i -= 1
                    
            except Exception:
                print("No device found...")
                pass

        self.show_on_screen(None)

    def show_on_screen(self, location):
        ################################################################################
        # Check source
        ################################################################################
        if self.foundInMedia:
            self.foundWhere = media
        else:
            self.foundWhere = run

        ################################################################################
        # Show available files
        ################################################################################
        try:
            for output in os.listdir(f"{location}/{userName}/"):
                # Only show disk the have baseFolderName inside
                if baseFolderName in os.listdir(f"{location}/{userName}/{output}/"):
                    if output not in self.captureDevices:   
                        # os.listdir(f"{location}/{userName}/{baseFolderName}")
                        # If device is in list, display to user just on time per device
                        self.captureDevices.append(output)

                        self.availableDevices = QPushButton(self.devicesAreadWidget)
                        self.availableDevices.setCheckable(True)
                        self.availableDevices.setAutoExclusive(True)
                        self.availableDevices.setFixedSize(180, 180)
                        self.availableDevices.setText(output)
                        self.availableDevices.setFont(QFont("Arial", 12))
                        self.availableDevices.adjustSize()
                        self.availableDevices.clicked.connect(
                            lambda *args, output=output: self.on_device_clicked(output))
                        self.availableDevices.setStyleSheet(
                            "QPushButton"
                            "{"
                                "text-align: bottom;"
                                "padding-bottom: 25px;"
                                "font: bold;"
                            "}")
                        
                        # Image
                        image = QLabel(self.availableDevices)
                        image.setFixedSize(96, 96)
                        image.move(58, 35)
                        image.setStyleSheet(
                            "QLabel"
                            "{"
                            f"background-image: url({src_restore_icon});"
                            "background-repeat: no-repeat;"
                            "background-color: transparent;"
                            "}")

                        self.devicesAreaLayout.addWidget(self.availableDevices)
            
                    # If x device is removed or unmounted, remove from screen
                    # for output in self.captureDevices:
                    #     if output not in os.listdir(f'{location}/{userName}'):
                    #         # Current output index
                    #         index = self.captureDevices.index(output)
                    #         # Remove from list
                    #         self.captureDevices.remove(output)             
                    #         # Delete from screen
                    #         item = self.devicesAreaLayout.itemAt(index)
                    #         widget = item.widget()
                    #         widget.deleteLater()
                    #         index -= 1

        except Exception:
            pass

        ################################################################################
        # Add layouts and widgets
        ################################################################################
        self.verticalLayout.addWidget(self.title)
        self.verticalLayout.addWidget(self.description)
        self.verticalLayout.addWidget(self.devicesAreadWidget, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.moreDescription, 2, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        self.setLayout(self.verticalLayout)

    def on_device_clicked(self, output):
        self.locationBackup = output
        self.continueButton.setEnabled(True)
        
        # If user has clicked on one device
        # if self.availableDevices.isChecked():
        #     self.outputBox = output
        #     # Enable use disk button
        #     self.continueButton.setEnabled(True)
        # else:
        #     # If deselected, empty self.outputBox
        #     self.outputBox = ""
        #     # Disable use disk button
        #     self.continueButton.setEnabled(False)

    def on_continue_clicked(self):
        # Enable continue button
        # self.continueButton.setEnabled(True)
        ################################################################################
        # Adapt external name is it has space in the name
        ################################################################################
        # if " " in self.outputBox:
        #     self.outputBox = str(self.outputBox.replace(" ", "\ ")).strip()

        ################################################################################
        # Get user's ox
        ################################################################################
        userPackageManager = os.popen(getUserPackageManager)
        userPackageManager = userPackageManager.read().strip().lower()

        ################################################################################
        # Update INI file
        ################################################################################
        config = configparser.ConfigParser()
        config.read(src_user_config)
        with open(src_user_config, 'w') as configfile:
            if "ubuntu" or "debian" in userPackageManager:
                # Save user's os name
                config.set(f'INFO', 'packageManager', 'deb')
            
            elif "fedora" or "opensuse" in userPackageManager:
                # Save user's os name
                config.set(f'INFO', 'packageManager', 'rpm')

            # Update INI file
            config.set(f'EXTERNAL', 'hd', f'{self.foundWhere}/{userName}/{self.locationBackup}')
            config.set('EXTERNAL', 'name', f'{self.locationBackup}')
            config.write(configfile)

        # Go to next window 
        widget.addWidget(main4) 
        widget.setCurrentIndex(widget.currentIndex()+1)

class PREBACKUP(QWidget):
    def __init__(self):
        super().__init__()
        self.optionsAddedList = []
        self.alreadySelectApps = False
        self.excludeAppList = []
        self.excludeAppsLoc = (f"{iniExternalLocation}/{baseFolderName}/"
                f"{applicationFolderName}/{src_exclude_applications}")
        
        # Delete .exclude-applications.txt first
        if os.path.exists(self.excludeAppsLoc):
            sub.run(f"rm -rf {self.excludeAppsLoc}", shell=True)
            
        self.read_ini_file()

    def read_ini_file(self):
        self.widgets()

    def widgets(self):
        ################################################################################
        # Layouts
        ################################################################################
        # Restore widget
        self.optionskWidget = QWidget()
        # self.optionskWidget.setFixedSize(340, 300)
        # self.optionskWidget.setStyleSheet("""
        # border: 1px solid blue;
        # """)

        self.scrollOptions = QScrollArea(self)
        self.scrollOptions.setFixedSize(370, 300)
        # self.scrollOptions.setFixedHeight(300)
        self.scrollOptions.setWidgetResizable(True)
        # self.scrollOptions.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollOptions.setWidget(self.optionskWidget)

        # Vertical base layout
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)

        # Vertical options layout
        self.verticalLayoutForOptions = QVBoxLayout(self.optionskWidget)
        self.verticalLayoutForOptions.setSpacing(5)
        self.verticalLayoutForOptions.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignTop)
        self.verticalLayoutForOptions.setContentsMargins(20, 20, 20, 20)

        # Title
        self.title = QLabel()
        self.title.setFont(QFont("Arial", 24))
        self.title.setText("Select the information to restore")
        self.title.setAlignment(QtCore.Qt.AlignHCenter)
        self.title.setStyleSheet("""
            font-weight: Bold;
        """)

        # Description
        self.description = QLabel()
        self.description.setFont(QFont("Arial", 11))
        self.description.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.description.setText("Please select the items you wish to transfer to this PC.")
        
        ################################################################################
        # System settings checkbox
        ################################################################################
        dummySystemSettingsSizeList = []
        try:
            # Icons size
            self.systemSettingsFolderSize = os.popen(f"du -hs {iconsMainFolder} 2>/dev/null")
            self.systemSettingsFolderSize = self.systemSettingsFolderSize.read().strip("\t")
            self.systemSettingsFolderSize = self.systemSettingsFolderSize.strip("\n")
            self.systemSettingsFolderSize = self.systemSettingsFolderSize.replace(f"{iconsMainFolder}", "")
            # Add to dummySystemSettingsSizeList
            dummySystemSettingsSizeList.append(self.systemSettingsFolderSize)

        except:
            pass
        
        try:    
            # Theme size
            self.systemSettingsFolderSize = os.popen(f"du -hs {themeFolderName} 2>/dev/null")
            self.systemSettingsFolderSize = self.systemSettingsFolderSize.read().strip("\t")
            self.systemSettingsFolderSize = self.systemSettingsFolderSize.strip("\n")
            self.systemSettingsFolderSize = self.systemSettingsFolderSize.replace(f"{themeFolderName}", "")
            # Add to dummySystemSettingsSizeList
            dummySystemSettingsSizeList.append(self.systemSettingsFolderSize)
        
        except:    
            pass

        try:
            # Cursor size
            self.systemSettingsFolderSize = os.popen(f"du -hs {cursorFolderName} 2>/dev/null")
            self.systemSettingsFolderSize = self.systemSettingsFolderSize.read().strip("\t")
            self.systemSettingsFolderSize = self.systemSettingsFolderSize.strip("\n")
            self.systemSettingsFolderSize = self.systemSettingsFolderSize.replace(f"{cursorFolderName}", "")
            # Add to dummySystemSettingsSizeList
            dummySystemSettingsSizeList.append(self.systemSettingsFolderSize)

            # Sum all values inside dummySystemSettingsSizeList
            self.systemSettingsFolderSize = sum(dummySystemSettingsSizeList)
        
        except:
            pass

        try:
            # System settings size information
            self.SystemSettingsSizeInformation = QLabel()
            # If M inside self.applicationsSizeInformation, add B = MB
            if "M" in self.systemSettingsFolderSize:
                self.SystemSettingsSizeInformation.setText(f"{self.systemSettingsFolderSize}B")
            else:
                self.SystemSettingsSizeInformation.setText(f"{self.systemSettingsFolderSize}")
            self.SystemSettingsSizeInformation.setFont(QFont("Arial", 10))
            self.SystemSettingsSizeInformation.adjustSize()
        

            self.systemSettingsCheckBox = QCheckBox()
            self.systemSettingsCheckBox.setText(" System Settings"
                f"               {self.systemSettingsFolderSize}")
            self.systemSettingsCheckBox.setFont(QFont("Arial", 11))
            self.systemSettingsCheckBox.adjustSize()
            self.systemSettingsCheckBox.setToolTip("This will restore: \n"
                "* Wallpaper\n"
                "* Theme\n"
                "   -- Icon\n"
                "   -- Cursor")

            self.systemSettingsCheckBox.setIcon(QIcon(f"{homeUser}/.local/share/{appNameClose}/src/icons/folder-development-symbolic.svg"))
            self.systemSettingsCheckBox.setIconSize(QtCore.QSize(22,22))
            self.systemSettingsCheckBox.clicked.connect(self.on_system_settings_clicked)
            
        except:
            pass

        ################################################################################
        # Application checkbox (Apps inside manual folder)
        ################################################################################
        try:
            # Get folder size
            if packageManager == "rpm":
                self.applicationSize = os.popen(f"du -hs {iniExternalLocation}/"
                    f"{baseFolderName}/{applicationFolderName}/{rpmFolderName}")
                self.applicationSize = self.applicationSize.read().strip("\t")
                self.applicationSize = self.applicationSize.strip("\n")
                self.applicationSize = self.applicationSize.replace(f"{iniExternalLocation}"
                    f"/{baseFolderName}/{applicationFolderName}/{rpmFolderName}", "").replace("\t", "")
            
            elif packageManager == "deb":
                self.applicationSize = os.popen(f"du -hs {iniExternalLocation}/"
                    f"{baseFolderName}/{applicationFolderName}/{debFolderName}")
                self.applicationSize = self.applicationSize.read().strip("\t")
                self.applicationSize = self.applicationSize.strip("\n")
                self.applicationSize = self.applicationSize.replace(f"{iniExternalLocation}"
                    f"/{baseFolderName}/{applicationFolderName}/{debFolderName}", "")
 
            ################################################################################
            # Application checkbox
            ################################################################################
            self.applicationPackagesCheckBox = QCheckBox()
            self.applicationPackagesCheckBox.setText(f" Applications "
                f"                              {self.applicationSize}")
            self.applicationPackagesCheckBox.setFont(QFont("Arial", 11))
            self.applicationPackagesCheckBox.adjustSize()
            self.applicationPackagesCheckBox.setIcon(QIcon(f"{homeUser}/.local/share/{appNameClose}/src/icons/find-here-symbolic.svg"))
            self.applicationPackagesCheckBox.setIconSize(QtCore.QSize(22,22))
            self.applicationPackagesCheckBox.setToolTip("This will reinstall: \n"
                "* All manual saved packages")
            self.applicationPackagesCheckBox.clicked.connect(self.on_application_clicked)

            # Application size information
            self.applicationSizeInformation = QLabel()
            # If M inside self.applicationsSizeInformation, add B = MB
            if "M" in self.applicationSize:
                self.applicationSizeInformation.setText(f"{self.applicationSize}B")
            else:
                self.applicationSizeInformation.setText(f"{self.applicationSize}")
            self.applicationSizeInformation.setFont(QFont("Arial", 10))
            self.applicationSizeInformation.adjustSize()
            self.applicationSizeInformation.setAlignment(QtCore.Qt.AlignRight)

            ################################################################################
            # Application checkbox (names)
            ################################################################################
            config = configparser.ConfigParser()
            config.read(src_user_config)
            with open(flatpakTxtFile, "r") as read_file:
                flatpaksToBeInstalled = len(read_file.readlines())

                self.flatpakCheckBox = QCheckBox()
                self.flatpakCheckBox.setText(f" Flatpak "
                    f"                                  {flatpaksToBeInstalled} Apps")
                self.flatpakCheckBox.setFont(QFont("Arial", 11))
                self.flatpakCheckBox.setIcon(QIcon(f"{homeUser}/.local/share/{appNameClose}/src/icons/find-here-symbolic.svg"))
                self.flatpakCheckBox.setIconSize(QtCore.QSize(22,22))
                self.flatpakCheckBox.setToolTip("This will reinstall: \n"
                    "* All flatpak applications")
                self.flatpakCheckBox.clicked.connect(self.on_flatpak_clicked)

        except:
            pass

        ################################################################################
        # Application checkbox (DATA)
        ################################################################################
        self.flatpakDataCheckBox = QCheckBox()
        self.flatpakDataCheckBox.setText(" Flatpak (Data)")
        self.flatpakDataCheckBox.setFont(QFont("Arial", 11))
        self.flatpakDataCheckBox.setIcon(QIcon(f"{homeUser}/.local/share/{appNameClose}/src/icons/folder-documents-symbolic.svg"))
        self.flatpakDataCheckBox.setIconSize(QtCore.QSize(22,22))
        self.flatpakDataCheckBox.setEnabled(False)
        self.flatpakDataCheckBox.clicked.connect(self.on_applications_data_clicked)

        try:
            # Get folder size
            self.flatpakDataSize = os.popen(f"du -hs {iniExternalLocation}/{baseFolderName}/{applicationFolderName}")
            self.flatpakDataSize = self.flatpakDataSize.read().strip("\t").strip("\n").replace(f"{iniExternalLocation}/{baseFolderName}/{applicationFolderName}", "").replace("\t", "")
        
 
            # Application size information
            self.applicationSizeInformation = QLabel()
            # If M inside self.applicationsSizeInformation, add B = MB
            if "M" in self.flatpakDataSize:
                self.applicationSizeInformation.setText(f"{self.flatpakDataSize}B")
            else:
                self.applicationSizeInformation.setText(f"{self.flatpakDataSize}")
            self.applicationSizeInformation.setFont(QFont("Arial", 10))
            self.applicationSizeInformation.adjustSize()
        
        except:
            pass

        ################################################################################
        # Files & Folders checkbox
        ################################################################################
        try:
            # Get available dates inside TMB
            dateFolders = []
            for output in os.listdir(f"{iniExternalLocation}/{baseFolderName}/"
                f"{backupFolderName}"):
                if not "." in output:
                    dateFolders.append(output)
                    dateFolders.sort(reverse=True, key=lambda date: datetime.strptime(date, "%d-%m-%y"))

            # Get time inside date
            timeFolder = []
            for output in os.listdir(f"{iniExternalLocation}/{baseFolderName}/"
                f"{backupFolderName}/{dateFolders[0]}/"):
                timeFolder.append(output)
                timeFolder.sort(reverse=True)

            # Get folder size
            self.fileAndFoldersFolderSize = os.popen(f"du -hs {iniExternalLocation}/"
                f"{baseFolderName}/{backupFolderName}/{dateFolders[0]}/{timeFolder[0]}")
            self.fileAndFoldersFolderSize = self.fileAndFoldersFolderSize.read().strip("\t")
            self.fileAndFoldersFolderSize = self.fileAndFoldersFolderSize.strip("\n")
            self.fileAndFoldersFolderSize = self.fileAndFoldersFolderSize.replace(f"{iniExternalLocation}"
                f"/{baseFolderName}/{backupFolderName}/{dateFolders[0]}/{timeFolder[0]}", "")

            # Clean terminal
            # sub.Popen("clear", shell=True)

            # Files and Folders checkbox        
            self.fileAndFoldersCheckBox = QCheckBox()
            self.fileAndFoldersCheckBox.setText(" Files and Folders"
                f"                        {self.fileAndFoldersFolderSize}")
            self.fileAndFoldersCheckBox.setFont(QFont("Arial", 11))
            self.fileAndFoldersCheckBox.setIcon(QIcon(f"{homeUser}/.local/share/{appNameClose}/src/icons/folder-documents-symbolic.svg"))
            self.fileAndFoldersCheckBox.setIconSize(QtCore.QSize(22,22))
            self.fileAndFoldersCheckBox.setToolTip("This will restore: \n"
                "* All recents back up files and folders")
            self.fileAndFoldersCheckBox.clicked.connect(self.on_files_and_folders_clicked)

            ################################################################################
            # User information
            ################################################################################
            self.userSizeInformation = QLabel()
            self.userSizeInformation.setFont(QFont("Arial", 10))
            self.userSizeInformation.adjustSize()
            self.userSizeInformation.setAlignment(QtCore.Qt.AlignRight)

            ################################################################################
            # Buttons
            ################################################################################
            # Back button
            self.backButton = QPushButton(self)
            self.backButton.setText("Back")
            self.backButton.setFont(QFont("Arial", 10))
            self.backButton.adjustSize()
            self.backButton.move(700, 555)
            self.backButton.clicked.connect(lambda *args: widget.setCurrentIndex(widget.currentIndex()-1))

            # Continue button
            self.continueButton = QPushButton(self)
            self.continueButton.setText("Continue")
            self.continueButton.setFont(QFont("Arial", 10))
            self.continueButton.adjustSize()
            self.continueButton.move(800, 555)
            if not self.optionsAddedList:
                self.continueButton.setEnabled(False)
            self.continueButton.clicked.connect(self.on_continue_button_clicked)
            # self.continueButton.clicked.connect(lambda *args: widget.setCurrentIndex(widget.currentIndex()+1))

            ################################################################################
            # Add layouts and widgets
            ################################################################################
            # TODO
            self.baseAppsWidget = QWidget()
            # self.baseAppsWidget.setStyleSheet("""
            # border: 1px solid red;
            # """)

            self.scrollShowMoreApps = QScrollArea()
            self.scrollShowMoreApps.setFixedHeight(0)
            self.scrollShowMoreApps.setWidgetResizable(True)
            # self.scrollShowMoreApps.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
            self.scrollShowMoreApps.setWidget(self.baseAppsWidget)
            ################################################################################

            self.selectAppsLayout = QVBoxLayout(self.baseAppsWidget)
            self.selectAppsLayout.setSpacing(5)

            self.verticalLayout.addWidget(self.title)
            self.verticalLayout.addWidget(self.description)

            self.verticalLayout.addStretch()
            self.verticalLayout.addWidget(self.scrollOptions, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.verticalLayoutForOptions.addWidget(self.applicationPackagesCheckBox)
            
            self.verticalLayoutForOptions.addWidget(self.scrollShowMoreApps)
            self.verticalLayoutForOptions.addWidget(self.flatpakCheckBox)
            self.verticalLayoutForOptions.addWidget(self.flatpakDataCheckBox)
            self.verticalLayoutForOptions.addWidget(self.fileAndFoldersCheckBox)
            self.verticalLayoutForOptions.addWidget(self.systemSettingsCheckBox)
            self.verticalLayout.addStretch()

            self.setLayout(self.verticalLayout)

        except:
            pass

        self.find_flatpak_txt()

    def find_flatpak_txt(self):
        ################################################################################
        # Something inside?
        ################################################################################
        try:
            # Look for flatpakTxt inside external device
            config = configparser.ConfigParser()
            config.read(src_user_config)
            with open(f"{flatpakTxtFile}", 'r') as output:
                output = output.read()
                # If is  not empty, enable these boxes
                if output != "":
                    self.flatpakCheckBox.setEnabled(True)

                else:
                    # Disable these boxes
                    self.flatpakCheckBox.setEnabled(False)  

        except FileNotFoundError:
            pass

        self.find_applications()

    def find_applications(self):
        ################################################################################
        # Check inside backup flatpak data (var)
        # There is not need to check (share) inside External
        # If Var is empty, just pass this options
        ################################################################################
        try:
            dummyList = []
            if packageManager == "rpm":
                for outputRPM in os.listdir(f"{rpmMainFolder}/"):
                    dummyList.append(outputRPM)

            elif packageManager == "deb":
                for outputDeb in os.listdir(f"{debMainFolder}/"):
                    dummyList.append(outputDeb)
            
            # If has something inside
            if dummyList:
                self.applicationPackagesCheckBox.setEnabled(True)
            
            else:
                self.applicationPackagesCheckBox.setEnabled(False)  

            # Empty list
            dummyList.clear()
            
        except:
            pass

        self.find_applications_data()

    def find_applications_data(self):
        ################################################################################
        # Check inside backup flatpak data (var)
        # There is not need to check (share) inside External
        # If Var is empty, just pass this options
        ################################################################################
        try:
            dummyList = []
            for output in os.listdir(f"{applicationVarFolder}/"):
                dummyList.append(output)

            if dummyList:
                self.flatpakDataCheckBox.setEnabled(True)

            else:
                self.flatpakDataCheckBox.setEnabled(False)  
            
            # Empty list
            dummyList.clear()

        except:
            pass

        self.find_files_and_folders()

    def find_files_and_folders(self):
        ################################################################################
        try:
            dummyList = []
            # Check inside backup folder 
            for output in os.listdir(f"{createBackupFolder}/"):
                dummyList.append(output)

            if dummyList:
                self.fileAndFoldersCheckBox.setEnabled(True)

            else:
                self.fileAndFoldersCheckBox.setEnabled(False)  

            # Clean list
            dummyList.clear()

        except:
            pass

        self.enable_system_settings()

    def enable_system_settings(self):
        dummyList = []
        try:
            # # Find user's DE type
            # userPackageManager = os.popen(getUserDE)
            # userPackageManager = userPackageManager.read().strip().lower()
            # Check if a wallpaper has been backup
            for output in os.listdir(f"{wallpaperMainFolder}/"):
                dummyList.append(output)

            # Check if icon has been backup
            for output in os.listdir(f"{iconsMainFolder}/"):
                dummyList.append(output)

            # Check if theme has been backup
            for output in os.listdir(f"{themeMainFolder}/"):
                dummyList.append(output)
            
            # Check if cursor has been backup
            for output in os.listdir(f"{cursorMainFolder}/"):
                dummyList.append(output)

            # Check if user DE is in the supported list
            if dummyList:
                # Enable systemSettingsCheckBox
                self.systemSettingsCheckBox.setEnabled(True)
                
            else:
                self.systemSettingsCheckBox.setEnabled(False)  

            # Empty list
            dummyList.clear()

        except:
            pass

    def on_application_clicked(self):
        # Open applications checkboxes
        if not self.alreadySelectApps:
            self.scrollShowMoreApps.setFixedHeight(120)
            self.alreadySelectApps = True
        else:
            self.scrollShowMoreApps.setFixedHeight(0)
            self.alreadySelectApps = False

        # Restore packages applications
        config = configparser.ConfigParser()
        config.read(src_user_config)
        with open(src_user_config, 'w') as configfile:
            if self.applicationPackagesCheckBox.isChecked():
                config.set('RESTORE', 'applications_packages', 'true')

                # Activate data checkbox
                self.applicationPackagesCheckBox.setChecked(True)
                # Enable continue button
                self.continueButton.setEnabled(True)
                # Add names to list
                self.optionsAddedList.append("packages")

                # Add checboxes dinamically
                self.dummyCheckBoxList = []
                for output in os.listdir(f"{iniExternalLocation}/{baseFolderName}/"
                    f"{applicationFolderName}/{debFolderName}/"):
                    dummyCheckBox = QCheckBox()
                    dummyCheckBox.setText((output.split("_")[0]).capitalize())
                    dummyCheckBox.setChecked(True)
                    # self.dummyCheckBoxList.append(output)
                    dummyCheckBox.clicked.connect(lambda *args, exclude=output: self.exclude_apps(exclude))

                    self.selectAppsLayout.addWidget(dummyCheckBox)

            else:
                config.set('RESTORE', 'applications_packages', 'false')

                # Disable names
                if "packages" in self.optionsAddedList:
                    self.optionsAddedList.remove("packages")
                
                # Clean exclude lsit
                self.excludeAppList.clear()

                # Remove applications checkboxes
                for i in range(self.selectAppsLayout.count()):
                    item = self.selectAppsLayout.itemAt(i)
                    widget = item.widget()
                    widget.deleteLater()
                    i -= 1

            # Write to INI file
            config.write(configfile)

            # Allow continue?
            self.allow_to_continue()

    def on_flatpak_clicked(self):
        ################################################################################
        # Write to INI file
        ################################################################################
        config = configparser.ConfigParser()
        config.read(src_user_config)
        with open(src_user_config, 'w') as configfile:
            if self.flatpakCheckBox.isChecked():
                config.set('RESTORE', 'applications_flatpak_names', 'true')
                
                # Activate flatpak checkbox
                self.flatpakCheckBox.setChecked(True)
                # Enable continue button
                self.continueButton.setEnabled(True)
                # Add names to list if not already there
                if "flatpak" not in self.optionsAddedList:
                    self.optionsAddedList.append("flatpak")

            else:
                config.set('RESTORE', 'applications_flatpak_names', 'false')
                # Disable data checkbox
                self.flatpakCheckBox.setChecked(False)
                # Disable flatpak if in list
                if "flatpak" in self.optionsAddedList:
                    self.optionsAddedList.remove("flatpak")

            # Write to INI file
            config.write(configfile)
            
            # Allow continue?
            self.allow_to_continue()

    def on_applications_data_clicked(self):
        # If user allow app to back up data, auto activate
        # backup flatpaks name too.
        config = configparser.ConfigParser()
        config.read(src_user_config)
        with open(src_user_config, 'w') as configfile:
            if self.flatpakDataCheckBox.isChecked():
                config.set('RESTORE', 'applications_flatpak_names', 'true')
                config.set('RESTORE', 'applications_data', 'true')

                # Activate data checkbox
                self.flatpakDataCheckBox.setChecked(True)
                # Enable continue button
                self.continueButton.setEnabled(True)
                # Add data to list if not already there
                if "data" not in self.optionsAddedList:
                    self.optionsAddedList.append("data")
                # Auto enable flatpak to list
                self.optionsAddedList.append("flatpak")
              
            else:
                config.set('RESTORE', 'applications_data', 'false')
                # Disable data checkbox
                self.flatpakDataCheckBox.setChecked(False)
                # Disable data if in list
                if "data" in self.optionsAddedList:
                    self.optionsAddedList.remove("data")

            # Write to INI file
            config.write(configfile)

            # Allow continue?
            self.allow_to_continue()
  
    def on_files_and_folders_clicked(self):
        ################################################################################
        # Write to INI file
        ################################################################################
        config = configparser.ConfigParser()
        config.read(src_user_config)
        with open(src_user_config, 'w') as configfile:
            if self.fileAndFoldersCheckBox.isChecked():
                config.set('RESTORE', 'files_and_folders', 'true')

                # Enable continue button
                self.continueButton.setEnabled(True)
                # Add files to list
                self.optionsAddedList.append("files")
              
            else:
                config.set('RESTORE', 'files_and_folders', 'false')

                # Disable continue button
                self.continueButton.setEnabled(False)
                if "files" in self.optionsAddedList:
                    self.optionsAddedList.remove("files")

            # Write to INI file
            config.write(configfile)

            # Allow continue?
            self.allow_to_continue()
  
    def on_system_settings_clicked(self):
        ################################################################################
        # Write to INI file
        ################################################################################
        config = configparser.ConfigParser()
        config.read(src_user_config)
        with open(src_user_config, 'w') as configfile:
            if self.systemSettingsCheckBox.isChecked():
                config.set('RESTORE', 'system_settings', 'true')

                # Enable continue button
                self.continueButton.setEnabled(True)
                # Add system_settings to list
                self.optionsAddedList.append("system_settings")
              
            else:
                config.set('RESTORE', 'system_settings', 'false')

                # Disable continue button
                self.continueButton.setEnabled(False)
                if "system_settings" in self.optionsAddedList:
                    self.optionsAddedList.remove("system_settings")

            # Write to INI file
            config.write(configfile)
            
        # Allow continue?
        self.allow_to_continue()

    def allow_to_continue(self):
        # If self.optionsAddedList is not empty, allow it
        if len(self.optionsAddedList) > 0:
            # Enable continue button
            self.continueButton.setEnabled(True)
        else:
            # Disable continue button
            self.continueButton.setEnabled(False)

    def on_continue_button_clicked(self):
        # Write applications exclude list .exclude-application.txt
        # Create a .exclude-applications
        if not os.path.exists(self.excludeAppsLoc):
            sub.run(f"{createCMDFile} {self.excludeAppsLoc}", shell=True)

        else:
            # Delete before continue
            sub.run(f"rm -rf {self.excludeAppsLoc}", shell=True)
            # Create again
            sub.run(f"{createCMDFile} {self.excludeAppsLoc}", shell=True)

        if self.excludeAppList:
            # Get user installed flatpaks
            config = configparser.ConfigParser()
            config.read(src_user_config)
            with open(self.excludeAppsLoc, 'w') as configfile:
                for apps in self.excludeAppList:  
                    configfile.write(f"{apps}\n")
        
        # Change current index
        widget.addWidget(main5)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # STATIC FUNC
    def select_apps_clicked(self):
        if not self.alreadySelectApps:
            self.scrollShowMoreApps.setFixedHeight(120)
            self.alreadySelectApps = True

        else:
            self.scrollShowMoreApps.setFixedHeight(0)
            self.alreadySelectApps = False

    def exclude_apps(self, exclude):
        # Only add to exclude, if it not already there
        if exclude not in self.excludeAppList:
            self.excludeAppList.append(exclude)
        else:
            self.excludeAppList.remove(exclude)

        print("Exclude:", self.excludeAppList)   

class BACKUPSCREEN(QWidget):
    def __init__(self):
        super().__init__()
        self.outputBox = ()

        self.widgets()

    def widgets(self):
        ################################################################################
        # Layouts
        ################################################################################
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)

        # Restore area widget
        self.devicesAreadWidget = QWidget()
        self.devicesAreadWidget.setFixedSize(400, 200)

        # Horizontal layout
        self.imagesLayout = QHBoxLayout(self.devicesAreadWidget)
        self.imagesLayout.setSpacing(10)

        ################################################################################
        # Texts
        ################################################################################
        # Title
        self.title = QLabel()
        self.title.setFont(QFont("Arial", 28))
        self.title.setText("Transferring Your information")
        self.title.setAlignment(QtCore.Qt.AlignHCenter)
        self.title.setStyleSheet("""
        font-weight: Bold;
        """)

        # Description
        self.description = QLabel()
        self.description.setFont(QFont("Arial", 11))
        self.description.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.description.setText(f"Backup from {appName} " 
            "will been transferred to this PC.")

        # More description
        self.moreDescription = QLabel()
        self.moreDescription.setFont(QFont("Arial", 6))
        self.moreDescription.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.moreDescription.setText('<h1>Click on "Restore" to begin.</h1>') 
        
        # Automatically reboot
        self.autoReboot = QCheckBox()
        self.autoReboot.setFont(QFont("Arial", 10))
        self.autoReboot.setText('Automatically reboot after restoring is done.') 
        self.autoReboot.clicked.connect(self.auto_reboot_clicked)

        # Restoring description
        self.whileRestoringDescription = QLabel()
        self.whileRestoringDescription.setFont(QFont("Arial", 11))
        self.whileRestoringDescription.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        ################################################################################
        # Images
        ################################################################################
        # Image 1       
        image = QLabel()
        image.setFixedSize(68, 68)
        image.setStyleSheet(
            "QLabel"
            "{"
            f"background-image: url({homeUser}/.local/share/{appNameClose}/src/icons/restore_64px.svg);"
            "background-repeat: no-repeat;"
            "background-color: transparent;"
            "background-position: center;"
            "}")

        # Image 2       
        image2 = QLabel()
        image2.setFixedSize(96, 96)
        image2.setStyleSheet(
            "QLabel"
            "{"
            f"background-image: url({homeUser}/.local/share/{appNameClose}/src/icons/arrow.png);"
            "background-repeat: no-repeat;"
            "background-color: transparent;"
            "background-position: center;"
            "}")

        # Image 3       
        image3 = QLabel()
        image3.setFixedSize(96, 96)
        image3.setStyleSheet(
            "QLabel"
            "{"
            f"background-image: url({homeUser}/.local/share/{appNameClose}/src/icons/applications-system.svg);"
            "background-repeat: no-repeat;"
            "background-color: transparent;"
            "background-position: center;"
            "}")

        ################################################################################
        # External device name
        ################################################################################
        widgetDeviceName = QWidget(self)
        widgetDeviceName.setFixedSize(185, 40)
        widgetDeviceName.move(232, 265)

        # Widget device layout
        widgetDeviceLayout = QHBoxLayout(widgetDeviceName)

        # External device name
        self.externalDeviceName = QLabel()
        self.externalDeviceName.setFont(QFont("Arial", 14))
        try:
            config = configparser.ConfigParser()
            config.read(src_user_config)
            # Add userName 
            self.externalDeviceName.setText(iniExternalName)
            self.externalDeviceName.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.externalDeviceName.adjustSize()
        
        except:
            pass

        ################################################################################
        # This pc label
        ################################################################################
        widgetThisPCName = QWidget(self)
        widgetThisPCName.setFixedSize(170, 40)
        widgetThisPCName.move(488, 265)

        # This pc name layout
        widgetLayout = QHBoxLayout(widgetThisPCName)
        self.thisPCName = QLabel()
        self.thisPCName.setFont(QFont("Arial", 14))
        self.thisPCName.setText(f"{(userName).capitalize()}")
        self.thisPCName.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
        self.thisPCName.adjustSize()

        ################################################################################
        # Buttons
        ################################################################################
        # Back button
        self.backButton = QPushButton(self)
        self.backButton.setText("Back")
        self.backButton.setFont(QFont("Arial", 10))
        self.backButton.adjustSize()
        self.backButton.move(700, 555)
        self.backButton.clicked.connect(lambda *args: widget.setCurrentIndex(widget.currentIndex()-1))

        # Continue button
        self.startRestoreButton = QPushButton(self)
        self.startRestoreButton.setText("Restore")
        self.startRestoreButton.setFont(QFont("Arial", 10))
        self.startRestoreButton.adjustSize()
        self.startRestoreButton.move(800, 555)
        self.startRestoreButton.setEnabled(True)
        self.startRestoreButton.clicked.connect(self.change_screen)

        ################################################################################
        # Add layouts and widgets
        ################################################################################
        self.verticalLayout.addWidget(self.title)
        self.verticalLayout.addWidget(self.description)
        self.verticalLayout.addWidget(self.devicesAreadWidget, 1, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.moreDescription, 2, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.whileRestoringDescription, 2, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.autoReboot, 2, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        # Widget device layouts
        self.imagesLayout.addWidget(image, 1, QtCore.Qt.AlignHCenter)
        self.imagesLayout.addWidget(image2, 0, QtCore.Qt.AlignHCenter)
        self.imagesLayout.addWidget(image3, 1, QtCore.Qt.AlignHCenter)
        widgetDeviceLayout.addWidget(self.externalDeviceName)
        widgetLayout.addWidget(self.thisPCName)

        # Add userName self.set
        self.setLayout(self.verticalLayout)

        self.read_ini_file()

    def read_ini_file(self):
        try:
            self.externalDeviceName.setText(iniExternalName)

            ################################################################################
            # Update widgets
            ################################################################################
            # if restoring is running
            if iniIsRestoreRunning == "true":
                # Show restoring description
                self.whileRestoringDescription.setText(f'Transferring '
                    f"{iniCurrentBackupInfo} to the user {userName}...") 
                # Hide more description
                self.moreDescription.hide()
                # Show restoring description
                self.whileRestoringDescription.show()

        except:
            pass

    def change_screen(self):
        config = configparser.ConfigParser()
        config.read(src_user_config)
        with open(src_user_config, 'w', encoding='utf8') as configfile:  
            config.set('RESTORE', 'is_restore_running', 'true')
            config.write(configfile)

        # Change screen
        widget.addWidget(main6)
        # Call restore python
        sub.Popen(f"python3 {src_restore_cmd}", shell=True)
        widget.showFullScreen()
        widget.setCurrentIndex(widget.currentIndex()+1)

    def auto_reboot_clicked(self):
        # Automatically reboot after done
        config = configparser.ConfigParser()
        config.read(src_user_config)
        with open(src_user_config, 'w', encoding='utf8') as configfile:  
            if self.autoReboot.isChecked():
                config.set('INFO', 'auto_reboot', 'true')
            else:
                config.set('INFO', 'auto_reboot', 'false')

            config.write(configfile)

        
class START_RESTORING(QWidget):
    def __init__(self):
        super().__init__()

        self.widgets()
            
    def widgets(self):
        # Title layout
        self.titlelLayout = QVBoxLayout()
        self.titlelLayout.setSpacing(20)
        self.titlelLayout.setContentsMargins(20, 20, 20, 20)
        
        # Welcome
        self.title = QLabel()
        self.title.setFont(QFont("Arial", 28))
        self.title.setText("This may take a few minutes...")
        self.title.setAlignment(QtCore.Qt.AlignHCenter)
        self.title.setStyleSheet("""
        font-weight: Bold;
        """)

        # More description
        self.moreDescription = QLabel()
        self.moreDescription.setFont(QFont("Arial", 11))
        self.moreDescription.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.moreDescription.setText(
            "Don't turn off your PC.\n"
            "This window will automatically close after restoring is done.") 
        self.moreDescription.setStyleSheet("""
        color: gray;
        """)

        ###########################################################################
        # Add layouts and widgets
        ################################################################################
        self.titlelLayout.addStretch()
        self.titlelLayout.addWidget(self.title, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.titlelLayout.addWidget(self.moreDescription, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.titlelLayout.addStretch()
        self.setLayout(self.titlelLayout)

        # Update
        timer.timeout.connect(self.read_ini_file)
        timer.start(1000) # Update every x seconds
        self.read_ini_file()

    def read_ini_file(self):
        config = configparser.ConfigParser()
        config.read(src_user_config)
        self.isRestoreRunning = config['RESTORE']['is_restore_running']

        if self.isRestoreRunning == "false":
            ###############################################################################
            # Update INI file
            ###############################################################################
            config = configparser.ConfigParser()
            config.read(src_user_config)
            with open(src_user_config, 'w') as configfile:
                # Set auto rebooting to false
                config.set('RESTORE', 'is_restore_running', 'none')
                config.write(configfile)

            exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    main = WELCOMESCREEN()
    main2 = OPTIONS()
    main3 = CHOOSEDEVICE()
    main4 = PREBACKUP()
    main5 = BACKUPSCREEN()
    main6 = START_RESTORING()

    widget.addWidget(main)   
    widget.setCurrentWidget(main)   

    # Window settings
    widget.setWindowTitle("Migration Assistant")
    widget.setWindowIcon(QIcon(src_migration_assistant_96px)) 
    widget.setFixedSize(windowXSize, windowYSize)
    widget.show()

    app.exit(app.exec())
