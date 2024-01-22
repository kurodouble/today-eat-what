import random
import time
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore
cred = credentials.Certificate('firebaseKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def get_random_restaurant_or_location():
    # Get all documents from the 'Food' collection
    docs = db.collection('Food').stream()

    # Convert to list and choose a random location
    locations = [doc for doc in docs]
    if not locations:
        return "No location in the Database, check with Kuro"

    chosen_location = random.choice(locations)

    # Get the 'restaurant' array from the chosen location
    restaurants = chosen_location.to_dict().get('restaurants', [])

    # If the 'restaurant' array is not empty, return a random restaurant
    if restaurants:
        return chosen_location.id + " : " + random.choice(restaurants)
    else:
        # If the 'restaurant' array is empty, return the location name
        return chosen_location.id

while True:
    print(get_random_restaurant_or_location())
    user_input = input("Are you satisfied with the result? (Y/N): ")
    if user_input.lower() == 'n':
        continue
    elif user_input.lower() == 'y':
        break
    elif user_input.lower() != 'n' and user_input.lower() != 'n':
        print('Wo Cong Xiao Jiu Zi Bei')
        time.sleep(2)
        break