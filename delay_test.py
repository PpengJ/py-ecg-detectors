import pathlib
import numpy as np
from ecgdetectors import Detectors
import matplotlib.pyplot as plt

# 每个类型的探测器的处理结果与标准点每个点相减，计算出每个标点的实际与预期的差值，即为每个点的输出延迟
# 一共25*5*8=1000个处理结果，125个ECG文件，一共计算出1000个差值数组，对每个种类的探测器延迟取中位数，然后减去中位数延迟，从而提高R峰的标定精度

current_dir = pathlib.Path(__file__).resolve()

experiment_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data'

subjects = list(experiment_dir.glob('subject*'))

for subject_dir in subjects:
    for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
        activity_dir = subject_dir / activity

        ecg_file = activity_dir / 'ECG.tsv'
        annotation_file = activity_dir / 'annotation_cs.tsv'

        if ecg_file.exists() and annotation_file.exists():
            unfiltered_ecg_dat = np.loadtxt(ecg_file)
            example_answer_dat1 = np.loadtxt(annotation_file)
            example_answer_dat2 = example_answer_dat1.ravel()
            example_answer_dat = example_answer_dat2.astype(int)
            # 对数据进行处理

        unfiltered_ecg = unfiltered_ecg_dat[:, 0]
        fs = 250

        detectors = Detectors(fs)
        r_peaks = np.array(detectors.two_average_detector(unfiltered_ecg))
        # r_peaks = detectors.matched_filter_detector(unfiltered_ecg,"templates/template_250hz.csv")
        # r_peaks = detectors.swt_detector(unfiltered_ecg)
        # r_peaks = detectors.engzee_detector(unfiltered_ecg)
        # r_peaks = detectors.christov_detector(unfiltered_ecg)
        # r_peaks = detectors.hamilton_detector(unfiltered_ecg)
        # r_peaks = detectors.pan_tompkins_detector(unfiltered_ecg)
        # r_peaks = np.array(detectors.wqrs_detector(unfiltered_ecg))

        diff_array = np.array([])
        for i in range(min(len(example_answer_dat),len(r_peaks))):
            num = example_answer_dat[i] - r_peaks[i]
            diff_array = np.append(diff_array, num)

        # # convert the sample number to time
        # #r_peaks = np.array(r_peaks1)
        # r_ts = r_peaks / fs
        # ex_r_ts = example_answer_dat / fs
        #
        # plt.figure()
        # t = np.linspace(0, len(unfiltered_ecg) / fs, len(unfiltered_ecg))
        # plt.plot(t, unfiltered_ecg)
        # plt.plot(r_ts, unfiltered_ecg[r_peaks], 'o',color = 'gold')
        # plt.plot(ex_r_ts, unfiltered_ecg[example_answer_dat], 'ro')
        # plt.title("Detected R peaks")
        # plt.ylabel("ECG/mV")
        # plt.xlabel("time/sec")
        # plt.show()
        #
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
        # print(example_answer_dat.shape,r_peaks.shape)
        print(diff_array)
        # # self.assertEqual(r_peaks,example_answer_dat)
        # np.testing.assert_array_equal(r_peaks,example_answer_dat)