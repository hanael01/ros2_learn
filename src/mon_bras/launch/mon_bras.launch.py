from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory



"""def generate_launch_description():
    return LaunchDescription([

        Node(
            package='mon_bras',
            executable='noeud_bras',
            name='bras_robotique',
            output='screen'
        ),


        Node(
            package='mon_bras',
            executable='affichage_bras',
            name='affichage_bras',
            output='screen'
        ),

    ])"""

def generate_launch_description():

    urdf_file = os.path.join(
        get_package_share_directory('mon_bras'),
        'urdf',
        'mon_bras.urdf'
    )

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),


        Node(
             package='joint_state_publisher_gui',
             executable='joint_state_publisher_gui',
             name='joint_state_publisher_gui',
             output='screen'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        ),

    ])

