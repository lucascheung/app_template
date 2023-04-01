import json
import os
import logging.config
from server.models import Test

def seed(db):
    # Add read seed file
    # if os.environ.get("ENV", "dev") == "dev":
    #     with open('./seed/seed.json') as json_file:
    #         seed_object = json.load(json_file)

    # else:
    #     with open('../seed/seed.json') as json_file:
    #         seed_object = json.load(json_file)

    # # Clear current database
    # db.session.query(Test).delete()
    # db.session.commit()
    
    # def seed_test(db,item):
    #     test = Test(
    #         test_id= item['test_id'],
    #         name= item['name'],
    #         test_groups= item['test_groups'],
    #         split_details=json.dumps(item['split_details']),
    #         created_at= item['created_at'],
    #         created_by= item['created_by'],
    #         advertiser_id = item['advertiser_id'],
    #         expiry_date = item['expiry_date'],
    #         status = item['status']
    #         )
    #     db.session.add(test)
    
    # for item in seed_object:
    #     seed_test(db,item)
    #     db.session.commit()

    # logger = logging.getLogger(__name__)
    # logger.info('seed finished')
    return True
