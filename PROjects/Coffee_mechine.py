Tea = ['Tea' , 0.50]
Water = ['Water' , 0.15]
Wc = ['White_coffee' , 0.80]
Co = ['Coffee_origenal' , 0.70]
#Функция отказа
def Refusing():
    print('Bye Bye!')
#функция налив напитка
def Pour_drink_and_offer_another():
    print('Your drink is ready with ' , sugar , ' spoons of sugar')
#функция вычесления здачи
def Calculate_money_dipozite():
    change = received_money - x
#функция выбор напитка
def choice_drink():
     print(x_2 , ' = ' , x , ' euro')
     received_money = float(input('Please put the ^^^money : '))
# условия выбора напитка
     if choice == '1':
        x = Tea[1]
        x_2 = Tea[0]
        choice_drink()
# условия выдачи сдачи
     if received_money > x:
            print('Your change is : ' , round(change, 2), ' euro'  )
            Calculate_money_dipozite()
            Pour_drink_and_offer_another()
            con_bye = input('Do you want another drink? Yes/No : ')
            if con_bye == 'Yes':
                continue
            else:
                Refusing()
                break
     elif received_money == x:
            Pour_drink_and_offer_another()
            con_bye = input('Do you want another drink? Yes/No : ')
            if con_bye == 'Yes':
                continue
            else:
                Refusing()
                break
     else:
         Refusing()
         break
print('             Welcome!!!')
while True:
    print('We have:' , 'Index - Name - Price' , '0 = End' , '1 =' Tea[0], Tea[1] 'euro', '\n')
    choice = input('Enter index: ')
    sugar = int(input('Enter quantity of shugar from 0 to 5 : '))
#условия функции отказа
    if choice == '0':
        Refusing()
        break

        

        '''print(x_2 , ' = ' , x , ' euro')
        received_money = float(input('Please put the ^^^money : '))
# условия выдачи сдачи
        if received_money > x:
            Calculate_money_dipozite()
            Pour_drink_and_offer_another()
            con_bye = input('Do you want another drink? Yes/No : ')
            if con_bye == 'Yes':
                continue
            else:
                Refusing()
                break
        elif received_money == x:
            Pour_drink_and_offer_another()
            con_bye = input('Do you want another drink? Yes/No : ')
            if con_bye == 'Yes':
                continue
            else:
                Refusing()
                break
        else:
            Refusing()
            break'''
    
            
    else:
        continue










'''if received_money > price:
    Calculate_money_dipozite()
    Pour_drink_and_offer_another()
    con_bye = input('Do you want another drink? Yes/No : ')
    if con_bye == 'Yes':
        continue
    else:
        Refusing()
        break'''
    
    





#условие для функции налив напитка
'''Pour_drink_and_offer_another()
con_bye = input('Do you want another drink? Yes/No : ')
if con_bye == 'Yes':
    continue
else:
    Refusing()
    break'''
   
