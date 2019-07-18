import numpy as np

f = open('conditions.txt','w+')
jacobians = []

for a in np.linspace(-1,1,5):
    for b in np.linspace(-1,1,5):
        for c in np.linspace(-1,1,5):
            for d in np.linspace(-1,1,5):
                
                if a+d<0 :
                    if a*d-b*c>0 :
                        J = np.matrix([[a,b],[c,d]])
                        jacobians.append(J)
                        f.write(str(J) + '\n\n')
print(jacobians)
f.close()