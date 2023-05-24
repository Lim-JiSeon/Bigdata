# 윈도우 콘솔 사용을 상정하여 제작
# 콘솔을 X키로 눌러 닫으면 저장이 잘 안될 수도 있음
# 엔터키를 눌러 종료할 것

from colorama import Fore, Style
import os
import utils

fp, fn = utils.filePaths()
filePath = fp[0]
fileName = fn[0]

with open(fileName, 'r+', encoding ='cp949') as f:
    lines = f.readlines()
    lines = [line.rstrip('\n') for line in lines]
    print('\n')
    while 1:
        print('enter를 눌러 종료')
        print('추가/삭제할 단어 입력 : ', end = '')
        word = input()
        if word == '':
            break

        os.system('cls')

        if word in lines:  # 이미 존재하면 삭제
            print(f'{Fore.LIGHTBLACK_EX}{word}{Style.RESET_ALL}을 목록에서 {Fore.RED}삭제{Style.RESET_ALL}(Y/N)', end = ' ')
            opt = input()
            os.system('cls')
            if opt == 'Y' or opt == 'y':
                lines.remove(word)
                print(f'{Fore.LIGHTBLACK_EX}{word}{Style.RESET_ALL}이 목록에서 {Fore.RED}삭제{Style.RESET_ALL}됨\n')
            else:
                print('\n')
                continue
        else:
            lines.append(word)
            print(f'{Fore.LIGHTBLACK_EX}{word}{Style.RESET_ALL}이 목록에 {Fore.BLUE}추가{Style.RESET_ALL}됨\n')

        lines.sort()    
        
        f.seek(0)
        f.truncate(0)
        f.write('\n'.join(lines))