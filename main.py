epoch_time = 1710247335223 / 1000  # Divide by 1000 to convert milliseconds to seconds
# datetime_obj = datetime.datetime.fromtimestamp(epoch_time)

# Convert datetime object to exponential format
exponential_format = "{:e}".format(epoch_time)

# Print the exponential format
print("this is exponential format", exponential_format)
print(type(exponential_format))