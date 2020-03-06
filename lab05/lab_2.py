'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''
import sys
sys.path.insert(0, '../tools/aima')
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.


cancerNetwork = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', { (T, T): 0.9, (T, F): 0.2}),
    ('Test2', 'Cancer', { (T, T): 0.9, (T, F): 0.2})
])

print("BP ( Cancer | Both Tests Positive )")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancerNetwork).show_approx())
print("BP ( Cancer | First Test Positive Second Test Negative )")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancerNetwork).show_approx())
