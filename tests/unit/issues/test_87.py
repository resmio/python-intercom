# # -*- coding: utf-8 -*-

# # import json
# # import time
# import unittest

# # from datetime import datetime
# from intercom.request import Request
# from intercom import User
# from mock import Mock
# # from nose.tools import eq_
# # from nose.tools import ok_
# from nose.tools import istest


# API_RESPONSE = bytes("""
# {
#     "type": "user",
#     "id": "xxx",
#     "user_id": "602",
#     "anonymous": false,
#     "email": "bob@example.com",
#     "name": null,
#     "pseudonym": null,
#     "avatar": {
#         "type": "avatar",
#         "image_url": null
#     },
#     "app_id": "xxx",
#     "companies": {
#         "type": "company.list",
#         "companies": [
#             {
#                 "type": "company",
#                 "company_id": "599",
#                 "id": "xxx",
#                 "name": "example"
#             }
#         ]
#     },
#     "location_data": {
#         "type": "location_data",
#         "city_name": "Fürth",
#         "continent_code": "EU",
#         "country_name": "Germany",
#         "latitude": "xx",
#         "longitude": "xx",
#         "postal_code": "xx",
#         "region_name": "Bayern",
#         "timezone": "Europe/Berlin",
#         "country_code": "DEU"
#     },
#     "last_request_at": 1428333010,
#     "last_seen_ip": "xxx",
#     "created_at": 1428006179,
#     "remote_created_at": 1428009744,
#     "signed_up_at": 1428009744,
#     "updated_at": 1429249406,
#     "session_count": 21,
#     "social_profiles": {
#         "type": "social_profile.list",
#         "social_profiles": []
#     },
#     "unsubscribed_from_emails": false,
#     "user_agent_data": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:37.0) Gecko/20100101 Firefox/37.0",
#     "tags": {
#         "type": "tag.list",
#         "tags": []
#     },
#     "segments": {
#         "type": "segment.list",
#         "segments": [
#             {
#                 "type": "segment",
#                 "id": "xxx"
#             },
#             {
#                 "type": "segment",
#                 "id": "xxx"
#             },
#             {
#                 "type": "segment",
#                 "id": "xxx"
#             }
#         ]
#     },
#     "custom_attributes": {
#         "Active": true,
#         "Email Activated": true,
#         "Staff": false
#     }
# }
# """, "utf-8")

# API_RESPONSE_2 = bytes("""
# {
#     "type": "user",
#     "id": "xxx",
#     "user_id": "10",
#     "anonymous": false,
#     "email": "another@example.com",
#     "name": null,
#     "pseudonym": null,
#     "avatar": {
#         "type": "avatar",
#         "image_url": "xxx"
#     },
#     "app_id": "xxx",
#     "companies": {
#         "type": "company.list",
#         "companies": [
#             {
#                 "type": "company",
#                 "company_id": "7",
#                 "id": "xxx",
#                 "name": "example"
#             }
#         ]
#     },
#     "location_data": {
#         "type": "location_data",
#         "city_name": "Polokwane",
#         "continent_code": "AF",
#         "country_name": "South Africa",
#         "latitude": "xxx",
#         "longitude": "xxx",
#         "postal_code": "xxx",
#         "region_name": "Limpopo",
#         "timezone": "Africa/Johannesburg",
#         "country_code": "ZAF"
#     },
#     "last_request_at": 1428599261,
#     "last_seen_ip": "xxx",
#     "created_at": 1426769458,
#     "remote_created_at": 1407336095,
#     "signed_up_at": 1407336095,
#     "updated_at": 1429248896,
#     "session_count": 3,
#     "social_profiles": {
#         "type": "social_profile.list",
#         "social_profiles": []
#     },
#     "unsubscribed_from_emails": false,
#     "user_agent_data": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36",
#     "tags": {
#         "type": "tag.list",
#         "tags": []
#     },
#     "segments": {
#         "type": "segment.list",
#         "segments": [
#             {
#                 "type": "segment",
#                 "id": "xxx"
#             },
#             {
#                 "type": "segment",
#                 "id": "xxx"
#             },
#             {
#                 "type": "segment",
#                 "id": "xxx"
#             }
#         ]
#     },
#     "custom_attributes": {
#         "is_active": true,
#         "email_activated": true,
#         "is_staff": false,
#         "Email Activated": true,
#         "Active": true,
#         "Staff": false
#     }
# }
# """, "utf-8")


# class UserTest(unittest.TestCase):

#     def setUp(self):  # noqa
#         response = Mock()
#         response.content = API_RESPONSE
#         response.encoding = 'utf-8'
#         response.status_code = 200
#         self.response = response

#     @istest
#     def it_to_dict_itself(self):
#         body = Request.parse_body(self.response)
#         user = User.create(response=body)
#         print(user.location_data.city_name)
