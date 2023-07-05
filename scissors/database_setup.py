
import sys
import os

# Append the parent directory of the script to the module search path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(script_dir, "..")
sys.path.append(parent_dir)

from scissors import create_app
from scissors.extensions import db

app = create_app()

# Instead of calling db = SQLAlchemy() here, import the existing instance
from scissors.extensions import db

# Initialize the app context
with app.app_context():
    # Define your models (if not already defined) in the models.py file.

    # Create the database tables
    db.create_all()
