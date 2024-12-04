import unittest
from Modulle_12.m_12_1 import Test_Runer
from Modulle_12.m_12_2 import Test_tournament_and_runner

ts = unittest.TestSuite()
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Runer.RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_tournament_and_runner.TournamentTest))
run = unittest.TextTestRunner(verbosity=2)
run.run(ts)
