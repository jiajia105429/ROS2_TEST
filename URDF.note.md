建立模型前，得先知道机器人由啥构成：

硬件结构：底盘、外壳、电机（能看得到的实体）。

驱动系统：电机驱动器、电源（让实体动起来的装置）。

传感系统：编码器、IMU、摄像头、雷达（感知自己和环境的器官）。

控制系统：树莓派、电脑等（运行代码的大脑）。

2. URDF 的核心两大件：Link 和 Joint
不管是多复杂的机器人，哪怕是机械臂，都可以拆解成这两样东西：

Link（连杆）：刚体部分。比如人的大臂、小臂，或者小车的车体、轮子。它们自己是动不了的。

Joint（关节）：连接 Link 的部分，提供自由度。比如人的手肘，或者小车的电机轴。

① Link 标签（描述外观和物理属性）
xml
<link name="link_name">
  <visual> 描述长什么样（比如形状、颜色、STL三维模型）</visual>
  <collision> 描述碰撞参数（用于物理引擎计算碰撞）</collision>
  <inertial> 描述质量、惯性矩阵</inertial>
</link>
踩坑点笔记：visual 和 collision 看起来一样，但为了节省算力，实际运动碰撞时，往往把复杂的 visual 模型简化成一个绿色的简单圆柱体 collision 模型。

② Joint 标签（描述怎么动）
xml
<joint name="joint_name" type="joint_type">
  <parent link="父连杆"/>
  <child link="子连杆"/>
  <origin xyz="x y z" rpy="roll pitch yaw"/> <!-- 两个连杆怎么安装到一起 -->
  <axis xyz="0 0 1"/> <!-- 绕哪个轴动 -->
  <limit lower="-3.14" upper="3.14" effort="10" velocity="1.0"/> <!-- 运动极限 -->
</joint>
六种运动类型（最常用的前4种）：

continuous：无限旋转（比如小车的轮子）。

revolute：有限旋转（比如机械臂的关节，有角度限制）。

prismatic：滑动平移（比如直线电机）。

fixed：固定死，不能动（比如把摄像头焊死在车体上）。

单位注意：ROS 里平移默认是米(m)，旋转默认是弧度(rad)，不是度！

3. 怎么看懂一个复杂的机器人模型？
不要一上来就死磕代码！先看 <link> 和 <joint> 标签，搞清楚这个机器人由几个部分组成，谁是父谁是子，画个树状图，全局就清晰了。

4. 今天用到的实操命令
可视化查看模型：ros2 launch learning_urdf display.launch.py （在 RViz 里直接用鼠标拖拽看 3D 模型，非常直观）。

生成模型结构树：urdf_to_graphviz mbot_base.urdf
能直接生成一个 PDF 文件，把 URDF 里的父子连杆结构（树状图）画出来，核对结构和排错必用。