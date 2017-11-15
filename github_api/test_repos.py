import unittest
from python_repos import *

"""测试status_code"""


class TestPythonRepos(unittest.TestCase):
	def test_status_code(self):
		self.assertEqual(200, r.status_code)


if __name__ == '__main__':
	unittest.main()()
