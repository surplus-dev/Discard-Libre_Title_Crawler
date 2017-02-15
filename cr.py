import requests
import re
import os

i = 0
message = ''
while True:
    print(i)
    temp = requests.get('https://librewiki.net/index.php?title=%ED%8A%B9%EC%88%98:%EA%B8%B4%EB%AC%B8%EC%84%9C&limit=5000&offset=' + str(i * 5000))
    if(temp):
        c = temp.text
        if(re.search("명령에 대한 결과가 없습니다\.", c)):
            break
        else:
            while True: 
                m = re.search('<a href="\/wiki\/(?:[^"]*)" title="(?:[^"]*)">([^<]*)<\/a>', c)
                if(m):
                    g = m.groups()
                    message = message + g[0] + '\n'
                    c = re.sub('<a href="\/wiki\/([^"]*)" title="([^"]*)">([^<]*)<\/a>', '', c, 1)
                else:
                    break
            i = i + 1
    else:
        break
message = re.sub('(?:개인정보 정책|리브레 위키 소개|면책 조항|이용약관|비밀번호를 잊으셨나요\?)\n', '', message)

datafile = open(os.path.abspath(os.path.join('librewiki.txt')) ,'w', encoding="utf-8")
datafile.write(message)
datafile.close()