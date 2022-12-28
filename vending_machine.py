import time
cash=[10,20,50,100]
cash_returned=[1,5,10,20,50,100]
cash_returned.reverse()

#assumption: type of cash available in vending machine is 1,5,10,20,50,100

vending_machine={'cola':1,'sprite':5,'7up':10,'fanta':20,'rootbeer':50,'anker':100}

try:
    money=int(input('insert money here: '))
    for drink in (vending_machine.keys()):
        print(drink, vending_machine[drink])

    drink = input('select your drink: ')
    while drink not in vending_machine.keys():
        drink = input('that one is not available right now, please select another drink: ')

    if money< vending_machine[drink]:
        while money < vending_machine[drink]:
            try:
                extra = int(input('please insert more money or input 0 to escape: '))
                money += extra
                print('your balance now: {}'.format(money))
                if extra == 0:
                    if money>0:
                        print('please take it back')
                    else:
                        pass
                    break
                else:
                    change = money - vending_machine[drink]
                    change_komakai = []
                    for komakai in cash_returned:
                        while change >= komakai:
                            change -= komakai
                            change_komakai.append(komakai)
                    for i in range(10):
                        print('-', end='')
                        time.sleep(0.3)
                    print('')
                    print('here is your {}'.format(drink))
                    if len(change_komakai) == 0:
                        pass
                    else:
                        print('your change is: {}'.format(change_komakai))
            except:
                print('please insert money only')
    else:

        change = money - vending_machine[drink]
        change_komakai = []
        for komakai in cash_returned:
            while change >= komakai:
                change -= komakai
                change_komakai.append(komakai)
        for i in range(10):
            print('-', end='')
            time.sleep(0.3)
        print('')
        print('here is your {}'.format(drink))
        if len(change_komakai) == 0:
            pass
        else:
            print('your change is: {}'.format(change_komakai))

except:
    print('please insert money only')
print('come again!')


