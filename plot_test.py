import pathlib
import numpy as np
from ecgdetectors import Detectors
import matplotlib.pyplot as plt

current_dir = pathlib.Path(__file__).resolve()

experiment_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data'

subjects = list(experiment_dir.glob('subject*'))


diff_of_one_detector5 = np.array([])


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
        fs = 250

        detectors = Detectors(fs)

        r_peaks5 = np.array(detectors.christov_detector(unfiltered_ecg))





        # # convert the sample number to time
        # #r_peaks = np.array(r_peaks1)
        r_ts = r_peaks5 / fs - 0.004
        ex_r_ts = example_answer / fs

        r_peaks5 = r_peaks5 - 0.004*250
        r_peaks5 = r_peaks5.astype(int)

        # print(x)
        # print(example_answer_dat)
        # print(len(unfiltered_ecg))
        # print(len(r_ts))
        # print(diff_array)
        # print(r_peaks)

        plt.figure()
        t = np.linspace(0, len(unfiltered_ecg) / fs, len(unfiltered_ecg))
        plt.plot(t, unfiltered_ecg)
        plt.plot(r_ts, unfiltered_ecg[r_peaks5], 'o',color = 'gold')
        plt.plot(ex_r_ts, unfiltered_ecg[example_answer], 'ro')
        plt.title("Detected R peaks")
        plt.ylabel("ECG/mV")
        plt.xlabel("time/sec")
        plt.show()

        # intervals = np.diff(r_ts)
        # heart_rate = 60.0 / intervals
        # plt.figure()
        # plt.plot(r_ts[1:], heart_rate)
        # plt.title("Heart rate")
        # plt.xlabel("time/sec")
        # plt.ylabel("HR/BPM")
        # plt.show()
        #

        # print(example_answer_dat)
        # print('r_peaks are ',r_peaks)
        print(example_answer.shape, r_peaks5.shape)
        # print(diff_array)

        # # self.assertEqual(r_peaks,example_answer_dat)
        # np.testing.assert_array_equal(r_peaks,example_answer_dat)