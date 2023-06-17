import glob

def combine_files(file_list, output_file):
    with open(output_file, 'w') as output:
        for i, file_name in enumerate(file_list):
            with open(file_name, 'r') as file:
                lines = file.readlines()
                # Remove first 3 lines except for the first file
                if i == 0:
                    lines = lines[3:]
                else:
                    lines = lines[6:]
                # Remove last line except for the last file
                if i != len(file_list) - 1:
                    lines = lines[:-1]
                output.write(''.join(lines))

# Specify the base directory
base_directory = '/home/luke/vnstat/'

# Accept date as input from the user
date = input("Enter the date (YYYY-MM-DD): ")

# Split the date into year, month, and day
year, month, day = date.split('-')

# Specify the directory path
directory = f'{base_directory}{month}/{day}/'

# Specify the time range
start_time = '00:00:01'
end_time = '22:00:01'
time_interval = 2

# Generate the file list using glob
file_list = []
for hour in range(0, 24, time_interval):
    time = f'{hour:02d}:00:01'
    file_name = f'{directory}{year}-{month}-{day}_{time}.txt'
    file_list.append(file_name)

# Specify the output file name
output_file = f'{base_directory}combined/{date}.txt'

# Call the function to combine the files
combine_files(file_list, output_file)

