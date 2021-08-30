import os
from setuptools import setup, find_packages

current_path = os.path.abspath('C:\\Users\\Peter\\Desktop\\Personal\\11_Repository\\Call of Duty Zombies\\zombie')


def read_file(*parts):
    with open(os.path.join(current_path, *parts), encoding='utf-8') as reader:
        return reader.read()


setup(
    name='cold_war_zombies',
    version='3.0.3',
    packages=['zombie',],
    license='MIT',
    description='A package for comparing weapons in Call of Duty Cold War Zombies',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Peter Rigali',
    author_email='peterjrigali@gmail.com',
    url='https://medium.com/@peterjrigali/best-weapon-in-zombies-9fddd33735c5',
)