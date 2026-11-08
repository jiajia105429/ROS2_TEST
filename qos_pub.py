import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import  QoSProfile,QoSReliabilityPolicy,QoSHistoryPolicy

class PublisherNode(Node):
    def _init_(self,name):
        super()._init_(name)

        qos_profile = QoSProfile(
                    reliability=QoSReliabilityPolicy.RELIABLE,#reliability = QoSReliabilityPoilcy.BEST_EFFORT
                    history=QoSHistoryPolicy.KEEP_LAST
                    depth=1)
        
            

    self.pub = self.create_publisher(
        String,"chatter",qos_profile)
    self.timer=self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "hello world"
        self.pub.publish(msg)
        self.get_logger().info(f'publishing:{msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode ("qos__pub")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()