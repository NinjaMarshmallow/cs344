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


cancerNetwork = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', { T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', { T: 0.9, F: 0.2})
])

print("BP ( Cancer | Both Tests Positive )")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancerNetwork).show_approx())
print("BP ( Cancer | First Test Positive Second Test Negative )")
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancerNetwork).show_approx())

'''

BP ( Cancer | Both Tests Positive )
False: 0.83, True: 0.17
BP ( Cancer | First Test Positive Second Test Negative )
False: 0.994, True: 0.00565

These results definitely go against the presumption that the test will be extremely accurate and telling.
The test seems like it should have a 90% chance of telling you one way or the other, but since the actual
probability of having cancer is so low, the number of false positives far outweights the number of true positives.

A negative test of cancer has a significant impact on the probability that you have cancer since the probability 
is 30x less if you tested negative on one test of two rather than positive on both tests.

BP ( Cancer | Both Tests Positive) = < P( has Cancer | Both Tests Positive ) , P( no Cancer | Both Tests Positive) >
 < P( has Cancer | Both Tests Positive ) , P( no Cancer | Both Tests Positive) >

 = alpha  * < P(Cancer & Test1 & Test2), P(not Cancer & Test1 & Test2) >
 = alpha * < .01 * .9 * .9 , .99 * .2 * .2 >
 = alpha * < .0081, .0396 > ( alpha = 1 / (.0081 + .0396) = 20.964) 
 
 = < .17, .83 >
 ( < True, False > )

 BP ( Cancer | Test1 & not Test2 ) = < P( has Cancer | Test1 & not Test2 ) , P( no Cancer | Test1 & not Test2) >
 < P( has Cancer | Test1 & not Test2 ) , P( no Cancer | Test1 & not Test2) >

 = alpha  * < P(Cancer & Test1 & not Test2), P(not Cancer & Test1 & not Test2) >
 = alpha * < .01 * .9 * .1 , .99 * .2 * .8 >
 = alpha * < .0009, .1584 > ( alpha = 1 / (.0009 + .1584) = 6.277)
 
 = < .0006, .994 >
 ( < True, False > )
'''