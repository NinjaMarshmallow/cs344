import sys
sys.path.insert(0, '../tools/aima')
from csp import CSP, parse_neighbors, min_conflicts


def Scheduler():
    """ Returns an instance of the CSP class. """
    courses = "cs108 cs112 cs214 stat343 cs336 cs300".split()
    profs = "norman adams schuurman pruim vanderlinden".split()
    slots = "mwf900 mwf1130 tth1030 tth130".split()
    rooms = "sb354 nh064".split()
        
    variables = courses
    assignments = {}
    assignments['cs108'] = "norman"
    assignments['cs112'] = "adams"
    assignments['cs214'] = "adams"
    assignments['stat343'] = "pruim"
    assignments['cs336'] = "vanderlinden"
    assignments['cs300'] = "schuurman"
    neighbors = parse_neighbors("""
    cs108: norman; cs112: adams; 
    cs214: adams; stat343: pruim; 
    cs336: vanderlinden; cs300: schuurman
    """, variables)
    domains = {}
    for course in courses:
        domains[course] = []
    for course in courses:
        for prof in profs:
            for room in rooms:
                for slot in slots:
                    domains[course].append(prof + " " + room + " " + slot)
    
    for type in [courses]:
        for A in type:
            for B in type:
                if A != B:
                    if B not in neighbors[A]:
                        neighbors[A].append(B)
                    if A not in neighbors[B]:
                        neighbors[B].append(A)

    def scheduler_constraints(A, a, B, b, recurse=0):
        ADomain = a.split()
        BDomain = b.split()
        A_Prof = ADomain[0]
        B_Prof = BDomain[0]
        A_Room = ADomain[1]
        B_Room = BDomain[1]
        A_Slot = ADomain[2]
        B_Slot = BDomain[2]
        A_Course = A
        B_Course = B
        
        if(A_Prof == B_Prof and A_Slot == B_Slot):
            return False
        if(A_Room == B_Room and A_Slot == B_Slot):
            return False

        if('norman' in a and A == 'cs108'):
            return True
        if('adams' in a and A == 'cs112'):
            return True
        if('adams' in a and A == 'cs214'):
            return True
        if('pruim' in a and A == 'stat343'):
            return True
        if('vanderlinden' in a and A == 'cs336'):
            return True
        if('schuurman' in a and A == 'cs300'):
            return True
        if(A in courses and B in courses):
            return False
        if(recurse == 0):
            return scheduler_constraints(B, b, A, a, 1)
        return True
    
    return CSP(variables, domains, neighbors, scheduler_constraints)

if __name__ == "__main__":
    schedule = Scheduler()
    solution = min_conflicts(schedule)
    print(solution)