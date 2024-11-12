import time
import pandas as pd
import numpy as np

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


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    # display the most common day of week

    # display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    # display most commonly used end station

    # display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        cities, months, days = get_filters()
        df = load_data(cities, months, days)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
