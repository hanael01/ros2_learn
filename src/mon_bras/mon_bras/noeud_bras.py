import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray


class BrasRobotique(Node):

    def __init__(self):
        super().__init__("bras_robotique")
        
        self.publisher_ = self.create_publisher(
            Float32MultiArray,
            '/positions_joints',
            10
        )


         
        self.positions = [1.0, 0.0, 3.0, 0.0, 5.0, 0.0]

        self.timer = self.create_timer(1.0, self.publier_positions)

        self.get_logger().info("Noeud bras robotique démarré !")



    def publier_positions(self):
        msg = Float32MultiArray()
        msg.data = self.positions
        self.publisher_.publish(msg)
        self.get_logger().info(f"Positions publiées : {self.positions}")



def main():
    rclpy.init()
    noeud = BrasRobotique()
    rclpy.spin(noeud)
    noeud.destroy_node()
    rclpy.shutdown()



if __name__ == "__main__":
    main()