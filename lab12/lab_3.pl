/*
Jason Klaassen for CS344 at Calvin College

Exercise 12.3

*/

connie.
duck.
measuredImproperly(connie).
equalWeightWithDuck(duck).
witch(X) :- madeOfWood(X).
madeOfWood(X) :- equalWeightWithDuck(X); measuredImproperly(X).

?- witch(connie)
/* Should Return yes */