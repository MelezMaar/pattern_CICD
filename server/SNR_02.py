def ping ():
    print('SNR_02 ping comlite!')
    return True

def settings(seting = None):
    if seting != None:
        print ('Настройки SNR_02 изменились')
        return seting
    else: 
        print('Настройки SNR_02 без изменений')

def chec_test(param):
    if param > 10 and param < 20: 
        print('Тест SNR_02 провален!')
        return False
    else:
        print('Тест SNR_02 успешен!')
        return True          