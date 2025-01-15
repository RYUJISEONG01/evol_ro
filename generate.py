import pyrosim.pyrosim as pyrosim

def create_robot():
    pyrosim.Start_URDF("body.urdf")

    pyrosim.Send_Cube(name="Torso",pos=[0, 0, 0.5],size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_RLeg",parent="Torso", child="RLeg",type="revolute",position=[0.5, 0, 1.5])
    pyrosim.Send_Cube(name="RLeg",pos=[0.5, 0, 0],size=[1, 1, 1])
    pyrosim.Send_Joint(name="Torso_LLeg",parent="Torso",child="LLeg",type="revolute",position=[-0.5, 0, 1.5])
    pyrosim.Send_Cube(name="LLeg",pos=[-0.5, 0, 0],size=[1, 1, 1])
    pyrosim.End()
create_robot()
