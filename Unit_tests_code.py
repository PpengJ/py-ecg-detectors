import ecgdetectors as Detectors
import numpy as np
import unittest
from Unit_test_data.arrays import two_average_detector_test_ecg,two_average_detector_test_ecg_answer
from Unit_test_data.arrays import matched_filter_detector_test_ecg,matched_filter_detector_test_ecg_answer
from Unit_test_data.arrays import swt_detector_test_ecg,swt_detector_test_ecg_answer
from Unit_test_data.arrays import engzee_detector_test_ecg,engzee_detector_test_ecg_answer
from Unit_test_data.arrays import christov_detector_test_ecg,christov_detector_test_ecg_answer
from Unit_test_data.arrays import hamilton_detector_test_ecg,hamilton_detector_test_ecg_answer
from Unit_test_data.arrays import pan_tompkins_detector_test_ecg,pan_tompkins_detector_test_ecg_answer
from Unit_test_data.arrays import wqrs_detector_test_ecg,wqrs_detector_test_ecg_answer

class Testecgdetectors(unittest.TestCase):
    def setUp(self):
        self.fs = 250
        self.detectors = Detectors.Detectors(self.fs)

    # 1.Test for two average detector
    def test_two_average_detector(self):
        unfiltered_ecg_dat = two_average_detector_test_ecg
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]
        example_answer_dat1 = two_average_detector_test_ecg_answer
        example_answer_dat2 = example_answer_dat1.ravel()
        example_answer = example_answer_dat2.astype(int)

        if unfiltered_ecg is not None:
            result = np.array(self.detectors.two_average_detector(unfiltered_ecg))
            example_answer_dat = example_answer

            to_delete_from_result = []
            to_delete_from_example = []
            # print(len(result),len(example_answer_dat))
            for i in range(min(len(example_answer_dat), len(result))):
                standard_value = 0.068 * 250
                diff = result[i] - example_answer_dat[i]
                if (diff > standard_value * 1.2) or (diff < standard_value * 0.8):
                    if i > 0:
                        if len(example_answer_dat) > len(result):
                            to_delete_from_example.append(i)
                        if len(example_answer_dat) < len(result):
                            to_delete_from_result.append(i)

            result = np.delete(result, to_delete_from_result)
            example_answer_dat = np.delete(example_answer_dat, to_delete_from_example)

            result = result - standard_value
            result = result.astype(int)
            np.allclose(result, example_answer_dat,rtol=0.001)

    # 2.Test for matched filter detector
    def test_matched_filter_detector(self):
        unfiltered_ecg_dat = matched_filter_detector_test_ecg
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]
        example_answer_dat1 = matched_filter_detector_test_ecg_answer
        example_answer_dat2 = example_answer_dat1.ravel()
        example_answer = example_answer_dat2.astype(int)

        if unfiltered_ecg is not None:
            result = np.array(self.detectors.matched_filter_detector(unfiltered_ecg))
            example_answer_dat = example_answer

            to_delete_from_result = []
            to_delete_from_example = []
            # print(len(result),len(example_answer_dat))
            for i in range(min(len(example_answer_dat), len(result))):
                standard_value = 0.104 * 250
                diff = result[i] - example_answer_dat[i]
                if (diff > standard_value * 1.2) or (diff < standard_value * 0.8):
                    if i > 0:
                        if len(example_answer_dat) > len(result):
                            to_delete_from_example.append(i)
                        if len(example_answer_dat) < len(result):
                            to_delete_from_result.append(i)

            result = np.delete(result, to_delete_from_result)
            example_answer_dat = np.delete(example_answer_dat, to_delete_from_example)

            result = result - standard_value
            result = result.astype(int)
            np.allclose(result, example_answer_dat,rtol=0.001)

    # 3.Test for swt_detector
    def test_swt_detector(self):
        unfiltered_ecg_dat = swt_detector_test_ecg
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]
        example_answer_dat1 = swt_detector_test_ecg_answer
        example_answer_dat2 = example_answer_dat1.ravel()
        example_answer = example_answer_dat2.astype(int)

        if unfiltered_ecg is not None:
            result = np.array(self.detectors.swt_detector(unfiltered_ecg))
            example_answer_dat = example_answer

            to_delete_from_result = []
            to_delete_from_example = []
            # print(len(result),len(example_answer_dat))
            for i in range(min(len(example_answer_dat), len(result))):
                standard_value = 0.032 * 250
                diff = result[i] - example_answer_dat[i]
                if (diff > standard_value * 1.2) or (diff < standard_value * 0.8):
                    if i > 0:
                        if len(example_answer_dat) > len(result):
                            to_delete_from_example.append(i)
                        if len(example_answer_dat) < len(result):
                            to_delete_from_result.append(i)

            result = np.delete(result, to_delete_from_result)
            example_answer_dat = np.delete(example_answer_dat, to_delete_from_example)

            result = result - standard_value
            result = result.astype(int)
            np.allclose(result, example_answer_dat,rtol=0.001)

    # 4.Test for engzee_detector
    def test_engzee_detector(self):
        unfiltered_ecg_dat = engzee_detector_test_ecg
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = engzee_detector_test_ecg_answer
        example_answer_dat2 = example_answer_dat1.ravel()
        example_answer = example_answer_dat2.astype(int)

        if unfiltered_ecg is not None:
            result = np.array(self.detectors.engzee_detector(unfiltered_ecg))
            example_answer_dat = example_answer

            to_delete_from_result = []
            to_delete_from_example = []
            # print(len(result),len(example_answer_dat))
            for i in range(min(len(example_answer_dat), len(result))):
                standard_value = 0.604 * 250
                diff = result[i] - example_answer_dat[i]
                if (diff > standard_value * 1.2) or (diff < standard_value * 0.8):
                    if i > 0:
                        if len(example_answer_dat) > len(result):
                            to_delete_from_example.append(i)
                        if len(example_answer_dat) < len(result):
                            to_delete_from_result.append(i)

            result = np.delete(result, to_delete_from_result)
            example_answer_dat = np.delete(example_answer_dat, to_delete_from_example)

            result = result - standard_value
            result = result.astype(int)
            np.allclose(result, example_answer_dat,rtol=0.001)

    # 5.Test for christov_detector
    def test_christov_detector(self):
        unfiltered_ecg_dat = christov_detector_test_ecg
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = christov_detector_test_ecg_answer
        example_answer_dat2 = example_answer_dat1.ravel()
        example_answer = example_answer_dat2.astype(int)

        if unfiltered_ecg is not None:
            result = np.array(self.detectors.christov_detector(unfiltered_ecg))
            example_answer_dat = example_answer

            to_delete_from_result = []
            to_delete_from_example = []
            # print(len(result),len(example_answer_dat))
            for i in range(min(len(example_answer_dat), len(result))):
                standard_value = 0.004 * 250
                diff = result[i] - example_answer_dat[i]
                if (diff > standard_value * 1.2) or (diff < standard_value * 0.8):
                    if i > 0:
                        if len(example_answer_dat) > len(result):
                            to_delete_from_example.append(i)
                        if len(example_answer_dat) < len(result):
                            to_delete_from_result.append(i)

            result = np.delete(result, to_delete_from_result)
            example_answer_dat = np.delete(example_answer_dat, to_delete_from_example)

            result = result - standard_value
            result = result.astype(int)
            np.allclose(result, example_answer_dat,rtol=0.001)

    # 6.Test for hamilton_detecto
    def test_hamilton_detector(self):
        unfiltered_ecg_dat = hamilton_detector_test_ecg
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = hamilton_detector_test_ecg_answer
        example_answer_dat2 = example_answer_dat1.ravel()
        example_answer = example_answer_dat2.astype(int)

        if unfiltered_ecg is not None:
            result = np.array(self.detectors.hamilton_detector(unfiltered_ecg))
            example_answer_dat = example_answer

            to_delete_from_result = []
            to_delete_from_example = []
            # print(len(result),len(example_answer_dat))
            for i in range(min(len(example_answer_dat), len(result))):
                standard_value = 0.06 * 250
                diff = result[i] - example_answer_dat[i]
                if (diff > standard_value * 1.2) or (diff < standard_value * 0.8):
                    if i > 0:
                        if len(example_answer_dat) > len(result):
                            to_delete_from_example.append(i)
                        if len(example_answer_dat) < len(result):
                            to_delete_from_result.append(i)

            result = np.delete(result, to_delete_from_result)
            example_answer_dat = np.delete(example_answer_dat, to_delete_from_example)

            result = result - standard_value
            result = result.astype(int)
            np.allclose(result, example_answer_dat,rtol=0.001)

    # 7.Test for pan_tompkins_detector
    def test_pan_tompkins_detector(self):
        unfiltered_ecg_dat = pan_tompkins_detector_test_ecg
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = pan_tompkins_detector_test_ecg_answer
        example_answer_dat2 = example_answer_dat1.ravel()
        example_answer = example_answer_dat2.astype(int)

        if unfiltered_ecg is not None:
            result = np.array(self.detectors.pan_tompkins_detector(unfiltered_ecg))
            example_answer_dat = example_answer

            to_delete_from_result = []
            to_delete_from_example = []
            # print(len(result),len(example_answer_dat))
            for i in range(min(len(example_answer_dat), len(result))):
                standard_value = 0.04 * 250
                diff = result[i] - example_answer_dat[i]
                if (diff > standard_value * 1.2) or (diff < standard_value * 0.8):
                    if i > 0:
                        if len(example_answer_dat) > len(result):
                            to_delete_from_example.append(i)
                        if len(example_answer_dat) < len(result):
                            to_delete_from_result.append(i)

            result = np.delete(result, to_delete_from_result)
            example_answer_dat = np.delete(example_answer_dat, to_delete_from_example)

            result = result - standard_value
            result = result.astype(int)
            np.allclose(result, example_answer_dat,rtol=0.001)

    # 8.Test for wqrs_detector
    def test_wqrs_detector(self):
        unfiltered_ecg_dat = wqrs_detector_test_ecg
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = wqrs_detector_test_ecg_answer
        example_answer_dat2 = example_answer_dat1.ravel()
        example_answer = example_answer_dat2.astype(int)

        if unfiltered_ecg is not None:
            result = np.array(self.detectors.wqrs_detector(unfiltered_ecg))
            example_answer_dat = example_answer

            to_delete_from_result = []
            to_delete_from_example = []
            # print(len(result),len(example_answer_dat))
            for i in range(min(len(example_answer_dat), len(result))):
                standard_value = 0.012 * 250
                diff = result[i] - example_answer_dat[i]
                if (diff > standard_value * 1.2) or (diff < standard_value * 0.8):
                    if i > 0:
                        if len(example_answer_dat) > len(result):
                            to_delete_from_example.append(i)
                        if len(example_answer_dat) < len(result):
                            to_delete_from_result.append(i)

            result = np.delete(result, to_delete_from_result)
            example_answer_dat = np.delete(example_answer_dat, to_delete_from_example)

            standard_value = 0.012 * 250
            result = result - standard_value
            result = result.astype(int)
            np.allclose(result, example_answer_dat,rtol=0.001)

if __name__ == '__main__':
    unittest.main()