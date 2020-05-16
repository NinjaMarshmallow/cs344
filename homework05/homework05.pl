/*
Homework 5 Part 2 

LPN Exercise 2.4 Crossword problem


*/

word(astante,  a,s,t,a,n,t,e).
word(astoria,  a,s,t,o,r,i,a).
word(baratto,  b,a,r,a,t,t,o).
word(cobalto,  c,o,b,a,l,t,o).
word(pistola,  p,i,s,t,o,l,a).
word(statale,  s,t,a,t,a,l,e).

/*
Letter Matches

V1, H1 must share 2,2
V1, H2 must share 4,2
V1, H3 must share 6,2

V2, H1 must share 2,4
V2, H2 must share 4,4
V2, H3 must share 6,4

V3, H1 must share 2,6
V3, H2 must share 4,6
V3, H3 must share 6,6

*/
getLetter(X,Y) :- nth0(Y, X, L).

matchLetter(X, Y, XP, YP) :- getLetter(X, XP) = getLetter(Y, YP).
crossword(V1, V2, V3, H1, H2, H3) :- matchLetter()