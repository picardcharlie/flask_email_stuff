from app import create_app
from flask_migrate import Migrate
from app.models import db, User
#db, user, post, etc

app = create_app('default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db = db, User = User) #db, user, post, etc