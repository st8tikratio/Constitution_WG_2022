## Code taken from Geek to Geek, then modified

import random


list = ['Decentralization', 'Educational', 'Equality', 'Honesty', 'Inclusivity', 'Self-Sovereignty', 'Sustainability', 'Transparency']
# list = [1, 2, 3, 4, 5, 6, 7, 8]   
# or any list of hashes, addresses, etc.
numruns = 0

# adjust [ < n ] as needed
while (numruns < 51): 
    data = [random.sample(list, 4)]
    print ("Random selection is: " + str(data))
    numruns = numruns + 1

print ("Done!" + str(numruns) + " random sets gnerated!" )
