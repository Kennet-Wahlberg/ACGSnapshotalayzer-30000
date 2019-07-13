from setuptools import setup

setup(
    name='snapshotalyser 3000',
    version='0,1',
    author="Kennet Wahlberg",
    author_email="kennet.wahlberg@pikewa.se",
    description="Snapshoalayser 3000 is a tool to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/Kennet-Wahlberg/ACGSnapshotalayzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
