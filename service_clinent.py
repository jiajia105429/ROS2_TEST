import sys
import rclpy
from rclpy.node import Node
from my_interface.srv import AddTwoInts

class AdderClient(Node):
    def __init__(self,name):
        super().__init__(name)
        self.client=self.create_client(AddTwoInts,'add_two_ints')
        while not self.cilent.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('waiting....')
        self.request=AddTwoInts.Request()

    def send_request(self):
        self.request.a=3
        self.request.b=5
        self.future = self.client.call_async(self.request)

def main(args=None):
    rclpy.init(args=args)
    node= AdderClient("service_adder_client")  
    node.send_request()
    while rclpy.ok():
        rclpy.spin_once(node)
        if node.future.done():
            try:
                response=node.future.result()
            except Exception as e:
                node.get_logger().info(f'fail:{e}')
            else:
                node.get_logger.info(f'result:{node.request.a}+{node.request.b}={response.sum}')
                break     
    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()
      
    