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

        experiment_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data'

        subjects = list(experiment_dir.glob('subject*'))

        diff_of_one_detector1 = np.array([])
        diff_of_one_detector2 = np.array([])
        diff_of_one_detector3 = np.array([])
        diff_of_one_detector4 = np.array([])
        diff_of_one_detector5 = np.array([])
        diff_of_one_detector6 = np.array([])
        diff_of_one_detector7 = np.array([])
        diff_of_one_detector8 = np.array([])

        for subject_dir in subjects:
            for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
                activity_dir = subject_dir / activity

                ecg_file = activity_dir / 'ECG.tsv'
                annotation_file = activity_dir / 'annotation_cs.tsv'

                if ecg_file.exists() and annotation_file.exists():
                    unfiltered_ecg_dat = np.loadtxt(ecg_file)
                    example_answer_dat1 = np.loadtxt(annotation_file)
                    example_answer_dat2 = example_answer_dat1.ravel()
                    example_answer = example_answer_dat2.astype(int)

                # 对数据进行处理
                unfiltered_ecg = unfiltered_ecg_dat[:, 0]
                # fs = 250

        detectors = Detectors(250)
        # r_peaks1 = detectors.two_average_detector(unfiltered_ecg)
        # r_peaks = detectors.matched_filter_detector(unfiltered_ecg,"templates/template_250hz.csv")
        # r_peaks = detectors.swt_detector(unfiltered_ecg)
        # r_peaks = detectors.engzee_detector(unfiltered_ecg)
        # r_peaks = detectors.christov_detector(unfiltered_ecg)
        # r_peaks = detectors.hamilton_detector(unfiltered_ecg)
        # r_peaks = detectors.pan_tompkins_detector(unfiltered_ecg)
        r_peaks = np.array(detectors.wqrs_detector(unfiltered_ecg))

        print(len(r_peaks))


