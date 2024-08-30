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
        if user['age'] >= age_threshold:
            filtered_users.append(user)
    return filtered_users

def calculate_average_age(users):
    total_age = 0
    for user in users:
        total_age += user['age']
    return total_age / len(users)

def process_user_data(file_path, age_threshold):
    users = load_data(file_path)
    if not users:
        return

    filtered_users = filter_users_by_age(users, age_threshold)

    average_age = calculate_average_age(filtered_users)
    print(f"Average age of filtered users: {average_age}")

    return filtered_users

if __name__ == "__main__":
    file_path = "user_data.json"
    age_threshold = 30
    filtered_users = process_user_data(file_path, age_threshold)
    print(f"Filtered Users: {filtered_users}")
