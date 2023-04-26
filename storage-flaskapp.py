import os
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, storage

app = Flask(__name__)

# Set the configuration values
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024  # 200 MB max file size


# Initialize Firebase
cred = credentials.Certificate('serviceaccount.json')
firebase_admin.initialize_app(cred, {'storageBucket': 'bucketalias.appspot.com'})
bucket = storage.bucket()

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({"error": "Failed to upload file"}), 400
    
    file = request.files['file']
    path = request.form.get('path')
    key = request.form.get('key')
    if key != "YOUR-RANDOM-API-KEY-GENERATED-BY-YOU-TO-PREVENT-UNAUTHORIZED-ACCESS":
        return jsonify({"error": "Permission Denied"}), 400
    
    # Upload the file to Firebase Storage
    blob = bucket.blob(path +"/"+ file.filename)
    blob.upload_from_file(file)
    blob.make_public()
    file_url = blob.public_url
    return jsonify({"url": file_url}), 200

if __name__ == '__main__':
    app.run()
