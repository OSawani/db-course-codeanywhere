import os # in order to utilise env variables within this file
from taskmanager import app # app var defined in init file

# tell app how and where to run our application
if __name__ == "__main__": # checking if name class is equal to the main string
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )



