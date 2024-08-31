from datetime import datetime

# Get the current date and time
now = datetime.now()

# Write it to a file in your repository
with open("last_updated.txt", "w") as file:
    file.write(f"Last updated on {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
