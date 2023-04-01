from server.exts import db

class ChangeLog(db.Model):
    __tablename__ = 'change_logs'

    change_log_id = db.Column(
        db.Integer,
        primary_key=True
    )
    user_id = db.Column(
        db.Integer
    )
    ref_table = db.Column(
        db.String(255)
    )
    ref_id = db.Column(
        db.Integer
    )
    event = db.Column(
        db.String(255)
    )
    old_values = db.Column(
        db.Text
    )
    new_values = db.Column(
        db.Text
    )
