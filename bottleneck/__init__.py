
# If you bork the build (e.g. by messing around with the templates),
# you still want to be able to import Bottleneck so that you can
# rebuild using the templates. So try to import the compiled Bottleneck
# functions to the top level, but move on if not successful.
try:
    from func import nanmax, nanmin, nanmean, nanstd, nanvar, median
except:
    pass
try:
    from move import move_nanmean
except:
    pass
try:
    from group import group_nanmean
except:
    pass

from bottleneck.version import __version__
from bottleneck.bench.bench import *

try:
    from numpy.testing import Tester
    test = Tester().test
    del Tester
except (ImportError, ValueError):
    print "No Bottleneck unit testing available."