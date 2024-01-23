#Open file from the different path and make sure, while running this script you replaced absolute test path
f = open(r"C:\Users\hp\PycharmProjects\ust_project\text_sample.txt", 'r').readlines()
#We opened file and read all lines in a list format, Now we'll print 2 lines from the file
for i in range(2):
    print(f"Line no: {i} \n", f[i])