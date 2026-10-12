import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String


class Responder(Node):
    def __init__(self):
        super().__init__('responder')
        self.create_subscription(Int32, '/palindrome_flag', self.flag_cb, 10)
        self.reply_pub = self.create_publisher(String, '/palindrome_reply', 10)

    def flag_cb(self, msg):
        reply = String()
        reply.data = 'Yes' if msg.data == 1 else 'No'
        self.reply_pub.publish(reply)
        self.get_logger().info(f'Got {msg.data} -> replying "{reply.data}"')


def main(args=None):
    rclpy.init(args=args)
    node = Responder()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
