#Zad1
def name(firstletter: str, surname: str) -> str:
    return (firstletter + '.' + surname)
print(name('E','Poreda'))
#Zad2
def name2(wholename: str, surname2: str) -> str:
    return (wholename[0].capitalize()+'.'+ surname2.capitalize())
print(name2('Eryk','Poreda'))
#Zad3
def yearofborn(first2:  str, last2: str, age: int) -> int:
    return (int(first2+last2) - age)
print(yearofborn('20','21',21))
#Zad4
def yearofbornupgrade(name_upgrade, surname_upgrade):
    func = yearofborn('20','21',21)
    return func
print(yearofbornupgrade('Eryk','Poreda'))
#Zad  5
def division(a,b):
    if a > 0 and b >=0:
        print('Obie liczby są dodatnie, b jest wieksze od 0')
        return a/b
print(division(10,5))
#Zad 6
sum = 0
count = 0
while True:
    num = input("Podaj liczbę")
    sum += float(num)
    count +=1
    if sum >=100:
        print(sum)
        break
#Zad7
def list_to_tuple(list):
    list = [1,2,3,4]
    return tuple(list)
print(list_to_tuple(1))

#Zad8
list = []
new_list = ''
while new_list != 'q':
    new_list = input('Wprowadz nowy element do listy, wprowadz q by przestac:')
    list.append(new_list)
print(tuple(list))

#Zad9
def weekday_number(num: int) -> str:
    return {
         1: 'Poniedzialek',
         2 : 'Wtorek',
         3: 'Środa',
         4: 'Czwartek',
         5: 'Piątek',
         6: 'Sobota',
         7: 'Niedziela',
    }[num]
print(weekday_number(2))

#Zad10
def ispalindrome(string) -> bool:
    reversed_string = string[::-1]
    if (string != reversed_string):
        return bool(False)
    else:
        return bool(True)
print(ispalindrome('abba'))
