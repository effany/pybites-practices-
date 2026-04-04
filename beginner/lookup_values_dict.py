NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}

found = []

def get_person_age(name):
    global found
    found = []
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    try:
        if loop_groups(group3, name) != None:
            return loop_groups(group3, name)[0]
        else:
            if loop_groups(group2, name) != None:
                return loop_groups(group2, name)[0]
            else:
                if loop_groups(group1, name) != None:
                    return loop_groups(group1, name)[0]
                else:
                    return NOT_FOUND
    except:
        return NOT_FOUND
    
## method 2

def get_person_age(name):
    for group in (group3, group2, group1):
        name_lower = name.lower()
        for key, age in group.items():
            if key.lower() == name_lower:
                return age
    return NOT_FOUND


def loop_groups(group, name):
   found = [group[name.lower()] for i in group.keys() if name.lower() == i.lower()]
   if len(found) > 0:
        return found
   else:
       return None

