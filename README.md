# Firest
Firebase REST API Python with requests.
# USAGE

.env
```
dbsecret=YOUR_DB_LEGECY_KEY
projectid=YOUR_PROJECT_ID
```

main.py
```
import os
from firebase import Firebase
from dotenv import load_dotenv

load_dotenv()

db = Firebase(os.getenv("projectid"), os.getenv("dbsecret"))

db.push("location",{'data':'data'})
db.put('location', {'data':'data'})
db.update('location', {'data':'data'})
db.delete('location')
db.get('location')
```
