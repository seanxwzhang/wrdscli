from setuptools import setup, find_packages

setup(
    name='wrdscli',
    version='0.0.1',
    description='Cli for interacting with WRDS',
    author='Sean Zhang',
    author_email='seanxwzhang@gmail.com',
    packages=find_packages(),
    install_requires=[
        'sqlalchemy>=1.3',
        'click>=7.0',
        'psycopg2>=2.7.6',
        'attrs>=19.2.0',
        'influxdb>=5.2.3'
    ],
    python_requires='>=3.7.4',
    entry_points='''
        [console_scripts]
        wrdscli=wrdscli.wrdscli:wrdscli
    ''',
)
