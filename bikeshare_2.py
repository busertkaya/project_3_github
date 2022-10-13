import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']

MONTH_OPTIONS = {'1': 'january', '2': 'february', '3': 'march', '4': 'april', '5': 'may', '6': 'june', '7': 'all'}

DAY_OPTIONS = {'1': 'monday', '2': 'tuesday', '3': 'wednesday', '4': 'thursday', '5': 'friday', '6': 'saturday', '7':'sunday', '8': 'all'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=str(input('Please chose one of the cities below \n Chicago , New York City, Washington: ')).lower()
        if city in CITIES:
            break
        else:
            print('#############################')
            print('Please select valid city name')
            print('#############################')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        user_month=str(input(' 1:January \n 2:February \n 3:March \n 4:April \n 5:May \n 6:June \n 7:All \n Please choose one of the options above:'  )).lower()
        if user_month in MONTH_OPTIONS:
            month=MONTH_OPTIONS[user_month]
            break
        else:
            print('#############################')
            print('Please select valid option  :')
            print('#############################')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        user_day=str(input(' 1:Monday \n 2:Tuesday \n 3:Wednesday \n 4:Thursday \n 5:Friday \n 6:Saturday \n 7:Sunday \n 8:All \n Please choose one of the options above:'  )).lower()
        if user_day in DAY_OPTIONS:
            day=DAY_OPTIONS[user_day]
            break
        else:
            print('#############################')
            print('Please select valid option  :')
            print('#############################')


    print('-'*40)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month=df['month'].mode()[0]
    print("Most common month is {}".format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print("Most common day is {}".format(most_common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour=df['hour'].mode()[0]
    print("Most common start hour is {}".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].mode()[0]
    print("Most commonly used start station is {}".format(most_common_start_station))

    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].mode()[0]
    print("Most commonly used end station is {}".format(most_common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station=df[['Start Station','End Station']].mode()
    print("Most frequent combination of start station and end station trip {} ".format(most_common_start_end_station))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total travel time is {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("Mean travel time is {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types is {}".format(user_types))

    try:
    # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print("Counts of genders is {}".format(gender_count))
    except:
        print("\nThere is no 'Gender' column in this file.")

        # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth=df['Birth Year'].min()
        most_recent_birth=df['Birth Year'].max()
        most_common_birth=df['Birth Year'].mode()[0]

        print("Earliest year of birth is {}".format(earliest_birth))
        print("Most recent year of birth is {}".format(most_recent_birth))
        print("Most common year of birth is {}".format(most_common_birth))
    except:
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays 5 rows of data from the csv file for the selected city.
    Args:
        param1 (df): The data frame you wish to work with.
    Returns:
        None.
    """
    row=0
    while True:
        view_raw_data=input("Would you like to see raw data. Type yes or no: ").lower()
        if view_raw_data == 'yes':
            print(df.iloc[row:row+6])
            row=+6
        elif view_raw_data == 'no':
            break
        else:
            print("You entered wrong input. Please try again")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
