from setup import *
from read_ini_file import UPDATEINIFILE

MAIN_INI_FILE = UPDATEINIFILE()
LATEST_LIST = []

def latest_backup_date_label():
    from get_backup_time import get_latest_backup_time
            
    LATEST_LIST.clear()
    try:
        for dateList in os.listdir(str(MAIN_INI_FILE.backup_folder_name())):
            if dateList not in LATEST_LIST:
                LATEST_LIST.append(dateList)

        LATEST_LIST.sort(reverse = True, key = lambda date: datetime.strptime(date, "%d-%m-%y"))
        latest_backup = str(get_latest_backup_time()[0]).replace("-",":")
        if LATEST_LIST[0] == f"{MAIN_INI_FILE.current_date()}-{MAIN_INI_FILE.current_month()}-{MAIN_INI_FILE.current_year()}": 
            return f"Today, {latest_backup}"
        else:
            # Check todays date, if last backup was Yesterday, return Yesterday
            if int(MAIN_INI_FILE.current_date()) - int(LATEST_LIST[0][:2]) == 1:
                return f"Yesterday, {latest_backup}"
            else:
                return LATEST_LIST[0]
            
    except Exception as e:
        print(e)
        return None

def latest_backup_date():
    LATEST_LIST.clear()
    try:
        for dateList in os.listdir(str(MAIN_INI_FILE.backup_folder_name())):
            if dateList not in LATEST_LIST:
                LATEST_LIST.append(dateList)

        LATEST_LIST.sort(reverse=True, key=lambda date: datetime.strptime(date, "%d-%m-%y"))
        return LATEST_LIST[0]
    except:
        pass

if __name__ == '__main__':
    pass