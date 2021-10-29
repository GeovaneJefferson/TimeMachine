import configparser
import sys
import os

from pathlib import Path
from PyQt5.uic import loadUi
from PyQt5.QtCore import QSize    
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

home_user = str(Path.home())
get_home_folders = os.listdir(home_user)
min_fix = ["0","1","2","3","4","5","6","7","8","9"]

src_user_config = "src/user.ini"
src_ui_options = "src/options.ui"
src_restore_icon = "src/icons/restore_48.png"

#dst_user_config = home_user+"/.local/share/timemachine/src/user.ini"
#dst_ui_options = "home_user+"/.local/share/timemachine/src/options.ui"
#dst_restore_icon = "home_user+"/.local/share/timemachine/src/icons/restore_48.png"

#CONFIGPARSER
config = configparser.ConfigParser()
config.read(src_user_config)

class Options(QMainWindow):
    def __init__(self):
        super(Options, self).__init__()
        loadUi(src_ui_options,self)
        self.label_hours.valueChanged.connect(self.label_hours_changed)
        self.label_minutes.valueChanged.connect(self.label_minutes_changed)
        
        #SCHEDULE OPTIONS
        #HOURS        
        hrs = (config.get('SCHEDULE', 'hours'))
        hrs = int(hrs)
        self.label_hours.setValue(hrs)

        #MINUTES        
        min = (config.get('SCHEDULE', 'minutes'))
        min = int(min)
        self.label_minutes.setValue(min)   

        #CHECK FOR:
        sun = config['SCHEDULE']['sun']
        if sun == "true":
            self.check_sun.setChecked(True) 
        mon = config['SCHEDULE']['mon']
        if mon == "true":
            self.check_mon.setChecked(True) 
        tue = config['SCHEDULE']['tue']
        if tue == "true":
            self.check_tue.setChecked(True) 
        wed = config['SCHEDULE']['wed']
        if wed == "true":
            self.check_wed.setChecked(True) 
        thu = config['SCHEDULE']['thu']
        if thu == "true":
            self.check_thu.setChecked(True) 
        fri = config['SCHEDULE']['fri']
        if fri == "true":
            self.check_fri.setChecked(True) 
        sat = config['SCHEDULE']['sat']
        if sat == "true":
            self.check_sat.setChecked(True) 

        #CALL UPDATE()
        self.update()

    def update(self):
        #ADD USER FOLDERS
        vertical = 10
        for self.folders in get_home_folders:
            if not self.folders.startswith('.'):
                self.folders_checkbox = QCheckBox(self.folders, self.folders_frame)
                self.folders_checkbox.setFixedSize(310, 22)
                self.folders_checkbox.move(10 ,vertical)
                vertical = vertical + 25
                text = self.folders_checkbox.text()
                self.folders_checkbox.show()
                if self.folders_checkbox.isChecked():
                    self.folders_checkbox.clicked.connect(lambda ch, text=text : self.on_folders_checked(text))
                    
                # with open(src_user_config, 'w') as configfile:
                #     self.folders_checkbox = str(self.folders_checkbox).replace(" ","_")
                #     config.set('FOLDER', self.folders, 'false')
                #     config.write(configfile)

        with open(src_user_config, 'r') as configfile:
            for key in config['FOLDER']:  
                print(key)

    def on_folders_checked(self,result):
        print(result)
        # if self.folders_checkbox == "true":
        #     print("ACTIVATE")
        with open(src_user_config, 'w') as configfile:
            config.set('FOLDER', result, 'true')
            config.write(configfile)

        # else:
        #     print("DEACTIVATE")
            # with open(src_user_config, 'w') as configfile:
            #     config.set('FOLDER', self.folders_checkbox, 'false')
            #     config.write(configfile)
        

        # else:
        # #----Remove (.desktop) if user wants to----#
        #     cfgfile = open(src_user_config, 'w')
        #     config.set('FOLDER', 'videos', 'false')
        #     config.write(cfgfile)
        #     cfgfile.close() 
        
    def on_check_sun_clicked(self):
        if self.check_sun.isChecked():
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'sun', 'true')
                config.write(configfile)  
                print("Sun")
        else:
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'sun', 'false')
                config.write(configfile) 

    def on_check_mon_clicked(self):
        if self.check_mon.isChecked():
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'mon', 'true')
                config.write(configfile) 
                print("Mon")
        else:
        #----Remove (.desktop) if user wants to----#
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'mon', 'false')
                config.write(configfile) 

    def on_check_tue_clicked(self):
        if self.check_tue.isChecked():
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'tue', 'true')
                config.write(configfile) 
                print("Tue")
        else:
        #----Remove (.desktop) if user wants to----#
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'tue', 'false')
                config.write(configfile) 

    def on_check_wed_clicked(self):
        if self.check_wed.isChecked():
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'wed', 'true')
                config.write(configfile) 
                print("Wed")
        else:
        #----Remove (.desktop) if user wants to----#
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'wed', 'false')
                config.write(configfile) 

    def on_check_thu_clicked(self):
        if self.check_thu.isChecked():
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'thu', 'true')
                config.write(configfile) 
                print("Thu")
        else:
        #----Remove (.desktop) if user wants to----#
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'thu', 'false')
                config.write(configfile) 

    def on_check_fri_clicked(self):
        if self.check_fri.isChecked():
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'fri', 'true')
                config.write(configfile) 
                print("Fri")
        else:
        #----Remove (.desktop) if user wants to----#
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'fri', 'false')
                config.write(configfile) 

    def on_check_sat_clicked(self):
        if self.check_sat.isChecked():
             with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'sat', 'true')
                config.write(configfile) 
                print("Sat")
        else:
        #----Remove (.desktop) if user wants to----#
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'sat', 'false')
                config.write(configfile) 

    def label_hours_changed(self):
        hours = self.label_hours.value()
        hours = str(hours)
        print((str(hours)))

        with open(src_user_config, 'w') as configfile:
            config.set('SCHEDULE', 'hours', hours)
            config.write(configfile) 

        if hours in min_fix:
            with open(src_user_config, 'w') as configfile:
                config.set('SCHEDULE', 'hours', '0'+hours)
                config.write(configfile) 

    def label_minutes_changed(self):
        minutes = self.label_minutes.value()
        minutes = str(minutes)
        print((str(minutes)))

        with open(src_user_config, 'w') as configfile:
            config.set('SCHEDULE', 'minutes', minutes)
            config.write(configfile) 

        if minutes in min_fix:
            with open(src_user_config, 'w') as configfile:
                    config.set('SCHEDULE', 'minutes', '0'+minutes)
                    config.write(configfile) 

# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
appIcon = QIcon(src_restore_icon)
widget.setWindowIcon(appIcon)
main_window = Options()
widget.addWidget(main_window)
widget.setFixedHeight(550)
widget.setFixedWidth(800)
widget.setWindowTitle("Options")
widget.show()
sys.exit(app.exec_())


