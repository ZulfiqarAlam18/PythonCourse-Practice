import time

# Print a progress bar with a carriage return to update the same line
for i in range(10):
    print(f"Progress: [{'#' * i}{' ' * (9 - i)}]", end='\r')
    time.sleep(1)  # Simulate some processing time

# Print a message after the progress bar
print("\nTask completed!")



