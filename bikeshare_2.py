import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input("which city would you like to check ? chicago , new york city , or washington\n").lower()
        if city not in CITY_DATA.keys() :
            print("invilid input")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True :
        month = input("which month would you like to check ? january , february , march , april, may ,june or all\n ").lower()
        months  =["january", "february", "march", "april", "may", "june","all"]
        if month not in months :
            print("invalid input")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input(" Which day would you like to check ? monday, tuesday ,wednesday,thursday,friday,saturday, sunday or all \n").lower()
        days = [ "monday"," tuesday","wednesday","thursday","friday","saturday", "sunday" , "all"]
        if day not in days:
            print("invalid input")
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != "all" :
        months  =["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df['month']== month]
    if day != "all":
        df = df[df["day_of_week"]== day.title()]
       

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    startStation = df['Start Station'].value_counts().idxmax()
    print('most commonly used start station \n', startStation)

    # display most commonly used end station
    
    endStation = df['End Station'].value_counts().idxmax()
    print('most commonly used end station \n',endStation)
   

    # display most frequent combination of start station and end station trip
    combinationStation = df.groupby(['Start Station', 'End Station']).count()
    print('most frequent combination of start station and end station trip \n', startStation, " , ", endStation)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totalTime = df['Trip Duration'].sum()
    print('total travel time is', totalTime/86400, " Days")

    # display mean travel time
    meanTime = df['Trip Duration'].mean()
    print('mean travel time is', meanTime/60, " Minutes")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    user_types = df["User Type"].value_counts()
    
    print('  User types \n', user_types)

    # Display counts of gender
    try:
     
      print('Gender Types\n', df['Gender'].value_counts())
    except KeyError:
      print(" data available ")
  
              
    
    
   

    # Display earliest, most recent, and most common year of birth
    try:
      print('Earliest Year:', df['Birth Year'].min())
    except KeyError:
      print("No data available ")

    try:
      print('Most Recent Year:',df['Birth Year'].max())
    except KeyError:
      print("No data available .")

    try:
     print('Most Common Year:',df['Birth Year'].value_counts().idxmax())
    except KeyError:
      print("No data available")
    
    
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    i = 0 
    user_input = input("Do you want to see 5 rows of data? type yes or no \n").lower()
    
    while True:
        if  user_input  == "no" :
             break
    
        print(df[i:i+5])
        user_input = input("Do you want to see another 5 rows of data? type yes or no \n").lower()
        i +=5
        
    
                
        

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


