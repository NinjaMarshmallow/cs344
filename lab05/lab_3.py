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


happyNetwork = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', ' ', 0.01),
    ('Happy', 'Sunny Raise', { (T,T): 1.0, 
                               (T,F): 0.7,
                               (F,T):0.9,
                               (F,F):0.1
                            })
])

print("BP ( Raise | Sunny )")
print(enumeration_ask('Raise', dict(Sunny=T), happyNetwork).show_approx())
print("BP ( Raise | Happy & Sunny )")
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happyNetwork).show_approx())

'''

BP ( Raise | Sunny )
False: 0.99, True: 0.01
BP ( Raise | Happy & Sunny )
False: 0.986, True: 0.0142

The First Probability Distribution is expected because according to the Bayesian Network, 
there is no causation between the weather being Sunny and getting a Raise

The Second Probability Distrubition makes sense because the probability that you have a raise is increased because there is a 
causal relationship between a raise and being happy, but the effect isn't as large because the happiness could also be
explained away be the fact that it is sunny and being Sunny has a much higher probability of occurance than raises.

BP ( Raise | Sunny ) = < P( has Raise | Sunny ) , P( no Raise | Sunny ) >
 = < P(has Raise), P( no Raise ) ------- Sunny and Raise are independent
 = < .01, .99 >
  ( < True, False > )

 BP ( Raise | Happy & Sunny ) = < P( has Raise | Happy & Sunny ) , P( no Raise | Happy & Sunny) >

 = alpha  * < P(Raise & Happy & Sunny), P(no Raise & Happy & Sunny)
 = alpha * < .01 * .7 * 1.0 , .99 * .7 * .7 >
 = alpha * < .007, .4851 > ( alpha = 1 / (.07 + .4851) = 1.80)
 
 = < .014, .986 >
 ( < True, False > )
'''