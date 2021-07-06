from setuptools import setup
setup(
    name='firebase_rtdb_pagination',
    packages=['firebase_rtdb_pagination'],
    version='1.0.1',
    license='MIT',
    description='Firebase Realtime DB Pagination',
    author='Jay Milagroso',
    author_email='j.milagroso@gmail.com',
    url='https://github.com/jmilagroso/firebase_rtdb_pagination',
    download_url='https://github.com/jmilagroso/firebase_rtdb_pagination/archive/refs/tags/1.0.1tar.gz',
    keywords=[
        'Firebase',
        'RealtimeDB',
        'Pagination'],
    install_requires=['firebase-admin'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
