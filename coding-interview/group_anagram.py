def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Group anagrams together."""
    sorted_strings = ["".join(sorted(string)) for string in strings]
    dedup_array = set(sorted_strings)
    result = []
    for item in dedup_array:
       sub_array = [strings[i] for i, string in enumerate(sorted_strings) if string == item]
       result.append(sub_array)
    return result



###### method 2 #####

from collections import defaultdict

def group_anagrams2(strings: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for string in strings:
        key = "".join(sorted(string))
        print(key)
        groups[key].append(string)
    return list(groups.values())

if __name__ == "__main__":
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    group_anagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])