import mymodule

mymodule.feriehvornår()

import mymodule as m

m.qouteoftheday()

from contextlib import contextmanager


@contextmanager
def openfile(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

    with openfile('demo') as f:
        f.write("se hvad jeg har hentet")
