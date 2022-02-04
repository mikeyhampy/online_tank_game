# Overview

I was trying to test the implications of a cloud database in use with a python 2-player game. I found that writing up to the cloud wass almost instant, it was pulling the information/actions back that took more time. In future attempts, increasing databasee speed will be my primary focus.

I wrote the "connect_fb_db" folder and the functions in the "firebase_python_connect" file to pull and write data to/from the database.

I was trying to test the speed and effectiveness of the "readtime database" in conjunction with python. There's no better way to test it than to do a realtime online game.

[Software Demo Video](https://youtu.be/LAUpvkZeAaI)

# Cloud Database

I used the firebase realtime database

Since I was testing a 2-player game, I only needed to store player data for 2 different players. So I just had to run the program on 2 computers and assign different player data for each.

# Development Environment

tools used to develop the software
* pyhon 3 (programming language)
* firebase admin (access database through python)
* raylib-py (display graphics and game controls)

# Useful Websites

list of websites that you found helpful in this project

* [Parwiz Forogh (youtube.com)](https://www.youtube.com/watch?v=EiddkXBK0-o)
* [CodeLoop](https://codeloop.org/?s=firebase)

# Future Work

list of things needed to fix, improve, and add in the future.
* improve speed of pulling data from cloud
* players login and playerdata is assigned for each user
* more compact storage for each player