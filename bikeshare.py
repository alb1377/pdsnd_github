import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','all']

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
        city = input('\nWhich city would you like to view information on: Chicago, New York city, or Washington?\n').lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print('Please choose from the options provided: Chicago, New York city, or Washington\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhat month are you interested in viewing more information on: January, February, March, April, May, June, or All?\n').lower()
        if month in months:
            break
        else:
            print('Please choose from the options provided: January, February, March, April, May, June, All\n')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) while True:
    while True:
        day = input('\nWhat day are you interested in viewing more information on: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All?\n').lower()
        if day in days:
            break
        else:
            print('Please choose from the options provided: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, All\n')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if month != 'all':
        month = months.index(month) + 1
        df = df[ df['month'] == month ]
    if day != 'all':
        day = days.index(day)
        df = df[ df['day'] == day ]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month

    for common_month in range(len(months)):
        common_month = df['month'].value_counts().idxmax()
        print('The most common month: ', months[common_month].title())
        break

    # TO DO: display the most common day of week
    for common_day in range(len(days)):
        common_day = df['day'].value_counts().idxmax()
        print('The most common day of the week: ', days[common_day].title())
        break

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common start hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most common start station:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('\nThe most common end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_start_end_trip = df[['Start Station', 'End Station']].mode().loc[0]
    print("\nThe most frequent combination of start and end station trip: {}, {}".format(frequent_start_end_trip[0],frequent_start_end_trip[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time: ', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    city = ('chicago', 'new york city', 'washington')
    gender = df['Gender'].value_counts()
    if city == 'chicago' or 'new york city':
        print(gender)
    else:
        print('No information')
    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    earliest_birth_year = birth_year.min()
    print('The earliest birth year: ', earliest_birth_year)
    recent_birth_year = birth_year.max()
    print('The most recent birth year: ', recent_birth_year)
    common_birth = birth_year.value_counts().idxmax()
    print('The most common birth year: ', common_birth)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
