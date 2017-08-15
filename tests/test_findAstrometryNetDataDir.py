
from __future__ import division, print_function, absolute_import

import os
import unittest

import lsst.utils.tests


def setupAstrometryNetDataDir(name, rootDir=None, verbose=False):
    """Locate the named Astrometry.net data directory from within
    the current tree, relative to this file, or relative to the supplied
    root directory.

    Returns the located data directory and sets the ASTROMETRY_NET_DATA_DIR
    environment variable.
    """
    if rootDir is None:
        rootDir = os.path.dirname(__file__)
    else:
        rootDir = os.path.abspath(rootDir)
    datapath = os.path.join(rootDir, 'astrometry_net_data', name)
    if not os.path.exists(datapath):
        raise ValueError("Need {} version of astrometry_net_data (from path: {})".format(name, datapath))
    if verbose:
        print('Setting up astrometry_net_data: {}'.format(datapath))
    os.environ["ASTROMETRY_NET_DATA_DIR"] = datapath
    return datapath


class TestAstrometryNetDataDirDiscovery(unittest.TestCase):

    def test_photocal(self):
        datapath = setupAstrometryNetDataDir('t2155')
        self.assertEqual(os.environ["ASTROMETRY_NET_DATA_DIR"], datapath)


def setup_module(module):
    lsst.utils.tests.init()


class MatchMemoryTestCase(lsst.utils.tests.MemoryTestCase):
    pass


if __name__ == "__main__":
    lsst.utils.tests.init()
    unittest.main()
