"""

^        : begin of line
$        : end of line
.        : match any character
\s       : space
\S       : Non-space 
*        : repeats char >=0 times (greedy)
*?       : repeats char >=0 times (non-greedy)
+        : repeats char >=1 times (greedy)
+?       : repeats char >=1 times (non-greedy)
[aeiou]  : in list
[^XYZ]   : not in list
[a-z0-9] : in range
()       : indicates where string extraction

"""

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()                        # 오른쪽 끝문자 삭제
    if re.search('^X-[^-]*?-[^-]*:', line):    # X-로 시작하고 X와 :사이에 -가 2개만 있는 라인 출력
        print(line)


x1 = "X-DSPAM-Probability: 0.0000"
x2 = "X-Authentication-Warning: nakamura.uits.iupui.edu: apache set sender to cwen@iupui.edu using -f"
x = 'From: Using the : character'
y = re.findall('^X-[^-]*?-[^-]*:', x2)
print(y)
# output : ['X-Authentication-Warning: nakamura.uits.iupui.edu:']

y = re.findall('^X-[^-]*?-[^-]*?:', x2)
print(y)
# output : ['X-Authentication-Warning:']



lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('\S+@\S+',lin)
print(y)
# output : ['stephen.marquard@uct.ac.za']

y = re.findall('@([^ ]*)',lin)
print(y)
# output : ['uct.ac.za']

y = re.findall('@([^ .]*)',lin)
print(y)
# output : ['uct']

y = re.findall('.([^.]+@[^.]+).',lin)
print(y)
# output : ['marquard@uct']

y = re.findall('.([^.]+@[^.]+.[^.]+).',lin)
print(y)
# output : ['marquard@uct.ac']