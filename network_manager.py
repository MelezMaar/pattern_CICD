import yaml
import server.ini
import time




path_connection = r'./repository'

def scandevices():

    with open(f"{path_connection}/devise.yaml", encoding="UTF-8") as file:
        devices = yaml.safe_load(file)

    conect_list = {}
    for device in devices:
        sw = eval(f'server.{device}')
        if sw.ping() == True: 
            conect_list[device] = sw
        time.sleep(2)
    return conect_list    
    
def settingsdevice(id):

    conect_list = scandevices()

    with open(f"{path_connection}/lan_settings.yaml", encoding="UTF-8") as file:
        list_lan_devices = yaml.safe_load(file)    

    lan_devise = list_lan_devices[id]
    
    for key, value in lan_devise.items():
        time.sleep(2)
        if conect_list[key]:
            conect_list[key].settings(value) 
        else:
            print(f'Настроить {key} не удалось')
            return False
        return True    


settingsdevice('id001')