# FlaskLoginSample
Learning Flask Framework

##1. Setup database
- First, you need config your link database in server.py file, line 10
- Second, open your folder with terminal and run:
- `$ from server import init_data`
- `> init_data()` - For create master data
- `> exit()`
- I insert two user account:
- username: `admin` - password: `123456abcd`
- username: `thuytony` - password: `123456abcd`
- You can edit that in file server.py

##2. Setup library
- In terminal:
`$ pip3 install Flask-PyMongo`
`$ pip3 install flask-bcrypt`

##3. Run login example
- In terminal:
`$ python3 server.py`