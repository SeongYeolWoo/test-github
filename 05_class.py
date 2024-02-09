class 업무():
    아침업무유무 = False
    
    def 아침업무체크(self):
        self.아침업무유무 = True

    def 아침업무(self, 상자):
        for 물건 in 상자:
            if 물건 == '사과':
                print(f"'{물건}' 냉장실에 넣기")
            elif 물건 == '아이스크림':
                print(f"'{물건}' 냉동실에 넣기")
            else:
                print(f"'{물건}'은 폐기처분")

        self.아침업무체크()

출근 = True

if 출근:
    상자 = ['콩','콩','콩','사과']

    twowix_업무 = 업무()
    print(twowix_업무.아침업무유무)
    twowix_업무.아침업무(상자)
    print(twowix_업무.아침업무유무)

    베어유_업무 = 업무()
    print(베어유_업무.아침업무유무)