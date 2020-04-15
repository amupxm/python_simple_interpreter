raw_file = open("program.amup", "r")


arr = {
    "target": "",
    "sec_target": "",
    "thr_target": "",
    "operator": "+",
    "A": 0,
    "B": 0,
    "C": 0,
    "D": 0
}
lines = []


def split(word):
    return [char for char in word]


for line in raw_file:
    lines.append(line)
    temp_len = len(line)
    arr['target'] = line[0]
    for index in range(temp_len):
        if(line[index] != " " and index > 0):
            if line[index] in ['A', 'B', 'C', 'D']:
                if(arr['sec_target'] == ""):
                    arr['sec_target'] = line[index]
                elif (arr['thr_target'] == ""):
                    arr['thr_target'] = line[index]
            elif line[index] in ['+', '-', '*', '/', '=']:
                arr['operator'] = line[index]
            elif line[index] == "\n" or index == temp_len:
                if(arr['sec_target'] != "" and arr['operator'] != "" and arr['thr_target'] != ""):
                    if(arr['operator'] == '+'):
                        arr[arr['target']] = str(int(
                            arr[arr['sec_target']]) + int(arr[arr['thr_target']]))
                    elif(arr['operator'] == "-"):
                        arr[arr['target']] = str(int(
                            arr[arr['sec_target']]) - int(arr[arr['thr_target']]))
                    elif(arr['operator'] == "*"):
                        arr[arr['target']] = str(
                            int(
                                arr[arr['sec_target']]) * int(arr[arr['thr_target']])
                        )
                    elif(arr['operator'] == "/"):
                        arr[arr['target']] = str(
                            int(
                                arr[arr['sec_target']]) / int(arr[arr['thr_target']]))
                    elif(arr['operator'] == "="):
                        print("")

                    arr['thr_target'] = ''
                    arr['operator'] = ""
                    arr['sec_target'] = ''
                    arr['target'] = ""

            else:

                arr[str(arr['target'])] = str(line[index])
print('A = ' + str(arr['A']))
print('B = ' + str(arr['B']))
print('C = ' + str(arr['C']))
print('D = ' + str(arr['D']))

print("-------------Converted to C++ language -----------")
print("")
print("#include <iostream.h> \n\n int main () \n{ \n int A,B,C,D ; \n ")
for line in lines:
    print(line.replace("\n", ";"))
print("count << A; \n return 0 ; \n }")
