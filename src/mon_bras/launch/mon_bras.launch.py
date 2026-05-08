from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
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

    ])