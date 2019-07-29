num = open('./other/number.txt', 'w+')
num1 = open('./other/number1.txt', 'w+')
for i in range(1 << 16):
    num.write(str(i) + "\n")
    num1.write(str(i) + " ")

num.close()
num1.close()
