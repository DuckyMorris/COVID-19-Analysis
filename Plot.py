import csv
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

Countries = [""]*209
Countries[0] = 'Afghanistan'
index = 0
Deaths = [0]*209
Cases = [0]*209
Pop =[0]*209
Pop[0] = 38041757
Continent = [""]*209
Continent[0] = 'Asia'


with open('Data.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if f'{row[6]}' != Countries[index]:
                    index = index+1
                    Countries[index] = f'{row[6]}'
                    Continent[index] = f'{row[10]}'
                    Deaths[index] = Deaths[index]+float(f'{row[5]}')
                    Cases[index] = Cases[index]+float(f'{row[4]}')
                    Pop[index] =(f'{row[9]}')
                    line_count += 1
                else:
                    line_count += 1
                    Deaths[index] = Deaths[index]+ float(f'{row[5]}')
                    Cases[index] = Cases[index]+ float(f'{row[4]}')
                    
                    
                     
            line_count += 1
#print(Continent)
for x in range (209):
    if Pop[x] == '':
        Pop[x] = 1
    else:
        Pop[x] = int(Pop[x])
        Cases[x] = (Cases[x]/Pop[x])*1000000
        Deaths[x] = (Deaths[x]/Pop[x])*1000000

for i in range (209):
    if Continent[i] == 'Africa':
        if Countries[i] == 'South_Africa':
            #label
            m = "o"
            c = 'y'
            plt.text(Cases[i],Deaths[i], "RSA")
        else:
            m = "o"
            c = 'y'
            
        
    elif Continent[i] == 'North America':
        m = "o"
        c = 'g'

    elif Continent[i] == 'Europe':
        m = "o"
        c = 'b'

    elif Continent[i] == 'South America':
        m = "o"
        c = 'r'

    elif Continent[i] == 'Middle East':
        m = "o"
        c = 'purple'

    elif Continent[i] == 'Asia':
        m = "o"
        c = 'orange'

    elif Continent[i] == 'Oceania':
        m = "o"
        c = 'c'
    plt.scatter(Cases[i],Deaths[i],marker=m, color=c)
    
plt.xlabel('Reported Confirmed Covid-19 Cases Per Million')
plt.ylabel('Reported Confirmed Covid-19 Deaths Per Million')

plt.show()    
#print(Cases)


