import json

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except Exception as e:
        print(f"Error loading file: {e}")
        return []
    return data

def filter_users_by_age(users, age_threshold):
    filtered_users = []
    for user in users:
        if user.get('age', 0) >= age_threshold:
            filtered_users.append(user)
    return filtered_users

def calculate_average_age(users):
    total_age = 0
    if not users:
        return 0
    for user in users:
        total_age += user.get('age', 0)
    return total_age / len(users)
