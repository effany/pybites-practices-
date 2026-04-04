NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    dedup_names = set(names)
    new_set = [name.title() for name in dedup_names]
    return new_set


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key =lambda name: name.split()[1], reverse=True)
    print(names)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    # names = dedup_and_title_case_names(names)
    # first_names = [name.split()[0] for name in names]
    # current_name = first_names[0]
    # for i in range(0, len(first_names) - 1):
    #     if len(current_name) > len(first_names[i]):
    #         current_name = first_names[i]
    # return current_name  
    names = dedup_and_title_case_names(names)
    first_names = [name.split()[0] for name in names]
    return min(first_names, key=len)



#dedup_and_title_case_names(NAMES)
#sort_by_surname_desc(NAMES)
shortest_first_name(NAMES)