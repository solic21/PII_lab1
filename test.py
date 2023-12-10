import unittest
import csv

import model
import inference_mamdani


class TestAll(unittest.TestCase):

    def test_all(self):
        with open('data.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                crisp = list(map(lambda x:float(x), row[:-1]))
                word_expected = row[-1]
                with self.subTest(crisp = crisp, word_expected=word_expected):
                    result, _ = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp)
                    self.assertEqual(result[1], word_expected)

