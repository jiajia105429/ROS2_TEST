Gazebo：造数据的。它是一个物理仿真平台，能模拟重力、摩擦、传感器（摄像头、雷达），没有实物机器人时用它来生成“虚拟数据”。

Rviz：看数据的。它没有物理引擎，只负责把 ROS 里的数据（话题）画出来。如果没有 Gazebo 或者真机提供数据，Rviz 里啥也没有。

常用组合：Gazebo 在后台算物理数据，Rviz 在前台看图像/模型，完美配合。

2. 常用传感器仿真（Gazebo 插件配置）
Gazebo 里装传感器，全靠 <gazebo> 标签里挂载对应的插件。

① 彩色相机 (Camera)
插件：libgazebo_ros_camera.so

关键配置：分辨率（1280x720）、视野角度、发布图像话题 image_raw。

Rviz 显示：在 Displays 里 Add -> Image，选对话题，就能看到画面。

② 三维相机 (RGBD/Kinect)
插件：还是 libgazebo_ros_camera.so，但 sensor type 要写成 depth。

关键配置：除了图像，还会输出深度信息，形成点云 points。

Rviz 显示：Add -> PointCloud2，把 Fixed Frame 设为 odom，就能看到带颜色的 3D 点云。

③ 激光雷达 (LiDAR)
插件：libgazebo_ros_ray_sensor.so

关键配置：扫描角度、最小/最大探测距离、采样点数（如 360）。

Rviz 显示：Add -> LaserScan，Fixed Frame 设为 odom，就能看到扫描出的点。

3. 实操命令速查
bash
# 启动 Rviz2
ros2 run rviz2 rviz2

# 启动带 RGBD 相机的仿真环境
ros2 launch learning_gazebo load_mbot_rgbd_into_gazebo.launch.py

# 启动带激光雷达的仿真环境
ros2 launch learning_gazebo load_mbot_laser_into_gazebo.launch.py

在 Rviz 里看不到图Fixed Frame 没设对。一般设成 odom 或 base_link 就好了。

如果 Rviz 里显示 No Image，先别急着改代码，去终端敲 ros2 topic list 看看有没有那个话题，再用 ros2 topic echo 看看话题里有没有数据。没数据那就是 Gazebo 插件没配好。

