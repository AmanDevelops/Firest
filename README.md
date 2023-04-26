# Firest
Firebase REST API Python with requests.
# USAGE

requirements.txt
```
certifi==2022.12.7
charset-normalizer==3.1.0
idna==3.4
python-dotenv==1.0.0
requests==2.28.2
six==1.16.0
urllib3==1.26.15
```

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
