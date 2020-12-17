# %% Setting up a site to display the Predicted winner using Flask

from flask import Flask
app = Flask(__name__)

@app.route('/')
def Superbowl_Winners():
    return 'The Kansas City Chiefs are the predicted winners of the 2020 Superbowl!!!!!!'


# %%
