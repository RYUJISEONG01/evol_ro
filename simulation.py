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
data_directory="data" # 책장을 만드는 것에 비유, 책장을 만들 공간은 data_directory이며, 거기의 이름은 data라고 명명
os.makedirs(data_directory, exist_ok=True) #책장을 만드는 작업,책장이 이미 있으면 사용, 없으면 만들기
output_filename = os.path.join(data_directory, "LlegSV.npy") #책을 책장에 넣을 정확한 위치를 정하는 것
numpy.save(output_filename,LlegSV) # 책을 저장 위치에 넣는 작업
print(f"sensor values saved to {output_filename}")