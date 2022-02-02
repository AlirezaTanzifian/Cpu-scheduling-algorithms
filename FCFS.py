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
# display list of process
print("List of Process is : ", process)
print("==================================================")
print("==================================================")
# starting process
count = 0
L = int(len(process))
while(count < L):
    y = count
    print("Process %s is running..." %(count+1))
    process.remove(process[0])
    print("Execution of the process %s is completed" %(count+1))
    count+=1
    print(process)
print("All processes were executed with Algorithm FCFS.")