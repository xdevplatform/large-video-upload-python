from setuptools import setup

setup(
    name='twitter-async-video-upload',
    url='https://github.com/twitterdev/large-video-upload-python',
    version='0.1',
    description='Uploading large video files asynchronously with the Twitter API.',
    author='Twitter Dev',
    author_email='',
    license='MIT',
    packages=['twitter-async-video-upload'],
    install_requires=['oauthlib', 'requests', 'requests-oauthlib'],
)
