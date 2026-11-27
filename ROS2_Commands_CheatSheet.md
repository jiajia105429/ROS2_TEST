节点
ros2 node list：列出当前系统里所有的节点（比如看底盘、雷达、导航节点起没起）。
ros2 node info /节点名：查看某个节点到底订阅了什么、发布了什么、提供了什么服务。

1. 话题
ros2 topic list：列出所有话题，看有没有你要找的（比如 /scan、/cmd_vel）。
ros2 topic echo /话题名：排错神技。实时打印话题里的数据，看里面是不是空的，或者数据对不对。
ros2 topic hz /话题名：排错神技。查这个话题发布的频率，比如雷达正常是 10Hz，如果现在只有 1Hz，说明卡了或者网络丢包。
ros2 topic info /话题名：查这个数据是谁发的（Publisher），谁收的（Subscriber）。

1. 服务（Service）与 参数（Param）
ros2 service list：列出所有服务。
ros2 service call /服务名 服务类型 "参数"：手动发一个请求（比如手动让机器人清空地图），测试服务端有没有反应。
ros2 param list：列出某个节点的所有参数。
ros2 param get /节点名 参数名：查询某个参数当前的值（比如查最大速度限制）。
ros2 param set /节点名 参数名 值：在线修改参数。

1. TF 坐标（排错核心）
ros2 run tf2_tools view_frames：生成 PDF 坐标树，看父子坐标系有没有断。
ros2 run tf2_ros tf2_echo 父系 子系：查两个坐标系的相对位置和距离。