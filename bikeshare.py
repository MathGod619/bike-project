import time
import pandas as pd
import numpy as np

    # data to be used in the program
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {'january' : 1, 'february' : 2,
              'march' : 3, 'april' : 4, 'may' : 5,
              'june' : 6, 'all' : 7 }

DAY_DATA = {'monday' : 1, 'tuesday': 2, 'wednesday' : 3,
            'thursday': 4, 'friday' : 5, 'saturday' : 6,
            'sunday' : 7, 'all' : 8}

    # this filters the data
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-'*40)
    print('Hello! Let\'s explore some US bikeshare data!')

    # this while loop will select the city from user input.
    city = ''
    while city not in CITY_DATA.keys():
        print("\nPlease choose your city:")
        print("\nChicago , New York City , Washington")
        print("\nYour input is not case sensitive.")
        print('-'*40)

    # standardize the user input
        city = input().lower()

    # if the user input is incorrect, restart the program
        if city not in CITY_DATA.keys():
            print("\nPlease check your input.  Restarting program...")

    # print the user input
    print(f"\nYou have chosen {city.title()} as your city.")
    print('-'*40)

    # similar loop as above
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nPlease choose the month you would like to see data for:")
        print("\nData is available from the months January - June.")
        print("\nYou can also see 'all' of the data.")
        print("\nYour input is not case sensitive.")
        print('-'*40)

    # standardize the user input
        month = input().lower()

    # if the user input is incorrect, restart the program
        if month not in MONTH_DATA.keys():
            print("\nPlease check your input.  Restarting program...")

    # print the user input
    print(f"\nYou have chosen {month.title()} as your month.")
    print('-'*40)

    # this loop seems familiar
    day = ''
    while day not in DAY_DATA.keys():
        print("\nPlease choose the day of the week you would like to see data for:")
        print("\nData is available from Monday - Sunday.")
        print("\nYou can also see 'all' of the data.")
        print("\nYour input is not case sensitive.")
        print('-'*40)

    # standardize the user input
        day = input().lower()

    # if the user input is incorrect, restart the program
        if day not in DAY_DATA.keys():
            print("\nPlease check your input.  Restarting program...")

    # print the user input
    print(f"\nYou have chosen {day.title()} as your day.")
    print('-'*40)

    # announce user inputs
    print(f"\nYour input: city: {city.title()}, month(s): {month.title()} and day(s): {day.title()}.")
    print('-'*40)
    return city, month, day

    # this loads the data for the city and filters it
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
    # load data for city
    print("\nLoading data...")
    print('-'*40)
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to dt
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = month.index(month) + 1
        df = df[df['month'] == month]

    # filter by day of week
    if day != 'all':
        day= day.index(day) + 1
        df = df[df['day_of_week'] == day]
    return df

    # displays statistcs about time data
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # find mode for month
    popular_month = df['month'].mode()[0]

    print(f"Most Popular Month (1 - January): {popular_month}")

    # find mode for day
    popular_day = df['day_of_week'].mode()[0]

    print(f"\nMost Popular Day (1 - Monday): {popular_day}")

    # create hour coulmn
    df['hour'] = df['Start Time'].dt.hour

    # find mode for hour
    popular_hour = df['hour'].mode()[0]
    print(f"\nMost Popular Start Hour: {popular_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # displays statistics about statin data
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"\nThe most commonly used start station: {common_start_station}")

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {common_end_station}")

    # display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'] + df['End Station']
    combo = df['Start To End'].mode()[0]
    print(f"\nThe most common combination is: {combo}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # displays statistics about the trip duration
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # calulate trip duration
    total_duration = df['Trip Duration'].sum()

    # format the time to minutes and seconds
    minute, second = divmod(total_duration, 60)

    # format time to hours and minutes
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    # display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # displays statistcs on the user data, if available
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    user_type = df['User Type'].value_counts()
    print('-'*40)
    print(f"\nThe User Types are:\n{user_type}")
    print('-'*40)

    # display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('-'*40)
        print(f"\nThe types of users by gender are:\n{gender}")
        print('-'*40)
    except:
        print('-'*40)
        print("\nThere is no 'Gender' column in this file.")
        print('-'*40)

    # display birth stats if available
    try:
        earlyb = int(df['Birth Year'].min())
        recentb = int(df['Birth Year'].max())
        commonb = int(df['Birth Year'].mode()[0])
        print('-'*40)
        print(f"\nThe earliest Birth Year is: {earlyb}.")
        print(f"\nThe most recent Birth Year: {recentb}.")
        print(f"\nThe most common Birth Year: {commonb}")
        print('-'*40)
    except:
        print('-'*40)
        print("No birth details available")
        print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # display raw data at uers request, in groups of 5
def raw_data(df):
    """Displays 5 rows of raw data from the csv file for the user selected city."""

    # create a list of accepted user input
    USER_INPUT = ['yes', 'no']
    uinput = ''

    # create a counter to index where in the raw data the user is
    count = 0

    # while loop to determine if user wants to see raw data
    while uinput not in USER_INPUT:
        print("\nDo you wish to view 5 rows of raw data?")
        print("\n Yes or No?")
        uinput = input().lower()
        print('-'*40)

        # the raw data is displayed if requested
        if uinput == "yes":
            print(df.head())
        elif uinput not in USER_INPUT:
            print("\nPlease check your input.")
            print("\nRestarting...\n")
            print('-'*40)

    # this loop will allow the user to see additional raw data
    while uinput == 'yes':
        print("Do you wish to view more raw data?")
        count += 5
        uinput = input().lower()

        if uinput == "yes":
            print(df[count:count+5])
        elif uinput != "yes":
            break

    print('-'*40)
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
#this project was so fun!

#Completed in August 2022
