这是ROS 2（Ubuntu 22.04 + Humble）手动敲的代码练习。是最基础的话题、服务、动作和参数。

Topic（话题）：写了发布者和订阅者，顺便测了一下 Qos 配置。
service（服务）：敲了个算加法的服务端和客户端。
action（动作）：让机器人画圆，测了带进度反馈（feedback）的异步通信。
parameter（参数）：写了怎么建参数、怎么读参数。

运行三板斧:
colcon build
source install/setup.bash
ros2 run learning_topic topic_helloworld_pub

踩过的坑：
1，发布者用了 best_effort，订阅者用了 reliable。这俩不匹配系统就直接静默断连了，用 ros2 topic info --verbose 。
2，参数动态修改：本来以为改参数得重启节点，试了一下在终端敲 ros2 param set，节点没重启，颜色阈值直接就变了，

详细学习笔记
- [TF2 坐标变换与跟随笔记](./TF2_Notes.md)
- [Launch 多节点启动笔记](./Launch_Notes.md)
- [TF2 广播器,监听器笔记](./transform.md)
- [Gazebo 三维物理仿真与 XACRO 笔记](./Gazebo_XACRO_Notes.md)
-  [Rviz 可视化与传感器仿真笔记](./Rviz_Sensors_Notes.md)
-  [ROS2 常用调试指令速查表](./ROS2_Commands_CheatSheet.md)
-  [Rviz 与 rqt 调试工具笔记](./Rviz_rqt_Debug_Notes.md)