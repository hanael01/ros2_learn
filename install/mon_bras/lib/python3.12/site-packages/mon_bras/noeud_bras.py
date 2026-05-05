import rclpy
from rclpy.node import Node



class BrasRobotique(Node):

    def __init__(self):
        super().__init__("bras_robotique")
        self.get_logger().info("Noeud bras robotique démarré !")





def main():
    rclpy.init()
    noeud = BrasRobotique()
    rclpy.spin(noeud)
    noeud.destroy_node()
    rclpy.shutdown()



if __name__ == "__main__":
    main()