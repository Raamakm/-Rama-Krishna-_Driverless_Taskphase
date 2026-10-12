import rclpy
from rclpy.node import Node
from taskone_msgs.msg import TaskOne


class WheelPublisher(Node):
    def __init__(self):
        super().__init__('wheel_publisher')
        self.pub = self.create_publisher(TaskOne, '/taskone', 10)

    def publish_values(self, ang_vel, radius):
        msg = TaskOne()
        msg.ang_vel = ang_vel
        msg.radius = radius
        self.pub.publish(msg)
        self.get_logger().info(f'Published: ang_vel={ang_vel}, radius={radius}')


def main(args=None):
    rclpy.init(args=args)
    node = WheelPublisher()
    try:
        while rclpy.ok():
            try:
                ang_vel = float(input('Enter angular velocity (rad/s): '))
                radius = float(input('Enter wheel radius (m): '))
            except ValueError:
                print('Please enter valid numbers.')
                continue
            node.publish_values(ang_vel, radius)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
