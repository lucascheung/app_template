import json
from flask import jsonify, request
from exts import db


# def get_tests():
#     methods = ['GET']
#     status, data = get_tests_helper()
#     response_object = {
#         'status': status,
#         'code': 20000,
#         'data': data
#         }
#     return jsonify(response_object)

# def create_test():
#     try:
#         methods = ['POST']
#         payload = request.get_json()
#         status, message = create_test_helper(payload)
#         response_object = {
#             'status': status,
#             'code': 20000,
#             'message': message
#             }
#         return jsonify(response_object)
#     except Exception as e:
#         print(str(e))


# # ========================HELPER METHODS BELOW==========================
# def get_tests_helper():
#     tests = []
#     user_tests = db.session.query(Test).all()

#     return "success", user_tests

# def create_test_helper(payload):
#     expiry_date_timestamp = format_timestamp(payload.get('expiry_date'))
#     payload['expiry_date'] = expiry_date_timestamp
#     # Make RPC call
#     addstudy_status, message = add_study(payload)

#     if addstudy_status == "success":
#         test_id = message['id']
#         if message['id'] == 0:
#             return "failed", message['BaseResp']['StatusMessage']
#         pl = {"test_id": test_id}
#         openstudy_status, message = open_study(pl)
#         if openstudy_status == "success":
#             # Write into DB
#             now = datetime.now()
#             now_timestamp = datetime.strftime(now,'%Y-%m-%dT%H:%M:%SZ')
#             print(test_id)
#             new_test = Test(
#                 test_id = int(test_id),
#                 name = payload.get('name'),
#                 test_groups = payload.get('test_groups'),
#                 advertiser_id = payload.get('advertiser_id'),
#                 split_details = json.dumps(payload.get('split_details')),
#                 expiry_date = expiry_date_timestamp,
#                 created_at = now_timestamp,
#                 created_by = str(cas.attributes['cas:employee_id']),
#                 status = 1
#             )
#             db.session.add(new_test)
#             db.session.commit()
#             return "success", message
#         else:
#            return "failed", message
#     else:
#         return "failed", message



# def find_test(test_id):
#     test = Test.query.filter(Test.test_id==test_id).first_or_404()
#     return test
