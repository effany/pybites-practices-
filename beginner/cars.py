from typing import Dict, List
import re 
cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType) -> str:
    """
    Retrieve the 'Jeep' models from the cars dict and join them by a
    comma and space (', '). Leave the original ordering intact.
    """
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars: CarsType) -> List[str]:
    """
    Loop through the cars dict filtering out the first model for each
    manufacturer. Return the matching models in a list leaving the original
    ordering intact.
    """
    return [car[0] for car in cars.values()]

def get_all_matching_models(
    cars: CarsType, grep: str = DEFAULT_SEARCH
) -> List[str]:
    """
    Return a list of all models containing the case insensitive
    'grep' string which defaults to DEFAULT_SEARCH ('trail').
    Sort the resulting sequence alphabetically
    """
    cars_list = []
    for cars in cars.values():
        found = [car for car in cars if re.search(grep.lower(), car.lower()) ]
        if len(found) > 0:
            cars_list.append(" ".join(found))
    return sorted(cars_list)

def sort_car_models(cars: CarsType) -> CarsType:
    """
    Loop through the cars dict returning a new dict with the
    same keys and the values sorted alphabetically.
    """
    new_car_dict = {}
    sorted_keys = sorted(cars.keys())
    for company in sorted_keys:
        sorted_list = sorted(cars[company])
        new_car_dict[company] = sorted_list
    return new_car_dict


print(get_all_jeeps(cars))

