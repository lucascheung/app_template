from datetime import datetime
from server.exts import db
from sqlalchemy import event

class Test(db.Model):
    __tablename__ = 'tests'

    test_id = db.Column(
        db.Integer,
        comment='Test ID',
        primary_key=True,
        unique=True,
        nullable=False
    )

    name = db.Column(
        db.Text,
        comment='Test Name',
        nullable=False
    )

    test_groups = db.Column(
        db.Integer,
        comment='number of groups',
        nullable=False
    )

    split_details = db.Column(
        db.Text,
        comment='split details',
        nullable=False
    )

    advertiser_id = db.Column(
        db.String(255),
        comment='advertiser_id'
    )

    created_at = db.Column(
        db.String(255),
        comment='Timestamp of creation in ISO8601 e.g. "2022-05-19T12:14:05Z"'
    )

    expiry_date = db.Column(
        db.String(255),
        comment='Timestamp of test expiry in ISO8601 e.g. "2022-05-19T12:14:05Z"'
    )

    created_by = db.Column(
        db.String(255),
        comment='employee ID'
    )

    status = db.Column(
        db.Integer,
        comment='1,0'
    )
