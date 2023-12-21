def format_time(time):
    if time == float('inf'):
        return 'Infinity'
    return f"{time//1000:02d}:{time%1000:03d}" if time != 0 else "00:000"


def display_leaderboard(leaderboard):
    print("Leaderboard (Top 3 times):")
    for i, score in enumerate(leaderboard[:3]):
        print(f"{i+1}. {format_time(score)}")
    print()

def is_infinite_time(time):
    return time == 0 or time == float('inf')

def update_leaderboard(leaderboard, new_time):
    if is_infinite_time(leaderboard[0]):
        leaderboard[0] = new_time
    elif is_infinite_time(leaderboard[1]):
        leaderboard[1] = new_time
    elif is_infinite_time(leaderboard[2]):
        leaderboard[2] = new_time
    else:
        leaderboard.append(new_time)
        leaderboard.sort()
        leaderboard = leaderboard[:3]
    return leaderboard

def write_to_file(leaderboard):
    file_positions = ["1stplace.txt", "2ndplace.txt", "3rdplace.txt"]
    for i, score in enumerate(leaderboard):
        with open(f"/Users/louisgan/Desktop/Mine/BOGGETBOLT/{file_positions[i]}", 'w') as file:
            file.write(format_time(score))

def main():
    leaderboard = [float('inf'), float('inf'), float('inf')]  # Initial leaderboard values as infinity
    # Check if files are empty or contain placeholder "00:000" time and update the leaderboard
    file_positions = ["1stplace.txt", "2ndplace.txt", "3rdplace.txt"]
    for i, file in enumerate(file_positions):
        with open(f"/Users/louisgan/Desktop/Mine/BOGGETBOLT/{file}", 'r') as f:
            content = f.read().strip()
            if content == "" or content == "00:000":
                leaderboard[i] = float('inf')
            else:
                time = content.split(':')
                seconds = int(time[0]) * 1000
                milliseconds = int(time[1])
                leaderboard[i] = seconds + milliseconds
    leaderboard.sort()

    print("Welcome to the TOP 3 Time Leaderboard!")
    display_leaderboard(leaderboard)

    while True:
        try:
            new_input = input("Enter a new time in ss:SSS format (or 'q' to quit): ")
            if new_input == 'q':
                break

            new_time = new_input.split(':')
            seconds = int(new_time[0]) * 1000
            milliseconds = int(new_time[1])
            new_number = seconds + milliseconds

            leaderboard = update_leaderboard(leaderboard, new_number)
            display_leaderboard(leaderboard)
            write_to_file(leaderboard)

        except (ValueError, IndexError):
            print("Please enter a valid time in ss:SSS format or 'q' to quit.")

    print("Thanks for using the leaderboard!")

if __name__ == "__main__":
    main()
