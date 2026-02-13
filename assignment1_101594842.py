"""
Author: <Wasifa Hossain>
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" # string
preferred_weight_kg = 20.5 # float
highest_reps = 25 # integer
membership_active = True # boolean

# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Nancy": (30, 45, 20),     # yoga, running, weightlifting
    "Max": (30, 35, 30),
    "Erica": (50, 55, 40)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, minutes in list(workout_stats.items()):
    yoga, running, weights = minutes
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes
# Step e: Create a 2D nested list called workout_list
workout_list = []
friend_names = []

for friend, minutes in workout_stats.items():
    if "_Total" in friend:
        continue
    yoga, running, weights = minutes
    workout_list.append([yoga, running, weights])
    friend_names.append(friend)
# Step f: Slice the workout_list
print("Yoga and Running minutes for all friends:")
for workout in workout_list:
    print(workout[:2])

print("\nWeightlifting minutes for the last two friends:")
for workout in workout_list[-2:]:
    print(workout[2])

# Step g: Check if any friend's total >= 120
for friend in friend_names:
    if workout_stats[f"{friend}_Total"] >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
name_input = input("\nEnter a friend's name: ")

if name_input in workout_stats and isinstance(workout_stats[name_input], tuple):
    yoga, running, weightlifting = workout_stats[name_input]
    total = workout_stats[f"{name_input}_Total"]
    print(f"\nWorkout details for {name_input}:")
    print(f"Yoga: {yoga} minutes")
    print(f"Running: {running} minutes")
    print(f"Weightlifting: {weightlifting} minutes")
    print(f"Total: {total} minutes")
else:
    print(f"Friend {name_input} not found in the records.")
# Step i: Friend with highest and lowest total workout minutes
totals = {
    friend: workout_stats[f"{friend}_Total"]
    for friend in friend_names
}

highest_friend = max(totals, key=totals.get)
lowest_friend = min(totals, key=totals.get)

print(f"\nFriend with the highest total workout minutes: {highest_friend}")
print(f"Friend with the lowest total workout minutes: {lowest_friend}")
