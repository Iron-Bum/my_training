from Tournament import Tournament
from Tournament import Runner
from unittest import TestCase
from unittest import main


class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for i in cls.all_results:
            for result, name in i.items():
                print(f"{name}: {result}й")
            print('--------------------------')

    def test_Tournament_1(self):
        tournament_1 = Tournament(90, self.runner1, self.runner3)
        results = tournament_1.start()
        last_runner = max(results.keys())
        TournamentTest.all_results.append(results)
        self.assertTrue(results[last_runner] == 'Ник')

    def test_Tournament_2(self):
        tournament_2 = Tournament(90, self.runner2, self.runner3)
        results = tournament_2.start()
        last_runner = max(results.keys())
        TournamentTest.all_results.append(results)
        self.assertTrue(results[last_runner] == 'Ник')

    def test_Tournament_3(self):
        tournament_3 = Tournament(90,  self.runner3, self.runner1, self.runner2)
        results = tournament_3.start()
        last_runner = max(results.keys())
        TournamentTest.all_results.append(results)
        self.assertTrue(results[last_runner] == 'Ник')

    def test_equal_distance_1(self):
        min_speed_runner = min(self.runner1.speed, self.runner2.speed, self.runner3.speed)
        tournament_4 = Tournament(min_speed_runner, self.runner3, self.runner2, self.runner1)
        results = tournament_4.start()
        last_runner = max(results.keys())
        TournamentTest.all_results.append(results)
        self.assertTrue(results[last_runner] == 'Ник')

    def test_equal_distance_2(self):
        min_speed_runner = min(self.runner1.speed, self.runner2.speed, self.runner3.speed)
        tournament_4 = Tournament(min_speed_runner, self.runner1, self.runner3, self.runner2)
        results = tournament_4.start()
        last_runner = max(results.keys())
        TournamentTest.all_results.append(results)
        self.assertTrue(results[last_runner] == 'Ник')

    def test_equal_distance_3(self):
        min_speed_runner = min(self.runner1.speed, self.runner2.speed, self.runner3.speed)
        tournament_4 = Tournament(min_speed_runner, self.runner3, self.runner1, self.runner2)
        results = tournament_4.start()
        last_runner = max(results.keys())
        TournamentTest.all_results.append(results)
        self.assertTrue(results[last_runner] == 'Ник')

    def test_equal_distance_4(self):
        min_speed_runner = min(self.runner1.speed, self.runner2.speed, self.runner3.speed)
        tournament_4 = Tournament(min_speed_runner, self.runner2, self.runner3, self.runner1)
        results = tournament_4.start()
        last_runner = max(results.keys())
        TournamentTest.all_results.append(results)
        self.assertTrue(results[last_runner] == 'Ник')

    def test_equal_distance_5(self):
        min_speed_runner = min(self.runner1.speed, self.runner2.speed, self.runner3.speed)
        tournament_4 = Tournament(min_speed_runner, self.runner1, self.runner2, self.runner3)
        results = tournament_4.start()
        last_runner = max(results.keys())
        TournamentTest.all_results.append(results)
        self.assertTrue(results[last_runner] == 'Ник')

    def test_equal_distance_6(self):
        min_speed_runner = min(self.runner1.speed, self.runner2.speed, self.runner3.speed)
        tournament_4 = Tournament(min_speed_runner, self.runner2, self.runner1, self.runner3)
        results = tournament_4.start()
        last_runner = max(results.keys())
        TournamentTest.all_results.append(results)
        self.assertTrue(results[last_runner] == 'Ник')






if __name__ == '__main__':
    main()
