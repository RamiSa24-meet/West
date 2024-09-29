from flask import Flask, render_template, request, redirect, url_for, flash
import requests
import json

app = Flask(__name__)
app.secret_key = '9fdee513b84d1e02c789454be7481d3f'  # Set a secret key for session management

# Firebase configuration
FIREBASE_URL = "https://west-c85a1-default-rtdb.europe-west1.firebasedatabase.app"
EMAILS_PATH = "/emails.json"  # Path to the emails node

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')

        # Check if the email already exists
        response = requests.get(FIREBASE_URL + EMAILS_PATH)  # Get all emails from the database
        emails = response.json()  # Convert response to JSON

        if emails:  # If there are existing emails
            # Check if the email is already in the database
            for email_entry in emails.values():
                if email_entry['email'] == email:
                    flash('This email is already signed up.', 'warning')
                    return redirect(url_for('index'))

        # Save the email to Firebase Realtime Database
        requests.post(FIREBASE_URL + EMAILS_PATH, json={'email': email})  # Add a new email entry
        flash('Thank you for signing up!', 'success')  # Show success message
        return redirect(url_for('index'))  # Redirect after POST

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
