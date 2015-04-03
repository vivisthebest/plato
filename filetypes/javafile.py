from filetypes.basefile import BaseFile
from filetypes.basetest import BaseTest
import filetypes
import prompt

from util import sprint, plural, COLOR_BLUE, COLOR_GREEN, COLOR_CYAN, \
                 COLOR_INVERTED, COLOR_RESET

import yaml

DEDUCTION_MODE_TYPES = prompt.PROMPT_MODES


class JavaFile(PlainFile):
    yaml_type = 'java'
    extensions = ['java']
    supported_tests = PlainFile.supported_tests.copy()
    supported_tests.append()

class PlainFile(BaseFile):
    yaml_type = 'plain'
    extensions = ['txt']
    
    supported_tests.append(DiffTest)
    supported_tests.append(ReviewTest)

    def __init__(self, dict_):
        BaseFile.__init__(self, dict_)

        if 'tests' in dict_:
            for t in dict_['tests']:
                test_cls = filetypes.find_test_class(PlainFile.yaml_type,
                                                     t['type'])
                self.tests.append(test_cls(t, PlainFile.yaml_type))


    def run_tests(self):
        results = []
        for t in self.tests:
            result = t.run(self.path)

            if result:
                if type(result) is list:
                    for r in result:
                        results.append(r)
                else:
                    results.append(result)

        return results



    def __str__(self):
        return self.path + " (java file)"
