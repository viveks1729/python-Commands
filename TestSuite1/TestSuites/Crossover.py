import unittest
from TestSuite1.Package_DC.TC_Batman import Batman_Test
from TestSuite1.Package_DC.TC_Superman import Superman_Test

from TestSuite1.Package_Marvel.TC_CaptainAmerica import CaptainAmerica_Test
from TestSuite1.Package_Marvel.TC_Thor import Thor_Test

batsy = unittest.TestLoader().loadTestsFromTestCase(Batman_Test)
sups = unittest.TestLoader().loadTestsFromTestCase(Superman_Test)
cap = unittest.TestLoader().loadTestsFromTestCase(CaptainAmerica_Test)
thor = unittest.TestLoader().loadTestsFromTestCase(Thor_Test)

darksied = unittest.TestSuite([batsy, sups])
thanos = unittest.TestSuite([cap, thor])
full_fight = unittest.TestSuite([cap,thor,sups,batsy])

unittest.TextTestRunner().run(full_fight)

