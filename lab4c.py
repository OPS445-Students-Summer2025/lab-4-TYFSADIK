#!/usr/bin/env python3


# Sample data
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

# Function to create a dictionary from two lists
def create_dictionary(keys, values):
    return dict(zip(keys, values))

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York:', york)


def shared_values(dict1, dict2):
    # Get the set of values from both dictionaries
    values1 = set(dict1.values())
    values2 = set(dict2.values())
    # Return the intersection (common values)
    return values1 & values2
