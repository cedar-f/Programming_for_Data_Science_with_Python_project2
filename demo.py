import time
import pandas as pd
import numpy as np
from tabulate import tabulate

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

MONTH = np.array(['january', 'february', 'march', 'april', 'may', 'june'])

WEEKDAYS = np.array(['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'])

QUESTION_LIST = {
    'city': 'Which city(ies) do you want do select data? Use commas to list the names.'
    , 'month': 'Which month(s) do you want do filter data? Use commas to list the names.'
    , 'weekday': 'Which weekday(s) do you want do filter data? Use commas to list the names.'
}


def get_user_choice(prompt, valid_choice):
    """ check user answer is valid or not and return it"""

    valid_choice = np.array(valid_choice)

    prompt = prompt + '\n(valid answer: ' + ','.join(valid_choice) + ' )\n>'
    while True:
        choice = input(prompt.lower())
        choice_arr = np.char.strip(np.array(choice.lower().split(',')))
        is_valid_choice = np.isin(choice_arr, valid_choice)
        invalid_choice = [str(choice_arr[index]) for index, value in enumerate(is_valid_choice) if not value]
        if len(invalid_choice) > 0:
            print(
                f'Something is not right. Please mind the formatting and be sure to enter a valid option\n Invalid answer {",".join(invalid_choice)}')
        else:
            return choice_arr


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (ndarray) city - name of the city to analyze
        (ndarray) month - name of the month to filter by, or "all" to apply no month filter
        (ndarray) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')
    print('-' * 40)

    cities = get_user_choice(QUESTION_LIST['city'], list(CITY_DATA.keys()))
    print('-' * 30)
    months = get_user_choice(QUESTION_LIST['month'], MONTH)
    print('-' * 30)
    days = get_user_choice(QUESTION_LIST['weekday'], WEEKDAYS)

    print('-' * 40)
    return cities, months, days


def load_data(cites, months, days):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (ndarray) city - name of the city to analyze
        (ndarray) month - name of the month to filter by, or "all" to apply no month filter
        (ndarray) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print("\nThe program is loading the data for the filters of your choice.")
    start_time = time.time()

    df = pd.DataFrame([])

    for city in cites:
        file_name = CITY_DATA[city]
        print(file_name)
        if len(df) == 0:
            df = pd.read_csv(file_name)
            df.insert(1, 'City', city)
        else:
            sub_df = pd.read_csv(file_name)
            sub_df.insert(1, 'City', city)
            df = pd.concat([df, sub_df])

    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-' * 40)
    return df


# cities, months, days = get_filters()

cites = np.array(['chicago', 'washington'])
months = np.array(['january', 'february'])
days = np.array(['monday', 'tuesday'])

df = load_data(cites, months, days)

print(tabulate(df.head(), headers='keys', tablefmt='psql'))
# print(df.head())

# time_stats(df)
# station_stats(df)
# trip_duration_stats(df)
# user_stats(df)
#
# restart = input('\nWould you like to restart? Enter yes or no.\n')
# if restart.lower() != 'yes':
#     break
