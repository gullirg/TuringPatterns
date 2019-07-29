import numpy as np

f = open('phase_plane_conditions.txt','w+')
jacobians = []
for i in np.linspace(-1,1,3):
    f.write('TRACE = '+str(i)+ '\n\n')
    for j in np.linspace(-1,1,3):
        f.write('DETERMINANT = '+str(j)+ '\n\n')
        for a in np.linspace(-1,1,3):
            for b in np.linspace(-1,1,3):
                for c in np.linspace(-1,1,3):
                    for d in np.linspace(-1,1,3):
                        
                        if a+d==i :
                            if a*d-b*c==j :
                                J = np.matrix([[a,b],[c,d]])
                                jacobians.append(J)
                                f.write(str(J) + '\n\n')
print(jacobians)
f.close()