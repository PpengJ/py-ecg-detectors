import unittest
import pathlib
import numpy as np
import sys
from testfile import qiuhe
from ecgdetectors import Detectors
import matplotlib.pyplot as plt

# 分别计算处理结果实际输出和预期输出数组的相邻元素之间的差值，并进行对比，若实际输出数组的差值在误差允许范围内，即可认为该探测器正常工作

class Testecgdetectors(unittest.TestCase):
    def test_init(self):
        current_dir = pathlib.Path(__file__).resolve()

        example_dir = current_dir.parent / 'test_data' / 'experiment_data' / 'subject_10' / 'walking' / 'ECG.tsv'
        example_answer_dir = current_dir.parent / 'test_data' / 'experiment_data' / 'subject_10' / 'walking' / 'annotation_cs.tsv'
        unfiltered_ecg_dat = np.loadtxt(example_dir)
        example_answer_dat1 = np.loadtxt(example_answer_dir)
        example_answer_dat2 = example_answer_dat1.ravel()
        example_answer_dat = example_answer_dat2.astype(int)
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]
        fs = 250

        detectors = Detectors(fs)
        r_peaks1 = detectors.two_average_detector(unfiltered_ecg)
        # r_peaks = detectors.matched_filter_detector(unfiltered_ecg,"templates/template_250hz.csv")
        # r_peaks = detectors.swt_detector(unfiltered_ecg)
        # r_peaks = detectors.engzee_detector(unfiltered_ecg)
        # r_peaks = detectors.christov_detector(unfiltered_ecg)
        # r_peaks = detectors.hamilton_detector(unfiltered_ecg)
        # r_peaks = detectors.pan_tompkins_detector(unfiltered_ecg)
        # r_peaks = np.array(detectors.wqrs_detector(unfiltered_ecg))

        # convert the sample number to time
        r_peaks = np.array(r_peaks1)
        r_ts = r_peaks / fs
        ex_r_ts = example_answer_dat / fs

        plt.figure()
        t = np.linspace(0, len(unfiltered_ecg) / fs, len(unfiltered_ecg))
        plt.plot(t, unfiltered_ecg)
        plt.plot(r_ts, unfiltered_ecg[r_peaks], 'o',color = 'gold')
        plt.plot(ex_r_ts, unfiltered_ecg[example_answer_dat], 'ro')
        plt.title("Detected R peaks")
        plt.ylabel("ECG/mV")
        plt.xlabel("time/sec")
        plt.show()

        intervals = np.diff(r_ts)
        heart_rate = 60.0 / intervals
        plt.figure()
        plt.plot(r_ts[1:], heart_rate)
        plt.title("Heart rate")
        plt.xlabel("time/sec")
        plt.ylabel("HR/BPM")
        plt.show()

        print(example_answer_dat)
        print('r_peaks are ',r_peaks)
        print(example_answer_dat.shape,r_peaks.shape)
        # self.assertEqual(r_peaks,example_answer_dat)
        np.testing.assert_array_equal(r_peaks,example_answer_dat)
