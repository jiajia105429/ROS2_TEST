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
