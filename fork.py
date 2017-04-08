import requests
import re
import os

i = 0
message = ''
while True:
    print(i)
    
    if(i == 0):
        temp = requests.get('https://librewiki.net/wiki/특수:모든문서')
    else:
        temp = requests.get('https://librewiki.net/' + url)
        
    if(temp):
        c = temp.text
        
        while True: 
            m = re.search('<a href="\/wiki\/([^"]*)"(?: class="mw-redirect")? title="([^"]*)">([^<]*)<\/a>', c)
            if(m):
                g = m.groups()
                message = message + g[2] + '\n'
                
                print(g[2])
                
                c = re.sub('<a href="\/wiki\/(?:[^"]*)"(?: class="mw-redirect")? title="([^"]*)">([^<]*)<\/a>', '', c, 1)
            else:
                break
                
        i = i + 1
        
        m = re.search('<a href="\/([^"]*)" title="특수:모든문서">다음 문서 \((?:[^<]*)<\/a>', c)
        if(m):
            g = m.groups()
            url = re.sub('&amp;', '&', g[0], 1)
            print(url)
        else:
            break
    else:
        break
        
message = re.sub("(개인정보 정책|리브레 위키 소개|면책 조항|이용약관|비밀번호를 잊으셨나요\?)\n", "", message)

datafile = open(os.path.abspath(os.path.join('librewiki.txt')) ,'w', encoding="utf-8")
datafile.write(message)
datafile.close()
