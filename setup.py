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
        'psycopg2-binary>=2.8.3',
        'psycopg2>=2.7.6',
        'attrs>=19.2.0',
        'influxdb>=5.2.3',
        'pyyaml>=5.1.2',
        'cached-property~=1.5.1;python_version<"3.8"',
    ],
    python_requires='>=3.7.4',
    entry_points='''
        [console_scripts]
        wrdscli=wrdscli.wrdscli:wrdscli
    ''',
)
