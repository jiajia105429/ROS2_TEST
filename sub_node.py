#sub modle   
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubNode(Node):
    def _init_(self,name):
        super()._init_(name)
        self.sub=self.create_subscription(String,'chatter',self.listener_callback,10)

    def listener_callback(self,msg):
        self.get_logger().info(f'I heard{msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node=SubNode("sub_node")
    rclpy.spin(node)
    rclpy.shutdown            

if __name__ == '__main__':
    main()      