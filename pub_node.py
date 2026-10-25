#pub modle
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PubNode(Node):
    def _init_(self,name):
        super()._init_(name)
        self.pub=self.create_publisher(String,'chatter',10)
        self.timer=self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'hello'
        self.pub.publish(msg)

def main (args=None):
    rclpy.init(args=args)
    node = PubNode("pub_node")
    rclpy.spin(node)
    node.destroy_node
    rclpy.shutdown()

if __name__ == '__main__':
    main()   