# Introduction to MongoDB


# Getting Started:
1. brew services start mongodb-community@4.2
->Successfully started `mongodb-community` (label: homebrew.mxcl.mongodb-community)

2. mongo
->MongoDB shell version v4.2.5

3. db
->Type db to display the current database.

4. use examples
->switched to db examples

5. db
->verify that your database is now examples

# Set up Your Own Deployment:Get Started with Atlas
1. Part 1: Create an Atlas Account:
        A: Sign up with your Google Account
            1. On the MongoDB Atlas landing page, click Start free.
            2. Click Sign up with Google.
            3. Enter your Gmail or Google Apps email address or the phone number associated with your Google account, then click Next.
            4. Enter the password for your Google account, then click Next.
            5. Review and select the checkbox to accept the Terms of Service and the Privacy Policy.
            Click Submit.
        B: Log in with your Google Account

2. Part 2: Deploy a Free Tier Cluster:
            1. Log into Atlas
            2. Click Build a Cluster
            3. Select Starter Clusters and click Create a Cluster
            4. Select your preferred Cloud Provider & Region
            5. Select M0 Sandbox for cluster tier.
            6. Enter a name for your cluster in the Cluster Name field.
            7. Click Create Cluster to deploy the cluster.

3. Part 3: Whitelist Your Connection IP Address:
            1. Open the Connect dialog.
            2. Configure your whitelist entry.
            3. Click Add IP Address.

4. Part 4: Create a Database User for Your Cluster:
            1. Open the Connect dialog.
            2. In the Create a MongoDB User step of the dialog, enter a Username and a Password for your database user.
            3. Click Create MongoDB User.

5. Part 5: Connect to Your Cluster:
            1. Install the PyMongo Driver
            2. Connect to Your Atlas Cluster:
                1. from pymongo import MongoClient
                2. client = MongoClient('mongodb+srv://dbUser61Test:LIxiaoni616@cluster0709-vpi83.mongodb.net/test?retryWrites=true&w=majority')

6. Part 6: Insert and View Data in Your Cluster:
        Insert Data into your Atlas Cluster with the PyMongo Driver:
        1. db = client.gettingStarted
        2. people = db.people
        3. import datetime
           personDocument = {
             "name": { "first": "Alan", "last": "Turing" },
             "birth": datetime.datetime(1912, 6, 23),
             "death": datetime.datetime(1954, 6, 7),
             "contribs": [ "Turing machine", "Turing test", "Turingery" ],
             "views": 1250000
           }
        4. people.insert_one(personDocument)
        ->  <pymongo.results.InsertOneResult object at 0x10da89d20>


