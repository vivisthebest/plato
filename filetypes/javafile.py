from filetypes.basefile import BaseFile
from filetypes.basetest import BaseTest
import filetypes
import prompt

from util import sprint, plural, COLOR_BLUE, COLOR_GREEN, COLOR_CYAN, \
                 COLOR_INVERTED, COLOR_RESET

import yaml

DEDUCTION_MODE_TYPES = prompt.PROMPT_MODES

def _print_file(path):
    f = open(path, 'rb')

    while True:
        c = f.read(1)
        if not c:
            break
        if c == '\r':
            continue
        if c == '\n':
            print()
            continue

        try:
            print(c.decode('utf-8'), end='')
        except UnicodeDecodeError:
            print(COLOR_INVERTED + '?' + COLOR_RESET, end='')



class JavaReviewTest(ReviewTest):
    def __init__(self, dict_, file_type):
        super().__init__(dict_, file_type)


class DiffTest(BaseTest):
    yaml_type = 'diff'

    def __init__(self, dict_, file_type):
        import os

        super().__init__(dict_, file_type)

        if not os.path.isfile(config.static_dir + os.sep + dict_['against']):
            raise ValueError("solution file for diff ('{}') "
                             "cannot be found".format(dict_['against']))

        self.against = config.static_dir + os.sep + dict_['against']


    def run(self, submission):
        import filecmp

        if filecmp.cmp(submission, self.against):
            return None
        else:
            return {'deduction': self.deduction,
                    'description': self.description,
                    'notes': ["files do not match"]}


class JavaFile(BaseFile):
    yaml_type = 'java'
    extensions = ['java']


class PlainFile(BaseFile):
    yaml_type = 'plain'
    extensions = ['txt']
    supported_tests = BaseFile.supported_tests.copy()
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
