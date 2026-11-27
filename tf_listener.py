mport rclpy
from rclpy.node import Node
import tf_transformations
from tf2_ros import TransformException
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener

class TFListener(Node):
    def __init__(self, name):
        super().__init__(name)
        self.tf_buffer = Buffer()
        self.tf_listener = TransformListener(self.tf_buffer, self)
        
        # 假设的坐标系
        self.source_frame = 'house'
        self.target_frame = 'world'
        
        # 创建定时器，每秒执行一次
        self.timer = self.create_timer(1.0, self.on_timer)

    def on_timer(self):
        try:
            now = rclpy.time.Time()
            trans = self.tf_buffer.lookup_transform(
                self.target_frame,
                self.source_frame,
                now)
        except TransformException as ex:
            self.get_logger().info(
                f'Could not transform {self.target_frame} to {self.source_frame}: {ex}')
            return

        pos = trans.transform.translation
        quat = trans.transform.rotation
        
        # 将四元数转换为欧拉角方便阅读
        euler = tf_transformations.euler_from_quaternion([quat.x, quat.y, quat.z, quat.w])
        
        self.get_logger().info('Get %s --> %s transform: [%f, %f, %f] [%f, %f, %f]'
          % (self.source_frame, self.target_frame, pos.x, pos.y, pos.z, euler[0], euler[1], euler[2]))


def main(args=None):
    rclpy.init(args=args)
    node = TFListener("tf_listener")
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()