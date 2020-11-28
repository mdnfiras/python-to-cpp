# imports
import sys
import os
from zipfile import ZipFile
import matplotlib.pyplot as plt

# preparing output folder
if (not(os.path.isdir("report"))):
    os.mkdir("report")

with ZipFile('data.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall()

contests = list()
problems = list()
total = 0

for i in range(1400):
    contests.append(i)
    j = 0
    if (os.path.isdir('data/python_code/' + str(i)) and os.path.isdir('data/cpp_code/' + str(i))):
        path, dirs, files = next(os.walk('data/python_code/' + str(i)))
        for folder in dirs:
            if ((folder == '.') or (folder == '..')):
                continue
            if (os.path.isdir('data/cpp_code/' + str(i) + '/' + folder)):
                j += 1
                total += 1
    problems.append(j)

plt.plot(contests, problems)
plt.xlabel("Contest ID")
plt.ylabel('Problems')
plt.title('Problems per contest')
plt.show()
plt.savefig('report/data.png')

f = open("report/data.txt", "w")
print("Total number of problems covered both in Python and C++ : " + str(total), file=f)
f.close()
