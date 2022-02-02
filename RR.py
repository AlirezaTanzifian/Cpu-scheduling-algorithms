# creating list
process = []
count = 0
num = input("Please enter the number of your processes: ")
num = int(num)
while(count < num):
    x = input("Please enter the time of your processes %s: " %(count+1))
    x = int(x)
    process.append(x)
    count+=1
print("==================================================")
print("==================================================")
# sort & display list of process
process.sort()
print("List of Process is : ", process)
print("==================================================")
print("==================================================")
#starting process
L = int(len(process))
while(L > 0):
    count = 0
    while(count < L):
        y = count
        if(process[y] == 0):
            process.remove(process[y])
            L = int(len(process))
            count = -1
        elif(process[y] > 0):
            print("Process %s is running..." %(count+1))
            process[y]-=2
            if(process[y] <= 0):
                print("Execution of the process %s is completed" %(count+1))
                process[y] = 0
        print(process)
        count+=1  
print("All processes were executed with Algorithm RR.")