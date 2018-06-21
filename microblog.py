from application import app, db
from application.models import User, Post

# Adds the database instance and models to the shell session. 
# Will invoke this function and register the items returned by it 
#  in the shell session.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
