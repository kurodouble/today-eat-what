import random
import time
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firestore
cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "where-to-eat-goss",
  "private_key_id": "ccae7ec4e3ac4bb3c9bfdfd0e464abb522097c64",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDMujw6B+Z9+Y5+\nQmYNa0V3QbrbLv/ugI2IgafJ7+IemB4sw8HSEczdECChWm9kD40Bb3RzLfRWegi5\nlfCldQulvm8EWqPQCMcaX2/ye1iNFVuDXnGQOWBo7zVCR9qP7MRXtRAzbuh56cNK\nLevbrtqTzMuNH7BiBpksGpV5b9L5BgpGwn5et5r5bocM9bVwkQ2ZQ29JrGxlnlhM\nglpM692K7wKkbBAGterT8ETpOGzb0ns23t44+Jbaemkg3Li6jhqNsICWF/IOPoOX\ns41+WkkT284Sfs3vA30s2K1V8yyFbEUFpVl0x0h+EY8R9Ufce7g/RqHHhUWxV0Lh\n6PMDbbDtAgMBAAECggEAA2lpHoh01rhFdSTdzC8eTGimg1zq+/UIJsm5Bkb+oYbk\ncyzcpTJnE8S0iSvXe7c8oNT+1PqOPgYGRjLRp1g7gPVwUTDCK8cxq5FX7Wu7zozC\nu9OOQ0U0LkYqQOKvVEMHBJ/VAh5ri7iRvhc6J9eSofBBm3uh4LL+c3s1RChRFOr1\nYw16yDv+sy5MWL1U11NqhRGLm/YZ4qrLOQ+pMvFyrSBUmSq0nvJUZADf8zMoSamu\nlJD+9UjGE+YucpekbuZgJZ/6XEDjPgIg7SYaU0JmwISu/Clh3ioqn7HHpUGABO0A\nXZavLkga30JLOM3JwTAz7n7k5JkXCQOyhL22LRBjgQKBgQDncbRhZr4MdtrJ1N3S\n4O3a7YlPny7VrOVvvTZRB3AI/D5w3mvHNKsGa+s+jHz6dE9ICgFJjjsptMdSDAp8\n52RDHjHvYulnjA3LNBvoVazyD4L+UKJRfr/j/E+JlUOx7j3/yqO/dkF5gEAxmKgx\njeboOx1Ue+X+paWeCmB5+CCWLQKBgQDict/Ry1/i2gHmJsjL3auYIQb2zSHHw8Zp\neQR7++1KDP0gF3/2jPw91CGh0+XMJGdx72+QndU1/AiQRzwExVb9rlyLSSgsnjsg\njWLfek+oIxFl4qs3g9P/Q0Vbw9rRGagWmoLY3Ana3EKfRvtO4VLNRi9OHh08AStx\nuAftAXr9wQKBgBN60n/QMfbCmi+apwD0xZBDpeb5sutxHe6Fsming5p+AJNnZRLj\nL/Hea3JcSLibyYB6txkFy5z7Bju1n7xbjWjIxdMsNBDvDMopnJ+1dlT5UUEucDsD\nvAroVZly4ru7HaTF3Xpj7abYUI7cFmv1UZYCQ7m0o+sG7iWbIfuiErwRAoGAVauU\nFbDVc+N6eHIP4WDZvFIyakitEQB2Hg0UrzteSHelg/CgDszD2ThaCPk7pQHYyPgG\nwzWTJjtVmg/5Guz1vj+q718b/dVXFTeoQlfprvilamBY2kXbfGUc5lyweg800mhe\nPGDysYRHCC84gF0qkFKPLwShlsPyhbFT/kxjFYECgYAHGv5XLqvFVFCJRp1TQ5Wi\nZk7sKBq0KrmEW/7pzq5UhtnadYxlbDoHthTVXx52HR/5Z5kDe/tJoUvh6M7dJqPh\nJkWa5lFvTF8Kaus08HZ6DS2BOoBr+Jxgj7Wq8aravf8dMf4z/YvJKEBDMCNQIBHA\n6oTypQHy0O9si+pyBONzLA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-9j2lr@where-to-eat-goss.iam.gserviceaccount.com",
  "client_id": "107268368000677071938",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9j2lr%40where-to-eat-goss.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})
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