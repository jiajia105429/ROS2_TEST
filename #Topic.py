#Topic
#pub modle
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PubNode(Node):
    def _init_(self,name):
        super()._init_(name)
        self.pub=self.create_publisher(String,'chatter',10)
        self.timer=self.create_timer(0.5,self.timer_callback)

    def time_callback(self):
        msg = String()
        msg.data = 'hello'
        self.pub.publish(msg)

 def main (args=None):
    rclpy.init(args=args)
    node = PubNode("pub_node")
    rclpy.spin(node)
    rclpy.shutdown()

 #sub modle   
 import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SubNode(Node):
    def _init_(self,name)
        super()._init_(name)
        self.sub=self.create_subscription(String,'chatter',self.listener_callback,10)

    def listener_callback(self,msg):
        self.get_logger().info(f'I heard{msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node=SubNode("sub_node")
    rclpy.spin(node)
    rclpy.shutdown            