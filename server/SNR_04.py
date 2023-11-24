def ping ():
    print('SNR_04 ping comlite!')
    return True

def settings(seting = None):
    if seting != None:
        print ('Настройки SNR_04 изменились')
        return seting
    else: 
        print('Настройки SNR_04 без изменений')


def chec_test(param):
    if param > 10 and param < 20: 
        print('Тест SNR_04 провален!')
        return False
    else:
        print('Тест SNR_04 успешен!')
        return True          