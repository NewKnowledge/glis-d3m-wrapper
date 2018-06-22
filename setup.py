from distutils.core import setup

setup(name='GlisD3MWrapper',
    version='1.0.0',
    description='A graph embedding package from New Knowledge',
    packages=['GlisD3MWrapper'],
    install_requires=["typing"],
    entry_points = {
        'd3m.primitives': [
            'distil.glis = GlisD3MWrapper:glis'
        ],
    },
)
