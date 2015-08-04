#!/usr/bin/env python

# Import modules.
# ---------------------------------------------------------
import Infiniivision

""" scope.py: Infiniivision 2000x/3000x acquisition program """

__author__ = "Sebastien Soudan"
__copyright__ = "Copyright 2013"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Sebastien Soudan"
__email__ = "sebastien.soudan@gmail.com"
__status__ = "Test"


# =========================================================
# Main program:
# =========================================================

# Initialize the oscilloscope, capture data, and analyze.
scope = Infiniivision.Infiniivision()
# scope.saveSetup("setup.stp")
scope.triggerEdge(Infiniivision.Channel1, 0)
scope.acquireMode(Infiniivision.NORMal)
scope.timebase(50e-3)
scope.timebaseOffset(0)
scope.single()
# scope.takeScreenshot()
scope.captureWaveform(Infiniivision.AllChannels, "waveform_data.csv", 2e4)
scope.run()
# scope.restoreSetup("setup.stp")
print "End of program."
