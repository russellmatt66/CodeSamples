import sys
import string
import numpy as np

def getTime(rtString: string, rtIdx: int) -> float:
    return float(rtString[:rtIdx])


"""
for i in {1..25}; do     
    echo "----- Run $i -----" >> perfstat_Nnum1_Ntnum2.txt;     
    perf stat -e r5301c7 ./simulation-binary >> perfstat_Nnum1_Ntnum2.txt 2>&1; 
done

^^^ This is the command to acquire performance data for 25 runs with N=num1, and Nt=num2 
"""
fileString = sys.argv[1] # this should be a .txt file containing the output from the runs

fp = open(fileString, 'r')
rtArray = []

while True:
    line = fp.readline()
    if (line == ''):
        break
    rtIdx = line.find("seconds time elapsed") # magic string because of perf stat output
    if (rtIdx == -1):
        continue
    else:
        runtime = getTime(line, rtIdx)
        rtArray.append(runtime)

fp.close()

print("Mean runtime is ")
print(np.mean(np.array(rtArray)))
print("\n")

print("Standard deviation is ")
print(np.std(np.array(rtArray)))
print("\n")
