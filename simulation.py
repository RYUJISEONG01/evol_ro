import pybullet as p
import pybullet_data
physicsclient =p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
planeId=p.loadURDF("body.urdf")

import time
for i in range(1000) :
    p.stepSimulation()
    time.sleep(1/60)
    print(i)
p.disconnect()
