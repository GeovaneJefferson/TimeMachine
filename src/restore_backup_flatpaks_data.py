from setup import *
from read_ini_file import UPDATEINIFILE
from notification_massage import notification_message_current_backing_up


MAIN_INI_FILE = UPDATEINIFILE()

async def restore_backup_flatpaks_data():
	print("Restoring flatpaks data...")
	
	for output in os.listdir(f"{MAIN_INI_FILE.flatpak_var_folder()}"):
		notification_message_current_backing_up(f'Restoring: {output}...')

		# Restore flatpak data (var) folders from external device
		sub.run(f"{COPY_RSYNC_CMD} {MAIN_INI_FILE.flatpak_var_folder()}/{output} {src_flatpak_var_folder_location}", shell=True)

	for output in os.listdir(f"{MAIN_INI_FILE.flatpak_local_folder()}"):
		notification_message_current_backing_up(f'Restoring: {output}...')

		# Restore flatpak data (Local) folders from external device
		sub.run(f"{COPY_RSYNC_CMD} {MAIN_INI_FILE.flatpak_local_folder()}/{output} {src_flatpak_local_folder_location}", shell=True)

	return "Task completed: Wallpaper"
            

if __name__ == '__main__':
    pass