상자 = ['사과' ,'배', '콩', '두부', '아이스크림']

for value in 상자:
    print(value, end = '\t')

    if value == '사과':
        print('{} 냉장실에 넣기'.format(value))

    elif value == '아이스크림':
        print('{} 냉동실에 넣기'.format(value))

    else:
        print('{}은 폐기처분'.format(value))