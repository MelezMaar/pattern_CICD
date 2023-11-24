def ping ():
    print('SNR_05 ping comlite!')
    return True

def settings(seting = None):
    if seting != None:
        print ('Настройки SNR_05 изменились')
        return seting
    else: 
        print('Настройки SNR_05 без изменений')


def chec_test(param):
    if param > 10 and param < 20: 
        print('Тест SNR_05 провален!')
        return False
    else:
        print('Тест SNR_05 успешен!')
        return True          