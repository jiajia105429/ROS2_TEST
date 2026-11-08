import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import  QoSProfile,QoSReliabilityPolicy,QoSHistoryPolicy

class SubscriberNode(Node):
    def _init_(self,name):
        super()._init_(name)
        qos_profile = QoSProfile(
                            reliability=QoSReliabilityPolicy.RELIABLE,#reliability = QoSReliabilityPoilcy.BEST_EFFORT
                            history=QoSHistoryPolicy.KEEP_LAST
                            depth=1
        )

        self.sub=self.create_subscription(
            String,"chatter",self.listener_callback,qos_profile
        )

    def listener_callback(self,msg):
        self.get_logger().info(f'I heard:{msg.data}')

def main(args=None):   
    rclpy.init(args=args)
    node = SubscriberNode ("qos_sub")
    clpy.spin(node)
    ode.destroy_node()
    rclpy.shutdown()