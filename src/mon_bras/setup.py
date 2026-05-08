from setuptools import find_packages, setup

package_name = 'mon_bras'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/mon_bras.launch.py'])
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tsoud',
    maintainer_email='hanaeldream@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'noeud_bras = mon_bras.noeud_bras:main',
            'affichage_bras = mon_bras.affichage_bras:main'
        ],
    },
)
