from setuptools import find_packages, setup

package_name = 'rt2_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rama',
    maintainer_email='rama@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'node1 = rt2_py.node1_publisher:main',
        'node2 = rt2_py.node2_checker:main',
        'node3 = rt2_py.node3_responder:main',
        ],
    },
)
