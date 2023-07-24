import pathlib
import numpy as np
from ecgdetectors import Detectors
import matplotlib.pyplot as plt

# 每个类型的探测器的处理结果与标准点每个点相减，计算出每个标点的实际与预期的差值，即为每个点的输出延迟
# 一共25*5*8=1000个处理结果，125个ECG文件，一共计算出1000个差值数组，对每个种类的探测器延迟取中位数，然后减去中位数延迟，从而提高R峰的标定精度

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
        fs = 250

        detectors = Detectors(fs)
        r_peaks1 = np.array(detectors.two_average_detector(unfiltered_ecg))
        # r_peaks2 = detectors.matched_filter_detector(unfiltered_ecg,"templates/template_250hz.csv")
        r_peaks3 = np.array(detectors.swt_detector(unfiltered_ecg))
        r_peaks4 = np.array(detectors.engzee_detector(unfiltered_ecg))
        r_peaks5 = np.array(detectors.christov_detector(unfiltered_ecg))
        r_peaks6 = np.array(detectors.hamilton_detector(unfiltered_ecg))
        r_peaks7 = np.array(detectors.pan_tompkins_detector(unfiltered_ecg))
        r_peaks8 = np.array(detectors.wqrs_detector(unfiltered_ecg))

        # 计算实际输出和预期输出的数组元素之间的差值
        # To do: 一般两个数组的第一个元素之间的差值可以作为该组结果差值的参照标准，
        #        因此如果中间某一组差值突然变大，则舍弃这个结果，并跳过元素数量较多的那个数组的该index对应的元素

        # 1.delay array of two_average_detector
        example_answer_dat = example_answer
        diff_list1 = [(r_peaks1[0] - example_answer_dat[0]) / 250]
        for i in range(min(len(example_answer_dat), len(r_peaks1))):
            num = (r_peaks1[i] - example_answer_dat[i]) / 250
            if (num > diff_list1[0] * 1.2) or (num < diff_list1[0] * 0.8):
                if i > 0:
                    if len(example_answer_dat) > len(r_peaks1):
                        example_answer_dat = np.delete(example_answer_dat, i)
                    if len(example_answer_dat) < len(r_peaks1):
                        r_peaks1 = np.delete(r_peaks1, i)
                num = (r_peaks1[i] - example_answer_dat[i]) / 250
            diff_list1.append(num)
        diff_array1 = np.array(diff_list1)
        diff_array1 = np.delete(diff_array1, 0)

        # # 2.delay array of matched_filter_detector
        # example_answer_dat = example_answer
        # diff_list2 = [(r_peaks2[0] - example_answer_dat[0]) / 250]
        # for i in range(min(len(example_answer_dat), len(r_peaks2))):
        #     num = (r_peaks2[i] - example_answer_dat[i]) / 250
        #     if ((num > diff_list2[0] * 1.2) or (num < diff_list2[0] * 0.8)):
        #         if i > 0:
        #             if len(example_answer_dat) > len(r_peaks2):
        #                 example_answer_dat = np.delete(example_answer_dat, i)
        #             if len(example_answer_dat) < len(r_peaks2):
        #                 r_peaks2 = np.delete(r_peaks2, i)
        #         num = (r_peaks2[i] - example_answer_dat[i]) / 250
        #     diff_list2.append(num)
        # diff_array2 = np.array(diff_list2)
        # diff_array2 = np.delete(diff_array2, 0)

        # 3.delay array of swt_detector
        example_answer_dat = example_answer
        diff_list3 = [(r_peaks3[0] - example_answer_dat[0]) / 250]
        for i in range(min(len(example_answer_dat), len(r_peaks3))):
            num = (r_peaks3[i] - example_answer_dat[i]) / 250
            if ((num > diff_list3[0] * 1.2) or (num < diff_list3[0] * 0.8)):
                if i > 0:
                    if len(example_answer_dat) > len(r_peaks3):
                        example_answer_dat = np.delete(example_answer_dat, i)
                    if len(example_answer_dat) < len(r_peaks3):
                        r_peaks3 = np.delete(r_peaks3, i)
                num = (r_peaks3[i] - example_answer_dat[i]) / 250
            diff_list3.append(num)
        diff_array3 = np.array(diff_list3)
        diff_array3 = np.delete(diff_array3, 0)

        # 4.delay array of engzee_detector
        example_answer_dat = example_answer
        diff_list4 = [(r_peaks4[0] - example_answer_dat[0]) / 250]
        for i in range(min(len(example_answer_dat), len(r_peaks4))):
            num = (r_peaks4[i] - example_answer_dat[i]) / 250
            if ((num > diff_list4[0] * 1.2) or (num < diff_list4[0] * 0.8)):
                if i > 0:
                    if len(example_answer_dat) > len(r_peaks4):
                        example_answer_dat = np.delete(example_answer_dat, i)
                    if len(example_answer_dat) < len(r_peaks4):
                        r_peaks4 = np.delete(r_peaks4, i)
                num = (r_peaks4[i] - example_answer_dat[i]) / 250
            diff_list4.append(num)
        diff_array4 = np.array(diff_list4)
        diff_array4 = np.delete(diff_array4, 0)

        # 5.delay array of christov_detector
        example_answer_dat = example_answer
        diff_list5 = [(r_peaks5[0] - example_answer_dat[0]) / 250]
        for i in range(min(len(example_answer_dat), len(r_peaks5))):
            num = (r_peaks5[i] - example_answer_dat[i]) / 250
            if ((num > diff_list5[0] * 1.2) or (num < diff_list5[0] * 0.8)):
                if i > 0:
                    if len(example_answer_dat) > len(r_peaks5):
                        example_answer_dat = np.delete(example_answer_dat, i)
                    if len(example_answer_dat) < len(r_peaks5):
                        r_peaks5 = np.delete(r_peaks5, i)
                num = (r_peaks5[i] - example_answer_dat[i]) / 250
            diff_list5.append(num)
        diff_array5 = np.array(diff_list5)
        diff_array5 = np.delete(diff_array5, 0)

        # 6.delay array of hamilton_detector
        example_answer_dat = example_answer
        diff_list6 = [(r_peaks6[0] - example_answer_dat[0]) / 250]
        for i in range(min(len(example_answer_dat), len(r_peaks6))):
            num = (r_peaks6[i] - example_answer_dat[i]) / 250
            if ((num > diff_list6[0] * 1.2) or (num < diff_list6[0] * 0.8)):
                if i > 0:
                    if len(example_answer_dat) > len(r_peaks6):
                        example_answer_dat = np.delete(example_answer_dat, i)
                    if len(example_answer_dat) < len(r_peaks6):
                        r_peaks6 = np.delete(r_peaks6, i)
                num = (r_peaks6[i] - example_answer_dat[i]) / 250
            diff_list6.append(num)
        diff_array6 = np.array(diff_list6)
        diff_array6 = np.delete(diff_array6, 0)

        # 7.delay array of pan_tompkins_detector
        example_answer_dat = example_answer
        diff_list7 = [(r_peaks7[0] - example_answer_dat[0]) / 250]
        for i in range(min(len(example_answer_dat), len(r_peaks7))):
            num = (r_peaks7[i] - example_answer_dat[i]) / 250
            if ((num > diff_list7[0] * 1.2) or (num < diff_list7[0] * 0.8)):
                if i > 0:
                    if len(example_answer_dat) > len(r_peaks7):
                        example_answer_dat = np.delete(example_answer_dat, i)
                    if len(example_answer_dat) < len(r_peaks7):
                        r_peaks7 = np.delete(r_peaks7, i)
                num = (r_peaks7[i] - example_answer_dat[i]) / 250
            diff_list7.append(num)
        diff_array7 = np.array(diff_list7)
        diff_array7 = np.delete(diff_array7, 0)

        # 8.delay array of wqrs_detector
        example_answer_dat = example_answer
        diff_list8 = [(r_peaks8[0] - example_answer_dat[0]) / 250]
        for i in range(min(len(example_answer_dat), len(r_peaks8))):
            num = (r_peaks8[i] - example_answer_dat[i]) / 250
            if ((num > diff_list8[0] * 1.2) or (num < diff_list8[0] * 0.8)):
                if i > 0:
                    if len(example_answer_dat) > len(r_peaks8):
                        example_answer_dat = np.delete(example_answer_dat, i)
                    if len(example_answer_dat) < len(r_peaks8):
                        r_peaks8 = np.delete(r_peaks8, i)
                num = (r_peaks8[i] - example_answer_dat[i]) / 250
            diff_list8.append(num)
        diff_array8 = np.array(diff_list8)
        diff_array8 = np.delete(diff_array8, 0)

    diff_of_one_detector1 = np.append(diff_of_one_detector1, diff_array1)
    # diff_of_one_detector2 = np.append(diff_of_one_detector2, diff_array2)
    diff_of_one_detector3 = np.append(diff_of_one_detector3, diff_array3)
    diff_of_one_detector4 = np.append(diff_of_one_detector4, diff_array4)
    diff_of_one_detector5 = np.append(diff_of_one_detector5, diff_array5)
    diff_of_one_detector6 = np.append(diff_of_one_detector6, diff_array6)
    diff_of_one_detector7 = np.append(diff_of_one_detector7, diff_array7)
    diff_of_one_detector8 = np.append(diff_of_one_detector8, diff_array8)

delta1 = np.median(diff_of_one_detector1)
# delta2 = np.median(diff_of_one_detector2)
delta3 = np.median(diff_of_one_detector3)
delta4 = np.median(diff_of_one_detector4)
delta5 = np.median(diff_of_one_detector5)
delta6 = np.median(diff_of_one_detector6)
delta7 = np.median(diff_of_one_detector7)
delta8 = np.median(diff_of_one_detector8)
print('Delta of two_average_detector is:', delta1)
# print('Delta of matched_filter_detector is:', delta2)
print('Delta of swt_detector is:', delta3)
print('Delta of engzee_detector is:', delta4)
print('Delta of christov_detector is:', delta5)
print('Delta of hamilton_detector is:', delta6)
print('Delta of pan_tompkins_detector is:', delta7)
print('Delta of wqrs_detector is:', delta8)
