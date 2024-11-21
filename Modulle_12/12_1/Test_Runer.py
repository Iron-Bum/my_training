from Runer import Runner
from unittest import TestCase
from unittest import main


class RunnerTest(TestCase):
    def test_walk(self):
        test_obj = Runner('test')
        for _ in range(10):
            test_obj.walk()
        self.assertEqual(test_obj.distance, 50)

    def test_run(self):
        test_obj = Runner('test')
        for _ in range(10):
            test_obj.run()
        self.assertEqual(test_obj.distance, 100)

    def test_challenge(self):
        test_obj_1 = Runner('test1')
        test_obj_2 = Runner('test2')
        for _ in range(10):
            test_obj_1.run()
            test_obj_2.walk()
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)


if __name__ == '__main__':
    main()
