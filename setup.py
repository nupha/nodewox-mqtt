import sys
sys.path.insert(0, 'src')
from nodewox.mqtt import __version__

from distutils.core import setup
setup(name='nodewox-mqtt',
	version=__version__,
	description='Paho MQTT derived client that using M2Crypto TLS',
	author='John Ray',
	author_email='996351336@qq.com',
	license='Eclipse Public License v1.0 / Eclipse Distribution License v1.0',
    package_dir={'': 'src'},
    packages=['nodewox', 'nodewox.mqtt'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
        'Topic :: Internet',
        ]
	)
