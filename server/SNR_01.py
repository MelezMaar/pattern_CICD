
def ping ():
    print('SNR_01 ping comlite!')
    return True

def settings(seting = None):
    if seting != None:
        print ('Настройки SNR_01 изменились')
        return seting
    else: 
        print('Настройки SNR_01 без изменений')

def chec_test(param):
    if param > 10 and param < 20: 
        print('Тест SNR_01 провален!')
        return False
    else:
        print('Тест SNR_01 успешен!')
        return True            
