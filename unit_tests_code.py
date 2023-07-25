import ecgdetectors as Detectors
import pathlib
import numpy as np
import unittest


class Testecgdetectors(unittest.TestCase):
    def setUp(self):
        self.current_dir = pathlib.Path(__file__).resolve()
        self.experiment_dir = self.current_dir.parent / 'tests' / 'test_data' / 'experiment_data'
        self.fs = 250
        self.detectors = Detectors.Detectors(self.fs)

    def load_data(self, activity):
        subjects = list(self.experiment_dir.glob('subject*'))

        for subject_dir in subjects:
            activity_dir = subject_dir / activity
            ecg_file = activity_dir / 'ECG.tsv'
            annotation_file = activity_dir / 'annotation_cs.tsv'

            if ecg_file.exists() and annotation_file.exists():
                unfiltered_ecg_dat = np.loadtxt(ecg_file)
                example_answer_dat1 = np.loadtxt(annotation_file)
                example_answer_dat2 = example_answer_dat1.ravel()
                example_answer = example_answer_dat2.astype(int)
                unfiltered_ecg = unfiltered_ecg_dat[:, 0]
                return unfiltered_ecg, example_answer
        return None, None

    def test_two_average_detector(self):
        for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
            unfiltered_ecg, example_answer = self.load_data(activity)
            if unfiltered_ecg is not None:
                result = np.array(self.detectors.two_average_detector(unfiltered_ecg))
                self.assertAlmostEqual(result, example_answer)

    # def test_matched_filter_detector(self):
    #     for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
    #         unfiltered_ecg, example_answer = self.load_data(activity)
    #         if unfiltered_ecg is not None:
    #             result = np.array(
    #                 self.detectors.matched_filter_detector(unfiltered_ecg, "templates/template_250hz.csv"))
    #             self.assertAlmostEqual(result, example_answer)

    def test_swt_detector(self):
        for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
            unfiltered_ecg, example_answer = self.load_data(activity)
            if unfiltered_ecg is not None:
                result = np.array(self.detectors.two_average_detector(unfiltered_ecg))
                self.assertAlmostEqual(result, example_answer)

    def test_engzee_detector(self):
        for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
            unfiltered_ecg, example_answer = self.load_data(activity)
            if unfiltered_ecg is not None:
                result = np.array(self.detectors.engzee_detector(unfiltered_ecg))
                self.assertAlmostEqual(result, example_answer)

    def test_christov_detector(self):
        for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
            unfiltered_ecg, example_answer = self.load_data(activity)
            if unfiltered_ecg is not None:
                result = np.array(self.detectors.christov_detector(unfiltered_ecg))
                self.assertAlmostEqual(result, example_answer)

    def test_hamilton_detector(self):
        for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
            unfiltered_ecg, example_answer = self.load_data(activity)
            if unfiltered_ecg is not None:
                result = np.array(self.detectors.hamilton_detector(unfiltered_ecg))
                self.assertAlmostEqual(result, example_answer)

    def test_pan_tompkins_detector(self):
        for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
            unfiltered_ecg, example_answer = self.load_data(activity)
            if unfiltered_ecg is not None:
                result = np.array(self.detectors.pan_tompkins_detector(unfiltered_ecg))
                self.assertAlmostEqual(result, example_answer)

    def test_wqrs_detector(self):
        for activity in ['hand_bike', 'jogging', 'maths', 'sitting', 'walking']:
            unfiltered_ecg, example_answer = self.load_data(activity)
            if unfiltered_ecg is not None:
                result = np.array(self.detectors.wqrs_detector(unfiltered_ecg))
                self.assertAlmostEqual(result, example_answer)


if __name__ == '__main__':
    unittest.main()
