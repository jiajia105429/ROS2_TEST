import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf_transformations
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster

class StaticTFBroadcaster(Node):
    def __init__(self, name):
        super().__init__(name)
        self.tf_broadcaster = StaticTransformBroadcaster(self)
        
        # 初始化坐标变换消息
        static_transformStamped = TransformStamped()
        static_transformStamped.header.stamp = self.get_clock().now().to_msg()
        static_transformStamped.header.frame_id = 'world'
        static_transformStamped.child_frame_id = 'house'
        
        # 设置平移
        static_transformStamped.transform.translation.x = 10.0
        static_transformStamped.transform.translation.y = 5.0
        static_transformStamped.transform.translation.z = 0.0
        
        # 欧拉角转四元数 (roll, pitch, yaw)
        quat = tf_transformations.quaternion_from_euler(0.0, 0.0, 0.0)
        
        # 设置旋转
        static_transformStamped.transform.rotation.x = quat[0]
        static_transformStamped.transform.rotation.y = quat[1]
        static_transformStamped.transform.rotation.z = quat[2]
        static_transformStamped.transform.rotation.w = quat[3]

        # 发送静态坐标变换
        self.tf_broadcaster.sendTransform(static_transformStamped)


def main(args=None):
    rclpy.init(args=args)
    node = StaticTFBroadcaster("static_tf_broadcaster")
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()