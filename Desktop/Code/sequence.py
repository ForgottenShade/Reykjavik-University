#Prints the input number worth of iterations in the built sequence.

def buildSequence(max):
    sequence = [1,2,3]
    for i in range(3,max):
            sequence.append(sequence[i-3] + sequence[i-2] + sequence[i-1])
    return sequence
        

n = int(input("Enter the length of the sequence: ")) # Do not change this line

#print(buildSequence(n))

for i in range(n):
    print(buildSequence(n)[i])
    
