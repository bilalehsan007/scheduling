file=open("my.txt","r")
process =0
num = 0
j = 1

for text in file:
        data = text.split()
        if process == 0:
            process = {data[0]:{"Priority": data[1], "Burst Time":data[2]}}
        elif data[0] not in process:
            process[data[0]]= {"Priority":data[1],"Burst Time":data[2]}
while len(process)>0:
    a = list(process.keys())[0]
    for i in process:
        if process.get(i).get("Priority") > process.get(a).get("Priority"):
            a = i
    x = int(process.get(a).get("Priority"))
    b = int(process.get(a).get("Burst Time"))

    while num < x:
            print(".")
            num +=1
    for i in num(b):
         print("-")
         num += 1

    process.pop(a)
    print ("|"+ a)
