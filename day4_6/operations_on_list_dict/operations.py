from data import us_state_abbrev, states_list

def main():

    tenth_item = list(us_state_abbrev.items())[9]
    print('10th item in us_state_abbrev is {}'.format(tenth_item))

    tenth_item = states_list[9]
    print('10th item in states_list is {}'.format(tenth_item))

    forty_fifth_key = list(us_state_abbrev.keys())[44]
    print('45th key in us_state_abbrev is {}'.format(forty_fifth_key))

    twenty_seventh_value = list(us_state_abbrev.values())[26]
    print('27th value in us_state_abbrev is {}'.format(twenty_seventh_value))


    key_to_replace = list(us_state_abbrev.keys())[14]

    print('Before replacement {}'.format(us_state_abbrev[key_to_replace]))

    us_state_abbrev[states_list[27]] = us_state_abbrev[key_to_replace]
    del us_state_abbrev[key_to_replace]

    print(len(us_state_abbrev))



if __name__ == '__main__':
    main()
