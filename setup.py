from setuptools import find_packages, setup

setup(
    name='devicer',
    version='1.0a2',
    description='Linux device activity monitor',
    author='YJ',
    author_email='yj1516268@outlook.com',
    url='https://github.com/YHYJ/Device-activity-monitor',
    license='MIT',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    zip_safe=False,
    install_requires=['evdev', 'toml'],
    entry_points={
        'console_scripts': [
            'findevices=swipe:allDevices',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',      # 3- Alpha, 4- Beta, 5 - Production/Stable
        "Programming Language :: Python :: 3",
    ]
)
