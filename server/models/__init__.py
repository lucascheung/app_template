import json
from datetime import datetime as dt
from server.exts import db
from sqlalchemy import event
from sqlalchemy.inspection import inspect
from .ChangeLog import ChangeLog

#TODO: add models here to track changes
TRACK_MODELS = []

def track_changes(cls):
    @event.listens_for(cls, 'before_update')
    def before_update(mapper, connection, target):
        state = db.inspect(target)
        old_values = {}
        new_values = {}

        for attr in state.attrs:
            hist = attr.load_history()
            if not hist.has_changes():
                continue
            # hist.deleted holds old value
            # hist.added holds new value
            old_value = hist.deleted[0] if hist.deleted else None
            new_value = hist.added[0] if hist.added else None
            old_values[attr.key] = old_value
            new_values[attr.key] = new_value
        # now changes map keys to new values
        uid = ""
        ref_table = cls.__table__.name
        ref_id = inspect(target).identity[0]
        event = determine_event(old_values, new_values)
        old_values_string = format_values(old_values)
        new_values_string = format_values(new_values)
        if not old_values_string == new_values_string:
            add_change_log(uid, ref_table, ref_id, event, old_values_string, new_values_string)

def determine_event(old_values, new_values):
    if not old_values:
        return 'create'
    if not new_values:
        return 'delete'
    return 'update'

def add_change_log(uid, ref_table, ref_id, event, old_values, new_values):
    cl = ChangeLog(
        user_id = uid,
        ref_table=ref_table,
        ref_id=ref_id,
        event=event,
        old_values=old_values,
        new_values=new_values
    )
    db.session.add(cl)

def format_values(data):
    for k, v in data.items():
        if type(v) == dt:
            data[k] = dt.strftime(v, '%Y-%m-%d')
    return json.dumps(data)

for cls in TRACK_MODELS:
    track_changes(cls)
