/*

Jason Klaassen for CS344 at Calvin College
5/16/20

Exercise 13.1

The recursion built in these exercises is made by defining a base case for the rule then defining the recursive case below it using a new variable to search the knowledge base recursively until one is found or the search ends.

a) Work below

b) Yes, modus ponens is the way that prolog searches the knowledge base for rules that can unify the query made. modus ponens is how Prolog takes the body of a rule and infers the head of that rule. Essentially doing the logic of IF body THEN head.



*/

/* 
    Exercise 3.2 from LPN
*/
nextDoll(natasha, irina).
nextDoll(olga, natasha).
nextDoll(katarina, olga).

in(X,Y) :- nextDoll(X, Y).
in(X, Y) :- nextDoll(X, Z), in(Z, Y). 

/*
    Exercise 4.5 from LPN
*/
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

/*
    Base case followed by translating the head appending it to Y recursively with the tail.
*/
listtran([], []).
listtran(X|tX, Y) :- listtran(tX, [tran(X), .. Y])]).

