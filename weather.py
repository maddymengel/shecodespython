import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    date_object = datetime.fromisoformat(iso_string) #Converts and ISO formatted date into a human readable format.
    formatted_date = date_object.strftime("%A %d %B %Y") #iso_string: An ISO date string..
    return formatted_date #Returns: A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021



def convert_f_to_c(temp_in_fahrenheit): #convert_f_to_c takes temp_in_farenheit (this represents the value to be converted)
    if isinstance(temp_in_fahrenheit, (int, float)): # checks if if the instance (temp_in_farenheit) is an int or float
        temp_in_celsius = (temp_in_fahrenheit - 32) * 5/9 # will perform if the above passes
        return round(temp_in_celsius, 1) # rounds the above conversion to 1dp
    elif isinstance(temp_in_fahrenheit, str):  # if temp_in_farenheit is a string it will be converted to a float using the below
        try:
            temp_in_fahrenheit = float(temp_in_fahrenheit)
            temp_in_celsius = (temp_in_fahrenheit - 32) * 5/9
            return round(temp_in_celsius, 1)
        except ValueError: # if temp_in_farenheit isn't a valid value, it will return an error message
            return "Invalid input: temperature must be a number"
    else: # if temp_in_farenheit isn't a valid value, it will return an error message
        return "Invalid input: temperature must be a number"

temp_in_f = 90
temp_in_c = convert_f_to_c(temp_in_f)
# print("The temperature in Celsius is:", temp_in_c)


def calculate_mean(weather_data):
    if all(isinstance(x, (int, float)) for x in weather_data): #Checks all elements are int or float, the calculates the mean value from a list of numbers.
        return sum(weather_data) / len(weather_data)
    elif all(isinstance(x, str) for x in weather_data): # If all elements are a string it will convert to a float and calculate the mean.
        numeric_data = [float(x) for x in weather_data]
        return sum(numeric_data) / len(numeric_data)
    else: # If the list contains elements that can't be calculated it won't be return. 
        raise ValueError("Invalid input: weather_data should contain numbers or strings representing numbers")



# def load_data_from_csv(csv_file):
#     """Reads a csv file and stores the data in a list.

#     Args:
#         csv_file: a string representing the file path to a csv file.
#     Returns:
#         A list of lists, where each sublist is a (non-empty) line in the csv file.
#     """
#     pass


# def load_data_from_csv(csv_file):
#     with open(csv_file) as f:
#         reader = csv.reader(f)
#         data = list(reader)
#     return data



def find_min(weather_data): # find the minimum value in weather_data list and turn a "tuple" that has the minimum value and its index
    if not weather_data: # checks if the list is empty, if its empty it returns an empty ().
        return ()
    min_value = min(weather_data) # finds the minimum value in the data set list and assigns it to the variable min_value
    min_indexes = [] # intialises empty list
    for i in range(len(weather_data)): # checks if the element at index i in in weather_data is equal to the minimum value, if it does it will append to the min_indexes list
        if weather_data[i] == min_value:
            min_indexes.append(i)
    min_index = min_indexes[-1] if min_indexes else -1 # assigns the last index to the variable min_index if the list is not empty, if its not empty it will assign -1
    return float(min_value), min_index # contains the minimum value converted to a float using the float function and the min_index

# Testing
# temperatures = [49, 57, 56, 55, 53, 49]
# result = find_min(temperatures)
# print(result)



def find_max(weather_data): # find the maximum value in weather_data list and turn a "tuple" that has the maximum value and its index
    if not weather_data: # checks if the list is empty, if its empty it returns an empty ().
        return ()
    max_value = max(weather_data) # finds the maximum value in the data set list and assigns it to the variable max_value
    max_indexes = [] # intialises empty list
    for i in range(len(weather_data)): # checks if the element at index i in in weather_data is equal to the maximum value, if it does it will append to the max_indexes list
        if weather_data[i] == max_value:
            max_indexes.append(i)
    max_index = max_indexes[-1] if max_indexes else -1 # assigns the last index to the variable max_index if the list is not empty, if its not empty it will assign -1
    return float(max_value), max_index





def generate_summary(weather_data):
# create empty lists
    temp_min_list = []
    temp_max_list = []
    date_list = []
# Iterate over each line in weather_data and extract the relevant data
    for line in weather_data:
        date_list.append(line[0])  # Store the date in the date_list
        temp_min_list.append(line[1])  # Store the minimum temperature in the temp_min_list
        temp_max_list.append(line[2])  # Store the maximum temperature in the temp_max_list
# Find the minimum and maximum temperatures and their corresponding positions in the lists
    min_value_f = find_min(temp_min_list)[0]  # Find the minimum value in temp_min_list in Fahrenheit
    min_value_c = convert_f_to_c(min_value_f)  # Convert the minimum value to Celsius
    min_data_position = find_min(temp_min_list)[1]  # Find the position of the minimum value in temp_min_list
    max_value_f = find_max(temp_max_list)[0]  # Find the maximum value in temp_max_list in Fahrenheit
    max_value_c = convert_f_to_c(max_value_f)  # Convert the maximum value to Celsius
    max_data_position = find_max(temp_max_list)[1]  # Find the position of the maximum value in temp_max_list
# Calculate the average low and high temperatures in Fahrenheit and convert them to Celsius
    average_low_f = calculate_mean(temp_min_list)  # Calculate the average of temp_min_list in Fahrenheit
    average_low_c = convert_f_to_c(average_low_f)  # Convert the average low temperature to Celsius
    average_high_f = calculate_mean(temp_max_list)  # Calculate the average of temp_max_list in Fahrenheit
    average_high_c = convert_f_to_c(average_high_f)  # Convert the average high temperature to Celsius
# Construct the summary string in the desired format using the calculated values
    return (
    f"{len(weather_data)} Day Overview\n"
    f"  The lowest temperature will be {format_temperature(min_value_c)}, and will occur on {convert_date(date_list[min_data_position])}.\n"
    f"  The highest temperature will be {format_temperature(max_value_c)}, and will occur on {convert_date(date_list[max_data_position])}.\n"
    f"  The average low this week is {format_temperature(average_low_c)}.\n"
    f"  The average high this week is {format_temperature(average_high_c)}.\n"
)
#test
# example_one_given = [
#     ["2021-07-02T07:00:00+08:00", 49, 67],
#     ["2021-07-03T07:00:00+08:00", 57, 68],
#     ["2021-07-04T07:00:00+08:00", 56, 62],
#     ["2021-07-05T07:00:00+08:00", 55, 61],
#     ["2021-07-06T07:00:00+08:00", 53, 62]
#     ]
# print(generate_summary(example_one_given))



def generate_daily_summary(weather_data):
    summary = "" # Initialize an empty string to store the summary

    for entry in weather_data: # Iterate over each entry in weather_data
        date = entry[0]  # Extract the date from the entry
        max_temp = convert_f_to_c(round(entry[2], 1))  # Convert and round the maximum temperature to Celsius
        min_temp = convert_f_to_c(round(entry[1], 1))  # Convert and round the minimum temperature to Celsius
        day = date.split("T")[0].split("-")[2]  # Extract the day from the date
        month = date.split("T")[0].split("-")[1]  # Extract the month from the date
        year = date.split("T")[0].split("-")[0]  # Extract the year from the date
# Adds data to the summary
        summary += f"---- {convert_date(entry[0])} ----\n"  # Add the formatted date to the summary
        summary += f"  Minimum Temperature: {min_temp}°C\n"  # Add the minimum temperature to the summary
        summary += f"  Maximum Temperature: {max_temp}°C\n\n"  # Add the maximum temperature to the summary
    return summary  # Return the final summary string

# # Testing
# example_one = [
#     ["2021-07-02T07:00:00+08:00", 49, 67],
#     ["2021-07-03T07:00:00+08:00", 57, 68],
#     ["2021-07-04T07:00:00+08:00", 56, 62],
#     ["2021-07-05T07:00:00+08:00", 55, 61],
#     ["2021-07-06T07:00:00+08:00", 53, 62]
# ]
# print(generate_daily_summary(example_one))
