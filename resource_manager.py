import yaml
import server.ini
import time

path_connection = r'./repository'

def ceck_devise(id):
    with open(f"{path_connection}/low_devise.yaml", encoding="UTF-8") as file:
        list_low_devices = yaml.safe_load(file)

    with open(f"{path_connection}/lan_settings.yaml", encoding="UTF-8") as file:
        list_lan_devices = yaml.safe_load(file)
    lan_devise = list_lan_devices[id]    

    for key, value in lan_devise.items():
        if list_low_devices[key] == 'free': 
            print(f'Оборудование {key} теперь зарезерервированно')
        else:
            print (f'Оборудование {key} занято. Тестирорвание невозможно!')
            return False
    return True

ceck_devise('id001')    
                         
