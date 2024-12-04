import logging
import unittest

from Modulle_12.m_12_1.Runer import Runner
from unittest import TestCase
from unittest import main


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_obj = Runner('test', -7)
            logging.info('test_walk" выполнен успешно')
            for _ in range(10):
                test_obj.walk()
            self.assertEqual(test_obj.distance, 100)
        except ValueError:
            logging.warning('"Неверная скорость для Runner"')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_obj = Runner(40, 13)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                test_obj.run()
            self.assertEqual(test_obj.distance, 260)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_obj_1 = Runner('test1')
        test_obj_2 = Runner('test2')
        for _ in range(10):
            test_obj_1.run()
            test_obj_2.walk()
        self.assertNotEqual(test_obj_1.distance, test_obj_2.distance)

    logging.basicConfig(
        level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
        format='%(asctime)s | %(levelname)s | %(message)s'
    )


if __name__ == '__main__':
    main()
