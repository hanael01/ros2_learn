class BrasRobotique:

    def __init__(self, nb_joints):
        self.nb_joints = nb_joints

    def afficher_joints(self):
        print(f"Ce bras a {self.nb_joints} joints")


Niryo = BrasRobotique(6)
Bob = BrasRobotique(4)
Niryo.afficher_joints()
Bob.afficher_joints()
