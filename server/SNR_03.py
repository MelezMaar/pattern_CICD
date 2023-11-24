def ping ():
    print('SNR_03 ping comlite!')
    return True

def settings(seting = None):
    if seting != None:
        print ('Настройки SNR_03 изменились')
        return seting
    else: 
        print('Настройки SNR_03 без изменений')

def chec_test(param):
    if param > 10 and param < 20: 
        print('Тест SNR_03 провален!')
        return False
    else:
        print('Тест SNR_03 успешен!')
        return True          