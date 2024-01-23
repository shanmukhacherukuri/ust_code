from collections import  Counter
line = "which is better python 2 or python 3"

line = line.split()

def check_alpha(str, lst):
    count = 0
    for i in lst:
        if i == str:
            count+=1
    return (str, count)

for x in line:
    result = check_alpha(x,line)
    print(result)

'''Result
('which', 1)
('is', 1)
('better', 1)
('python', 2)
('2', 1)
('or', 1)
('python', 2)
('3', 1)
'''