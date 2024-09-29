from flask import Flask, render_template, request, redirect, url_for, flash
import pyrebase

app = Flask(__name__)
app.secret_key = '9fdee513b84d1e02c789454be7481d3f'  # Set a secret key for session management

# Firebase configuration
config = {
    'apiKey': "AIzaSyAe1q62a1SStUv8Q_GvHVdchPzDvWmi2K8",
    'authDomain': "west-c85a1.firebaseapp.com",
    'databaseURL': "https://west-c85a1-default-rtdb.europe-west1.firebasedatabase.app",
    'projectId': "west-c85a1",
    'storageBucket': "west-c85a1.appspot.com",
    'messagingSenderId': "90401560585",
    'appId': "1:90401560585:web:c240e47b2179be99d480d8",
    'measurementId': "G-5ZE3TD1EXM"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()  # Initialize the database

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')

        # Check if the email already exists
        emails = db.child('emails').get()  # Get all emails from the database
        
        if emails.each():  # If there are existing emails
            # Check if the email is already in the database
            for email_entry in emails.each():
                if email_entry.val()['email'] == email:
                    flash('This email is already signed up.', 'warning')
                    return redirect(url_for('index'))

        # Save the email to Firebase Realtime Database
        db.child('emails').push({'email': email})  # Add a new email entry
        flash('Thank you for signing up!', 'success')  # Show success message
        return redirect(url_for('index'))  # Redirect after POST

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
