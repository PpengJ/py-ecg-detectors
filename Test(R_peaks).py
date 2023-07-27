import ecgdetectors as Detectors
import pathlib
import numpy as np
import unittest

class Testecgdetectors(unittest.TestCase):
    def setUp(self):
        self.fs = 250
        self.detectors = Detectors.Detectors(self.fs)

    # 1.Test for two average detector
    def test_two_average_detector(self):
        current_dir = pathlib.Path(__file__).resolve()
        example_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_20' / 'sitting' / 'ECG.tsv'
        example_answer_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_20' / 'sitting' / 'annotation_cs.tsv'
        unfiltered_ecg_dat = np.loadtxt(example_dir)
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]
        example_answer_dat1 = np.loadtxt(example_answer_dir)
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
        current_dir = pathlib.Path(__file__).resolve()

        example_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_00' / 'jogging' / 'ECG.tsv'
        example_answer_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_00' / 'jogging' / 'annotation_cs.tsv'

        unfiltered_ecg_dat = np.loadtxt(example_dir)
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = np.loadtxt(example_answer_dir)
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
        current_dir = pathlib.Path(__file__).resolve()

        example_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_06' / 'sitting' / 'ECG.tsv'
        example_answer_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_06' / 'sitting' / 'annotation_cs.tsv'

        unfiltered_ecg_dat = np.loadtxt(example_dir)
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = np.loadtxt(example_answer_dir)
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
        current_dir = pathlib.Path(__file__).resolve()

        example_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_03' / 'jogging' / 'ECG.tsv'
        example_answer_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_03' / 'jogging' / 'annotation_cs.tsv'

        unfiltered_ecg_dat = np.loadtxt(example_dir)
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = np.loadtxt(example_answer_dir)
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
        current_dir = pathlib.Path(__file__).resolve()

        example_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_20' / 'sitting' / 'ECG.tsv'
        example_answer_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_20' / 'sitting' / 'annotation_cs.tsv'

        unfiltered_ecg_dat = np.loadtxt(example_dir)
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = np.loadtxt(example_answer_dir)
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
        current_dir = pathlib.Path(__file__).resolve()

        example_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_20' / 'sitting' / 'ECG.tsv'
        example_answer_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_20' / 'sitting' / 'annotation_cs.tsv'

        unfiltered_ecg_dat = np.loadtxt(example_dir)
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = np.loadtxt(example_answer_dir)
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
        current_dir = pathlib.Path(__file__).resolve()

        example_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_08' / 'maths' / 'ECG.tsv'
        example_answer_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_08' / 'maths' / 'annotation_cs.tsv'

        unfiltered_ecg_dat = np.loadtxt(example_dir)
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = np.loadtxt(example_answer_dir)
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
        current_dir = pathlib.Path(__file__).resolve()

        example_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_22' / 'sitting' / 'ECG.tsv'
        example_answer_dir = current_dir.parent / 'tests' / 'test_data' / 'experiment_data' / 'subject_22' / 'sitting' / 'annotation_cs.tsv'

        unfiltered_ecg_dat = np.loadtxt(example_dir)
        unfiltered_ecg = unfiltered_ecg_dat[:, 0]

        example_answer_dat1 = np.loadtxt(example_answer_dir)
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