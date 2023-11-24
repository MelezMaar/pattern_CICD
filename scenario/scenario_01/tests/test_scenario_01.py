import yaml
import server.ini
import time
import pytest
import scenario.scenario_01.scenario_01 as scenario

path_connection = r'./repository'

@pytest.fixture
def devise_for_test():
    devise_for_test = []
    with open(f"{path_connection}/lan_settings.yaml", encoding="UTF-8") as file:
        list_lan_devices = yaml.safe_load(file)
    lan_devise = list_lan_devices['id001'].keys() 
    sw1, sw2 = lan_devise
    devise_for_test.append(eval(f'server.{sw1}'))
    devise_for_test.append(eval(f'server.{sw2}'))
    return devise_for_test
    

@pytest.mark.parametrize(
    ("param1", "param2"),
    [
        (12,
         11),
        (9,
         100),         
    ],
)

@pytest.mark.id001
def test_sw_scenario (devise_for_test, param1, param2):
    assert scenario.sw_scenario(devise_for_test, param1, param2) == True


