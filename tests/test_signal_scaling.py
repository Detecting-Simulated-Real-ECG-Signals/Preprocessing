from defibrilator_preprocessing.signal_scaling import threshold_scale, clip_signal
import unittest
import numpy as np


class TestThresholdScale(unittest.TestCase):
    def test_thresholds(self):
        scaled = threshold_scale(np.array([0, 1]), 0, 1)
        self.assertEqual(scaled, np.array(0, 1))

    def test_upper_threshold(self):
        scaled = threshold_scale(np.array([0, 2]), 0, 1)
        self.assertTrue(scaled[0] == 0)
        self.assertTrue(scaled[1] > 1)

    def test_lower_threshold(self):
        scaled = threshold_scale(np.array([-1, 1]), 0, 1)
        self.assertTrue(scaled[0] < 0)
        self.assertTrue(scaled[1] == 1)


class TestClipSignal(unittest.TestCase):
    def test_thresholds(self):
        scaled = clip_signal(np.array([-1, 0, 1, 2]), 0, 1)
        self.assertEqual(scaled, np.array(0, 0, 1, 1))
