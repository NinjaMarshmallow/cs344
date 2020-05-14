/**
Jason Klaassen for CS344 at Calvin College
5/13/20

Exercise Responses

12.1

a)
    1.4 
        The first three are straight forward adjectives.
        #4 - Created the clause of footmassage(X, mia)
        Same style as #4
        Took the or in the sentence to mean logical or so I made two seperate clauses
    
    1.5
        wizard(ron). => yes
        witch(ron). => no
        wizard(hermione). => no
        witch(hermione). => no
        wizard(harry). => yes
        wizard(Y). => Y = ron
        witch(Y). => uncaught exception: error(existence_error(procedure,witch/1),top_level/0)

b) Yes modus ponens refers to the ability to use the 'implies' operator. Since this operator 
    can be reduced from a implies b to --- (not a) OR b --- then it can be easily implemented 
    with logical operators.

c) The power behind horn clauses is the ability to stack multiple together to gradually build 
    a system of logic by first creating low level facts then building higher and higher level 
    horn clauses to ask more interesting questions. The issue with this though is that is 
    requires the logician to keep extremely close attention to the relationships between clauses 
    to avoid infinite looping or incorrect results or forgetting how the system functions in general 
    making it impossible to extend or fix

d) Yes, the TELL operations are those that form a logic base that start with a predicate clause 
    to establish knowledge such as fruit(apple).the ASK operations can be executed with the 
    ?- syntax or like this example fruit(W). which responds with W = any fruit in the knowledge base

Below is the finished program with a knowledge base for testing

*/

killer(butch).
married(mia, marsellus).
dead(zed).
tasty(cheesecake).
tasty(kiwi).
nutritious(spinach).
nutritious(kiwi).
goodDancer(charlie).
footMassage(zed, mia).

killedByMarsellus(X) :- footMassage(X, mia).

lovedByMia(X) :- goodDancer(X).

julesWillEat(X) :- tasty(X); nutritious(X).

wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).
