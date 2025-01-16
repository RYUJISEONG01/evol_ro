import numpy as np
import pybullet as p
import pyrosim.pyrosim as pyrosim
import pybullet_data
import numpy
import os
import random
physicsclient =p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
p.loadURDF("plane.urdf")
robotId=p.loadURDF("body.urdf")



import time
LlegSV=numpy.zeros(10000)

num_step=10000
step_index= 0
amplitude = 1
frequency = 0.3
angle_offset = np.pi/2


p.setRealTimeSimulation(1)
pyrosim.Prepare_To_Simulate(robotId)


while p.isConnected() and step_index<num_step :
    LlegSV=pyrosim.Get_Touch_Sensor_Value_For_Link("LLeg")
    input_force1 = amplitude * np.sin(2 * np.pi * frequency * step_index + angle_offset)
    input_force2 = amplitude * np.sin(2 * np.pi * frequency * step_index )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b"Torso_LLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=input_force1,
        maxForce=250
    )
    pyrosim.Set_Motor_For_Joint(
        bodyIndex=robotId,
        jointName=b"Torso_RLeg",
        controlMode=p.POSITION_CONTROL,
        targetPosition=input_force2,
        maxForce=250
    )
    step_index += 1
    time.sleep(1 / 6)


p.disconnect()
data_directory="data"
os.makedirs(data_directory, exist_ok=True)
output_filename = os.path.join(data_directory, "LlegSV.npy")
numpy.save(output_filename,LlegSV)
print(f"sensor values saved to {output_filename}")
