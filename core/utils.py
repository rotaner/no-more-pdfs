# Return a clean list with the selected pages by the user
# in order and without repetitions
def string_to_pagelist_convertor(raw_given_string):
    # Create a empty list where the all the pages will be saved
    raw_selected_pages = []
    
    # Clean the string given a convert it into a list
    split_values = raw_given_string.replace(" ","").split(",")
    for values in split_values:
        if "-" in values:
            # Create a two-item list with the first and last page
            range_values = values.split("-")
            # Convert the text into intergers
            value_1 = int(range_values[0])
            value_2 = int(range_values[1])

            # Look up for the max and min in case the user writes the request backwards
            min_value = min(value_1, value_2)
            max_value = max(value_1, value_2)

            # Create the full range of requested pages
            range_list = range(min_value,max_value+1)

            # Add all the elements into the main list
            raw_selected_pages.extend(range_list)

        # Single page required
        else:
            raw_selected_pages.append(int(values))

    # Clean the duplicates and turn it into a list
    selected_pages = list(set(raw_selected_pages))
    # Sort the pages
    selected_pages.sort()
    # Return the list, ready to be used   
    return selected_pages
