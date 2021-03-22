import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
 
 
coords1 = [0.9, -0.4,0.3]
coords2 = [0,0,0]
 
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')
 
ax.scatter((coords1[0], coords2[0]),
        (coords1[1], coords2[1]),
        (coords1[2], coords2[2]),
         color="k", s=150)
 
ax.plot((coords1[0], coords2[0]),
        (coords1[1], coords2[1]),
        (coords1[2], coords2[2]),
         color="r")
 
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')



# 计算距离
np_c1 = np.array(coords1)
np_c2 = np.array(coords2)
distance = np.linalg.norm(np_c1 - np_c2)
ax.text(x=(coords1[0]+ coords1[0])/2, y=(coords1[1]+ coords1[1])/2, z=(coords1[2]+ coords1[2])/2, s=str(distance))
 
 
plt.title('Euclidean distance between 2 3D-coordinates')
 
plt.show()
