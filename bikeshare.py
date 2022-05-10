import pandas as pd

CityData = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities=['chicago','new york city','washington']
months=['all','january', 'february', 'march', 'april', 'may', 'june']
days=['all', 'saturday','sunday','monday','tuesday','wednesday','thrusday','friday']
def filters():
    try:
        city = input("choose the city you want to analyze: chicago, new york city, washington?")
        while city.lower().strip() not in cities:
            city = input("please enter a valid city: chicago, new york city, washington or all?")
        month = input("choose the month you want to analyze: january, february, march, april, may, june or all?")
        while month.lower().strip() not in months:
            month = input("please enter a valid month: january, february, march, april, may, june or all?")
        day = input("choose the day you want to analyze: saturday, sunday, monday, tuesday, wednesday, thrusday, friday or all?")
        while day.lower().strip() not in days:
            day = input("please enter a valid day: saturday, sunday, monday, tuesday, wednesday, thrusday, friday or all?")
        return city, month, day
    except Exception as e:
        print("something went wrong while entering the inputs, the error is {}." ,format(e))
        
        
        
def data(city, month, day):
    # Loading data for a specified city and filtering it by month and day
    try:
        df = pd.read_csv(CityData[city])
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['End Time']= pd.to_datetime(df['End Time'])
        df['month'] = df['Start Time'].dt.month
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            df = df[(df['month'] == month)]      
        df['day_of_week'] = df['Start Time'].dt.day
        df['hour']=df['Start Time'].dt.hour
        return df
    except Exception as e:
        print("something went wrong with the inputs, the error is {}." ,format(e))


def common_times_of_travel(df,city):
    # here we calculate the most common times of travel
    try:
        # most common month
        common_month_num= df['Start Time'].dt.month.mode()[0]
        common_month=months[common_month_num-1].title()
        print( 'In ' + city + ', the most common month is ' + common_month+ '.')
    except Exception as e:
        print('an error happened while calculating the most common month, the error is: {}.',format(e))
    try:
        # most common day of week
        common_day= str(df['Start Time'].dt.day.mode()[0])
        print( 'In ' + city + ', the most common day is ' + common_day+ '.')
    except Exception as e:
        print('an error happened while calculating the most day of week, the error is: {}.',format(e))
    try:
        # most common hour of day
        common_hour= str(df['Start Time'].dt.hour.mode()[0])
        print( 'In ' + city + ', the most common hour is ' + common_hour + '.')
    except Exception as e:
        print('an error happened while calculating the most common hour of day, the error is: {}.',format(e))


def common_stations_and_trips(df,city):
    # here we calculate the most common sations and trips
    try:
        # most common start station
        common_start_station = df["Start Station"].mode()[0]
    except Exception as e:
        print("something went wrong with calculating the common start station, the error is {}." ,format(e))
    try:
        # most common end station
        common_end_station = df["End Station"].mode()[0]
    except Exception as e:
        print("something went wrong with calculating the common end station, the error is {}." ,format(e))
    try:
        # most common trip
        df['Start To End']=df['Start Station'].str.cat(df['End Station'], sep=' to ')
        common_trip = df['Start To End'].mode()[0]
        print('In ' + city + ', the most common start station is ' + common_start_station + ', the most common end station is ' + common_end_station + ', and the most common trip is ' + common_trip + '.')
    except Exception as e:
        print("something went wrong with calculating the common trip, the error is {}." ,format(e))
        
       
def travel_time(df,city):
    try:
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['End Time']=pd.to_datetime(df['End Time'])
        total_travel_time=(df['End Time']-df['Start Time']).sum()
        counts=(df['End Time']-df['Start Time']).count()
        df['total_travel_time']=(df['End Time']-df['Start Time']).sum()
        average_travel_time=total_travel_time/counts
        #average_travel_time=total_travel_time/df['total_travel_time'].count()
        print('the total travel time is: '+ str(total_travel_time)+', and the average travel time is: '+str(average_travel_time)+'.')
    except Exception as e:
        print("something went wrong with the inputs, the error is {}." ,format(e))
      
def user_info(df,city):
    try:
        counts_of_each_user_type=df['User Type'].value_counts()
        print(counts_of_each_user_type)
        if city == 'chicago' or city=='new york city':
                counts_of_each_gender=df['Gender'].value_counts()
                print(counts_of_each_gender)
                earliest_year_of_birth=df['Birth Year'].min()
                print(earliest_year_of_birth)
                most_recent_year_of_birth=df['Birth Year'].max()
                print(most_recent_year_of_birth)
                most_common_year_of_birth=df['Birth Year'].mode()[0]
                print('in '+ city+ ", the counts of each user type is: "+str(counts_of_each_user_type)+", the counts of each gender is: "+ str(counts_of_each_gender)+', the earliest year of birth is: '+str(earliest_year_of_birth)+ ', the most recent year of birth is: '+str(most_recent_year_of_birth)+', and the most common year of birth is: '+ str(most_common_year_of_birth)+'.')
        else:
                print('in '+ city+", the counts of each user type is: "+counts_of_each_user_type+'.')
    except Exception as e:
        print("something went wrong with the inputs, the error is {}." ,format(e))


def display(df):
    while True:
        counter=0
        show_data=input('do you want to see the first five raws of the data? type "yes" or "no"').lower()
        
        while (show_data=='yes'):
                print(df.iloc[counter:counter+5,:9])
                counter+=5
                show_data=input('do you want to see the following five raws of the data? type "yes" or "no"').lower()
                if show_data=='yes':
                    print(df.iloc[counter:counter+5,:9])
                elif show_data!='yes':
                    break
        break

def main():
    while True:
        city,month,day=filters()
        df=data(city,month,day)
        common_times_of_travel(df,city)
        common_stations_and_trips(df,city)
        travel_time(df,city)
        user_info(df,city)
        display(df)
        
        restart=input("do you want to try again? enter 'yes' or 'no':")
        if restart=='yes':
            main()
        elif restart.lower!='yes':
            break
        break
if __name__ == "__main__":
	main()
    