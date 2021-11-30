file = open("output.txt", "r", encoding='utf-8')
key = ''
s = []


def check_string(key):
    with open('output.txt', "r", encoding='utf-8') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:

        if line[0:len(key)] == key:
            # if key in line:
            print(line)
            return True
    return False


while True:
    key = input('請輸入英文(輸入-1結束迴圈):')
    if key == '-1':
        break

    if check_string(key):
        continue

    else:
        print('This word is not in the dictionary')

file.close()
