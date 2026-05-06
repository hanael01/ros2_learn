import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray


class AffichageBras(Node):

    def __init__(self):
        super().__init__("affichage_bras")

        self.subscription = self.create_subscription(
            Float32MultiArray,
            '/positions_joints',
            self.recevoir_positions,
            10
        )

        self.get_logger().info("Noeud affichage démarré !")

    def recevoir_positions(self, msg):
        self.get_logger().info(f"Positions reçues : {list(msg.data)}")


def main():
    rclpy.init()
    noeud = AffichageBras()
    rclpy.spin(noeud)
    noeud.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()