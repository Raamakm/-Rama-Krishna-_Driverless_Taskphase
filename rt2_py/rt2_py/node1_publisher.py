import threading
import rclpy
from rclpy.node import Node
from rt2_msgs.msg import RT2String


class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')
        self.pub = self.create_publisher(RT2String, '/rt2_string', 10)
        self.current = None
        self.create_timer(1.0, self.publish_current)

    def publish_current(self):
        if self.current is None:
            return
        msg = RT2String()
        msg.data = self.current
        self.pub.publish(msg)


def input_loop(node):
    while rclpy.ok():
        try:
            text = input('Enter a string: ').strip()
        except EOFError:
            break
        if text:
            node.current = text


def main(args=None):
    rclpy.init(args=args)
    node = StringPublisher()
    threading.Thread(target=input_loop, args=(node,), daemon=True).start()
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
