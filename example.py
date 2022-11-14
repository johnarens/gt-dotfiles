import numpy as np # noqa

x = 10

if (x == 10):
    x += 1
else:
    x = 0

y = np.arange(1, 10)
# this is a really long comment that is too long for the requirement in PEP8.  When asdfasdfasdfadfadsfasdfasdfasfd # noqa
# this is a really long comment that is too long for the requirement in PEP8.  When asdfasdfasdfadfadsfasdfasdfasfd 
z = 10


long_var_name = 10
long_var_name = 20

long_var_name = 50
long_var_name = 25

# asdadfafddff asdfadfdasf


class xyz:
    """Docstring."""

    def __init__(self, x):
        """Perform initialization."""
        self.x = x

    def dostuff(self, x):
        """Do stuff."""
        y = x + 1
        return y
