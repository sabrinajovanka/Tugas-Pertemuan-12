kata = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def terbilang(n):
    if n < 10:
        return kata[n]
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' billion ' + (terbilang(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + ' million ' + (terbilang(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
        if n // 1_000 == 1:
            return " one thousand " + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
        else:
            return terbilang(n // 1_000) + " thousand " + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
        if n // 100 == 1:
            return ' one hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
        else:
            return terbilang(n // 100) + ' hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
    elif n >= 20:
        if n // 10 == 2:
            return 'twenty ' + terbilang( n % 10)
        elif n // 10 == 3:
            return 'thirty ' + terbilang(n % 10)
        elif n // 10 == 5:
            return 'fifty ' + terbilang(n % 10)
        else:
            return terbilang(n // 10) + ('ty ' if (n // 10) != 8 else 'y ') + terbilang(n % 10)
        # if n == 21:
        #     return ' twenty one'
        # if n == 22:
        #     return ' twenty two'
        # if n == 23:
        #     return ' twenty three'
        # if n == 24:
        #     return ' twenty four'
        # if n == 25:
        #     return ' twenty five'
        # if n == 26:
        #     return ' twenty six'
        # if n == 27:
        #     return ' twenty seven'
        # if n == 28:
        #     return ' twenty eight'
        # if n == 29:
        #     return ' twenty nine'
        # if n == 30:
        #     return ' thirty'
        # if n == 50:
        #     return ' fifty'
        # return terbilang(n // 10) + 'ty ' + (terbilang(n % 10) if n % 10 != 0 else '')
    else:
        if n == 10:
            return ' ten'
        elif n == 11:
            return ' eleven'
        elif n == 12:
            return ' twelve'
        elif n == 13:
            return ' thirteen'
        elif n == 15:
            return ' fifteen'
        else:
            return terbilang(n % 10) + 'teen'        


# test
import os
while True:
    os.system('cls')
    try:
        n = int(input('number ? '))
        print(f'{n:,} = {terbilang(n)}')
    except:
        print('data input anda tidak benar ...')
    os.system('pause')