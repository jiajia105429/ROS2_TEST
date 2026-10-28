import rclpy
from rclpy.node import Node
from my_interface.srv import AddTwoInts

class AdderServer(Node):
    def _init_(self,name):
        super()._init_(name)
        self.srv=self.create_service(AddTwoInts,'add_two_ints',self.adder_callback)
        self.get_logger().info('Service server started,waiting')

    def adder_callback(self,request,reponse):
        reponse.sum=   request.a + request.b
        self.get_logger().info(f'received request:{request.a}+{request.b}={reponse.sum}')
        return reponse

def main(args=None):
    rclpy.init(args=args)
    node=AdderServer("service_adder_server")
    clpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__=='_main_':
     main()                    