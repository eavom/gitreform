import random
from datetime import datetime, timedelta
from helper.texthelper import TextHelper

# Function to generate random datetimes with varying times, skipping days randomly
def generate_random_datetimes(start_date, end_date):
    current_date = start_date
    datetime_list = []

    while current_date <= end_date:

        # Generate a random number of times (between 5 and 50) for the current date
        if int(random.random()*100) < 60:
            num_times = random.randint(1, 15)
        else:
            num_times = random.randint(1, 3)
        
        for _ in range(num_times):
            # Generate a random time between 00:00 and 23:59
            random_hour = random.randint(0, 23)
            random_minute = random.randint(0, 59)
            random_second = random.randint(0, 59)

            # Create the datetime object for the current date with random time
            random_time = current_date.replace(hour=random_hour, minute=random_minute, second=random_second)
            datetime_list.append(random_time.isoformat())
        
        # Randomly decide whether to skip days (60% chance of 0 skip days, 40% chance of 1-5 skip days)
        if int(random.random()*100) < 20:
            days_to_skip = random.randint(1, 5)
        else:
            days_to_skip = 1
        
        current_date += timedelta(days=days_to_skip)
    
    # Sort the list to ensure ascending order
    datetime_list.sort()
    
    return datetime_list

# Start and end dates
start_date = datetime(2016, 12, 26)
end_date = datetime.now()

# Generate the list of random datetimes
random_datetimes = generate_random_datetimes(start_date, end_date)
commit_helper = TextHelper()
file = open("generated_file.txt", "a")

# Print the generated datetimes
for dt in random_datetimes:
    commit_message = commit_helper.get_random_commit_message()
    # print(f'Generating Commit for ==> {dt}')
    file.write(f'\n$Env:GIT_AUTHOR_DATE="{dt}"')
    file.write(f'\n$Env:GIT_COMMITTER_DATE="{dt}"')
    file.write(f'\ngit commit --allow-empty -m "{commit_message}" | Out-Null')

file.close()