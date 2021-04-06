def Soundex(name):
    name = name.upper()

    result = ''
    result += name[0]

    row = {
        'AEIOUHWY': '0',
        'BFPV': '1',
        'CGJKQSXZ': '2',
        'DT': '3',
        'L': '4',
        'MN': '5',
        'R': '6'
    }

    for word in name[1:]:
        for key in row.keys():
            if word in key:
                temp = row[key]
                if temp != result[-1]:
                    result += temp

    result = result.replace('0', '')
    result = result[:4].ljust(4, '0')
    print('Result : ', result)


if __name__ == '__main__':
    name = input('Enter YourName Or LastName : ')
    Soundex(name)
