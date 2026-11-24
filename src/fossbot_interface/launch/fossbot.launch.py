import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
import launch_ros.actions


def generate_launch_description():
    fossbot_sim_dir = get_package_share_directory('fossbot_educational_description')

    fossbot_sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(fossbot_sim_dir, 'launch', 'single.launch.py')
        )
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'vel',
            default_value='0.5',
            description='Set velocity'
        ),

        fossbot_sim_launch,

        launch_ros.actions.Node(
            package='fossbot_interface',
            executable='click_controller',
            name='click_controller',
            parameters=[
                {'linear_speed': LaunchConfiguration('vel')}
            ]
        ),

        launch_ros.actions.Node(
            package='fossbot_interface',
            executable='dashboard_node',
            name='dashboard_node'
        )
    ])