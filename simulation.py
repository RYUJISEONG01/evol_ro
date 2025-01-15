import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
physicsclient =p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
robotId=p.loadURDF("body.urdf")

pyrosim.Prepare_To_Simulate(robotId)

import time
for i in range(1000) :
    p.stepSimulation()
    LLeg_touchsensor=pyrosim.Get_Touch_Sensor_Value_For_Link("LLeg")
    print(f"sensor value :{LLeg_touchsensor}"  )
    time.sleep(1/60)
    print(i)
p.disconnect()
