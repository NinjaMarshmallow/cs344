'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013
@student: Jason Klaassen at Calvin University Spring 2020
'''
import sys
sys.path.insert(0, '../tools/aima')
from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)

# Compute P(Cavity | catch)
ProbCatch = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print("Probability of a Cavity when there is a Toothache:")
print(PC.show_approx())

'''
P( Cavity | catch ) = P(Cavity && Catch) / P(Catch)

P(Cavity && Catch) = .108 + .072
P(Catch) = .108 + .016 + .072 + .144

P(Cavity && Catch) / P(Catch) = (.108 + .072) / (.108 + .016 + .072 + .144)

= .529

BoldP(Cavity | catch) = < .529, .471 >

'''

print("Probability of a Cavity when there is a catch:")
print(ProbCatch.show_approx())

'''
P( Coin2 | Coin1 ) = P(Coin2 && Coin1) / P(Coin1)

P(Cavity && Catch) = 0.5 * 0.5
P(Catch) = 0.5

P(Cavity && Catch) / P(Catch) = .25 * .5 = .5

BoldP(Coin2 | Coin1) = < .5, .5 >

'''

P = JointProbDist(['Coin1', 'Coin2'])
T, F = True, False
P[T, T] = P[F, F] = P[T, F] = P[F, T] = 0.5 * 0.5
ProbCoin2 = enumerate_joint_ask('Coin2', { 'Coin1': T}, P)


print("Probability of Coin2 is heads given Coin1 is heads:")
print(ProbCoin2.show_approx())

'''
c. Yes
   Yes

'''

