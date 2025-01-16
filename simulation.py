import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy
import os
physicsclient =p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
robotId=p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)

import time
LlegSV=numpy.zeros(10000)

for i in range(500) :
    p.stepSimulation()
    LlegSV[i]=pyrosim.Get_Touch_Sensor_Value_For_Link("LLeg")

    time.sleep(1/60)

p.disconnect()
data_directory="data"
os.makedirs(data_directory, exist_ok=True)
output_filename = os.path.join(data_directory, "LlegSV.npy")
numpy.save(output_filename,LlegSV)
print(f"sensor values saved to {output_filename}")