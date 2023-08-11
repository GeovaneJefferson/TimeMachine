from setup import *
from prepare_backup import *

# Wallpaper
from get_current_users_wallpaper import user_wallpaper

# Update
from read_ini_file import UPDATEINIFILE

# Get users DE
from get_users_de import get_user_de

# Get backup folder
from get_folders_to_be_backup import get_folders

# Get flatpaks folders size
from get_flatpaks_folders_size import flatpak_var_list, flatpak_local_list


# Handle signal
signal.signal(signal.SIGINT, signal_exit)
signal.signal(signal.SIGTERM, signal_exit)


class BACKUP:
    async def backup_wallpaper(self):
        # GNOME/KDE
        # Send notification status
        notification_message("Backing up: Wallpaper...")

        # Replace wallpaper inside the folder, only allow 1
        if os.listdir(f"{MAIN_INI_FILE.wallpaper_main_folder()}"):
            # Delete all wallpapers inside wallpaper folder
            for wallpaper in os.listdir(f"{MAIN_INI_FILE.get_database_value('EXTERNAL', 'name')}/{BASE_FOLDER_NAME}/{WALLPAPER_FOLDER_NAME}/"):
                sub.run(f"rm -rf {MAIN_INI_FILE.get_database_value('EXTERNAL', 'name')}/{BASE_FOLDER_NAME}/{WALLPAPER_FOLDER_NAME}/{wallpaper}", shell=True)

        # Backup current wallpaper
        sub.run(f"{COPY_CP_CMD} {user_wallpaper()} {MAIN_INI_FILE.wallpaper_main_folder()}/", shell=True)
        
    async def backup_home(self):
        # Backup Home
        # Send notification status
        notification_message("Backing up: Home folders...")

        # Backup Home folder
        # Backup all (user.ini true folders)
        for folder in get_folders():
            sub.run(f"{COPY_CP_CMD} {HOME_USER}/{folder} {MAIN_INI_FILE.time_folder_format()}", shell=True)

    async def backup_home_hidden_files(self):
        # For GNOME
        if get_user_de() == 'gnome':
            # Send notification status
            notification_message("Backing up: .local/share/ ...")

            # Backup .local/share/ selected folders for GNOME
            # .local/share/gnome-shell
            include_list=[
                "gnome-shell"]

            for folder in os.listdir(f"{HOME_USER}/.local/share/"):
                # TODO
                # folders_list.append(folder)
                if folder in include_list:
                    try:
                        sub.run(f"{COPY_RSYNC_CMD} {HOME_USER}/.local/share/{folder} \
                            {MAIN_INI_FILE.gnome_local_share_main_folder()}", shell=True)
                    except:
                        pass

            # Send notification status
            notification_message("Backing up: .config/ ...")

            # Backup .config/ selected folders
            include_list = [
                "dconf"
            ]

            for folder in os.listdir(f"{HOME_USER}/.config/"):
                if folder in include_list:
                    sub.run(f"{COPY_RSYNC_CMD} {HOME_USER}/.config/{folder} {MAIN_INI_FILE.gnome_config_main_folder()}",shell=True)

        # For KDE
        if get_user_de() == 'kde':
            # Send notification status
            notification_message("Backing up: .local/share ...")

            # Backup .local/share/ selected folder for KDE
            include_list=[
                # "icons",
                "kwin",
                "plasma_notes",
                "plasma",
                "aurorae",
                "color-schemes",
                "fonts",
                "kate",
                "kxmlgui5",
                "icons",
                "themes"]

            for folder in os.listdir(f"{HOME_USER}/.local/share/"):
                # .local/share
                if folder in include_list:
                    try:
                        sub.run(f"{COPY_RSYNC_CMD} {HOME_USER}/.local/share/{folder} {MAIN_INI_FILE.kde_local_share_main_folder()}",shell=True)
                    except:
                        pass

            # Send notification status
            notification_message("Backing up: .config ...")

            # Backup .config/ selected folders for KDE
            try:
                include_list=[
                    # "icons",
                    "gtk-3.0",
                    "gtk-4.0",
                    "kdedefaults",
                    "dconf",
                    "fontconfig",
                    "xsettingsd",
                    "dolphinrc",
                    "gtkrc",
                    "gtkrc-2.0",
                    "kdeglobals",
                    "kwinrc",
                    "plasmarc",
                    "plasmarshellrc",
                    "kglobalshortcutsrc",
                    "khotkeysrc"]

                for folder in os.listdir(f"{HOME_USER}/.config/"):
                    if folder in include_list:
                        sub.run(f"{COPY_RSYNC_CMD} {HOME_USER}/.config/{folder} {MAIN_INI_FILE.kde_config_main_folder()}",shell=True)
            except:
                pass

            # Send notification status
            notification_message("Backing up: .kde/share...")

            # Backup share selected folders for KDE
            try:
                folders_list=[]
                includeList = [
                    # "icons",
                    "gtk-3.0",
                    "gtk-4.0",
                    "kdedefaults",
                    "dconf",
                    "fontconfig",
                    "xsettingsd",
                    "dolphinrc",
                    "gtkrc",
                    "gtkrc-2.0",
                    "kdeglobals",
                    "kwinrc",
                    "plasmarc",
                    "plasmarshellrc",
                    "kglobalshortcutsrc",
                    "khotkeysrc"]

                for folders in os.listdir(f"{HOME_USER}/.kde/share/"):
                    folders_list.append(folders)

                    sub.run(f"{COPY_RSYNC_CMD} {HOME_USER}/.kde/share/{folders} \
                        {str(MAIN_INI_FILE.kde_share_config_main_folder())}", shell=True)
            except:
                pass

    async def backup_flatpak(self):
        # Send notification status
        notification_message("Backing up: Flatpak Applications ...")

        # Backup flatpak installed apps by the name
        try:
            counter = 0
            flatpak_list = []

            CONFIG = configparser.ConfigParser()
            CONFIG.read(SRC_USER_CONFIG)
            with open(MAIN_INI_FILE.flatpak_txt_location(), 'w') as configfile:
                for flatpak in os.popen(GET_FLATPAKS_APPLICATIONS_NAME):
                    flatpak_list.append(flatpak)

                    # Write USER installed flatpak to flatpak.txt inside external device
                    configfile.write(flatpak_list[counter])

                    counter += 1
                    
        except Exception as e:
            print("Flatpak names ERROR:", e)
            pass

        # Backup flatpak data
        if MAIN_INI_FILE.get_database_value('STATUS', 'allow_flatpak_data'):
            # Send notification status
            notification_message("Backing up: Flatpak Data ...")

            # Backup flatpak data folder
            try:
                # Start Flatpak (var/app) backup
                counter = 0
                for _ in flatpak_var_list():
                    # Copy the Flatpak var/app folders
                    sub.run(f"{COPY_RSYNC_CMD} {flatpak_var_list()[counter]} \
                            {MAIN_INI_FILE.flatpak_var_folder()}", shell=True)

                    counter += 1

                # Start Flatpak (.local/share/flatpak) backup
                counter = 0
                for _ in flatpak_local_list():
                    # Copy the Flatpak var/app folders
                    sub.run(f"{COPY_RSYNC_CMD} {flatpak_local_list()[counter]} \
                            {MAIN_INI_FILE.flatpak_local_folder()}", shell=True)

                    counter += 1

            except:
                pass

    async def end_backup(self):
        print("Ending backup...")

        # Send notification status
        notification_message("")

        MAIN_INI_FILE.set_database_value('STATUS', 'backing_up_now', 'False')
        MAIN_INI_FILE.set_database_value('STATUS', 'unfinished_backup', 'No')

        MAIN_INI_FILE.set_database_value('SCHEDULE', 'time_left', 'None')

        # RESTORE DATABASE 
        # Connect to the SQLite database (creates a new database if it doesn't exist)
        conn = sqlite3.connect(MAIN_INI_FILE.restore_settings_location())
        # Create a cursor to interact with the database
        cursor = conn.cursor()

        # Execute the SQL command to create the table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS INFO;
        ''')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        self.set_database_value('INFO', 'wallpaper', f'{user_wallpaper().split("/")[-1]}')

        # KDE
        if get_user_de() == 'kde':
            self.set_database_value('INFO', 'icon', f'{self.get_kde_users_icon_name()}')
            self.set_database_value('INFO', 'cursor', f'{self.get_kde_users_cursor_name()}')
            self.set_database_value('INFO', 'font', f'{self.get_kde_users_font_name()}, {self.get_kde_users_font_size()}')
            self.set_database_value('INFO', 'gtktheme', f'{self.get_gtk_users_theme_name()}')
            self.set_database_value('INFO', 'theme', f'None')
        # GNOME
        else:
            self.set_database_value('INFO', 'icon', f'{self.get_gtk_users_icon_name()}')
            self.set_database_value('INFO', 'cursor', f'{self.get_gtk_users_cursor_name()}')
            self.set_database_value('INFO', 'font', f'{self.get_gtk_user_font_name()}')
            self.set_database_value('INFO', 'gtktheme', f'{self.get_gtk_users_theme_name()}')
            self.set_database_value('INFO', 'theme', f'None')
            self.set_database_value('INFO', 'colortheme', f'None')

        print("Backup is done!")
        print("Sleeping for 60 seconds...")
        # Wait x, so if it finish fast, won't repeat the backup
        time.sleep(60)
        # Quit
        exit()

    #########################################################
    # KDE
    #########################################################
    # KDE cursor
    def get_kde_users_cursor_name(self):
        with open(f"{HOME_USER}/.config/xsettingsd/xsettingsd.conf", "r") as read:
            read=read.readlines()

            for counter in range(len(read)):
                if read[counter].split()[0] == "Gtk/CursorThemeName":
                    # Return users cursor name
                    return read[counter].split()[1].replace('"','')

    # KDE font
    def get_kde_users_font_name(self):
        with open(f"{HOME_USER}/.config/kdeglobals", "r") as read:
            read=read.readlines()

            for counter in range(len(read)):
                if read[counter].startswith("font="):
                    # Return users kde font name
                    return (read[counter]).strip().split(",")[0].replace("font=","")

    # KDE font size
    def get_kde_users_font_size(self):
        with open(f"{HOME_USER}/.config/kdeglobals", "r") as read:
            read=read.readlines()

            for counter in range(len(read)):
                if read[counter].startswith("font="):
                    # Return users kde font size
                    return (read[counter]).strip().split(",")[1]

    # KDE icon
    def get_kde_users_icon_name(self):
        with open(f"{HOME_USER}/.config/xsettingsd/xsettingsd.conf", "r") as read:
            read=read.readlines()
            for counter in range(len(read)):
                if read[counter].split()[0] == "Net/IconThemeName":
                    # Return users icon name
                    return read[counter].split()[1].replace('"','')

    #########################################################
    # GNOME
    #########################################################
    # GTK theme
    def get_gtk_users_theme_name(self):
        user_theme_name=os.popen(GET_USER_THEME_CMD).read().strip().replace("'", "")
        # Return users theme name
        return user_theme_name

        # def users_theme_size():
        #     try:
        #         userThemeSize=os.popen(f"du -s {homeUser}/.themes/{users_theme_name()}")
        #         userThemeSize=userThemeSize.read().strip("\t").strip("\n").replace(f"{homeUser}/.themes/{users_theme_name()}", "").replace("\t", "")
        #         userThemeSize=int(userThemeSize)
        #     except ValueError:
        #         try:
        #             userThemeSize=os.popen(f"du -s {homeUser}/.local/share/themes/{users_theme_name()}")
        #             userThemeSize=userThemeSize.read().strip("\t").strip("\n").replace(f"{homeUser}/.local/share/themes/{users_theme_name()}", "").replace("\t", "")
        #             userThemeSize=int(userThemeSize)
        #         except ValueError:
        #             try:
        #                 userThemeSize=os.popen(f"du -s /usr/share/themes/{users_theme_name()}")
        #                 userThemeSize=userThemeSize.read().strip("\t").strip("\n").replace(f"/usr/share/themes/{users_theme_name()}", "").replace("\t", "")
        #                 userThemeSize=int(userThemeSize)
        #             except ValueError:
        #                 return None

        #     return userThemeSize

    # GTK font
    def get_gtk_user_font_name(self):
        user_font_name=os.popen(GET_USER_FONT_CMD).read().replace("'", "")
        user_font_name=" ".join(user_font_name.split())
        return user_font_name

        # def get_user_font():
        #     if get_user_de() == 'kde':
        #         mainFont=FONT()
        #         return  f"{mainFont.get_kde_font()}, {mainFont.get_kde_font_size()}"

        #     else:
        #         userFontName=os.popen(getUserFontCMD)
        #         userFontName=userFontName.read().replace("'", "")
        #         userFontName=" ".join(userFontName.split())
        #         return userFontName

    # GTK icon
    def get_gtk_users_icon_name(self):
        userIconName=os.popen(GET_USER_ICON_CMD).read().strip().replace("'", "")
        # Return users icon name
        return userIconName

        # def users_icon_size():
        # try:
        #     userIconSize=os.popen(f"du -s {homeUser}/.icons/{users_icon_name()}")
        #     userIconSize=userIconSize.read().strip("\t").strip("\n").replace(f"{homeUser}/.icons/{users_icon_name()}", "").replace("\t", "")
        #     userIconSize=int(userIconSize)

        # except ValueError:
        #     try:
        #         userIconSize=os.popen(f"du -s {homeUser}/.local/share/icons/{users_icon_name()}")
        #         userIconSize=userIconSize.read().strip("\t").strip("\n").replace(f"{homeUser}/.local/share/icons/{users_icon_name()}", "").replace("\t", "")
        #         userIconSize=int(userIconSize)

        #     except ValueError:
        #         try:
        #             userIconSize=os.popen(f"du -s /usr/share/icons/{users_icon_name()}")
        #             userIconSize=userIconSize.read().strip("\t").strip("\n").replace(f"/usr/share/icons/{users_icon_name()}", "").replace("\t", "")
        #             userIconSize=int(userIconSize)

        #         except ValueError:
        #             return None

        # return userIconSize

    # GTK cursor
    def get_gtk_users_cursor_name(self):
        user_cursor_name=os.popen(GET_USER_CURSOR_CMD).read().strip().replace("'", "")
        # Return users GTK cursor name
        return user_cursor_name
    
    def set_database_value(self, table, key, value):
        # Connect to the SQLite database
        conn = sqlite3.connect(SRC_USER_CONFIG_DB)
        cursor = conn.cursor()
            
        cursor.execute(f'''
            INSERT OR REPLACE INTO {table} (key, value)
            VALUES (?, ?)
        ''', (f'{key}', f'{value}'))

        conn.commit()
        conn.close()

    async def main(self):
        # Call the asynchronous functions using await.
        await self.backup_wallpaper()
        await self.backup_home()
        await self.backup_home_hidden_files()
        await self.backup_flatpak()
        await self.end_backup()


if __name__ == '__main__':
    MAIN_INI_FILE = UPDATEINIFILE()
    # Main
    main = BACKUP()
    # To call an async function, you need to run it within an event loop using asyncio.run()
    asyncio.run(main.main())
