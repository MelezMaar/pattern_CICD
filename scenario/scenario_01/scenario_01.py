import yaml
import server.ini
import time

def sw_scenario (sw, param1, param2):
    if sw[0].chec_test(param1) == False: return False
    elif sw[1].chec_test(param2) == False: return False
    else: return True

def ggg ():
    pass    