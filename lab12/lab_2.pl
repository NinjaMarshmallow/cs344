/**
Jason Klaassen for CS344 at Calvin College
5/13/20

Exercise Responses

12.2

a)

    2.1
        The unified pairs are:
        1, 3, 7, 8, 12, 13, 14
    
    2.2

        magic(house_elf). => no
        wizard(harry). => no
        magic(wizard). => no
        magic('McGonagall') => yes
        magic(Hermione) => no

        search tree:

        magic(Hermione)
            |                   
        house_elf(Hermione) => no
            |
        wizard(Hermione) => no
            |
        witch(Hermione) => no (hermione =/= Hermione in prolog)

        So magic(Hermione) => no

b) I have no idea what that means at all and I can't find it on the Prolog page, so yes?

c) Yes, Prolog's inferencing combines two clauses into one clause when attempting to unify, which is the definition of resolution.

*/

house_elf(dobby).
witch(hermione).
witch(’McGonagall’).
witch(rita_skeeter).
magic(X):-  house_elf(X).
magic(X):-  wizard(X).
magic(X):-  witch(X).