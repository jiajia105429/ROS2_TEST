TF：Transform 坐标变换
定义：实时计算机器人各个零件之间的相对位置
常用：map（地图）：以客观世界的物理位置为基准
odom（里程计）：靠自己轮子转几圈来推算位置（有误差）
base_link（车底盘）：机器人自己的物理中心点
laser_link/ camera_link（雷达/摄像头）：雷达，摄像头装在哪
命令：
ros2 run tf2_tools view_frames：打开TF2工具箱里‘查看坐标系’。看全家福，把当前所有零件（海龟1、海龟2、世界地图等）的位置关系，画成了一张“家谱图”。
ros2 run tf2_ros tf2_echo turtle2 turtle1：把海龟2相对于海龟1的坐标打印出来。
ros2 run rviz2 rviz2 -d <配置文件路径>：打开rviz，把数字变成3d坐标轴，看动态变化。
-d：加载指定的配置文件
$(ros2 pkg prefix --share turtle_tf2_py)/rviz/turtle_rviz.rviz：打开 Rviz，并加载那个叫 turtle_tf2_py 的包里面，专门用来演示海龟坐标的配置文件。
$( ... )：linux里，指先运行括号里的命令，再把结果拿出来填到这里
pkg prefix ：去查这个包安装在哪
--share：去查这个包里的share文件夹在哪
turtle_tf2_py：包名
rviz/turtle_rviz.rviz：具体的文件路径。
