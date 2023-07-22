from setup import *
from read_ini_file import UPDATEINIFILE

async def restore_kde_config():
    MAININIFILE=UPDATEINIFILE()

    try:
        sub.run(f"{COPY_RSYNC_CMD} {MAININIFILE.kde_config_main_folder()}/ {HOME_USER}/.config/", shell=True)
    except:         
        pass

    return "Task completed: restore kde config"

if __name__ == '__main__':
    pass
