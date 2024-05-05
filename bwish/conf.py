import os
import pathlib

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
print(BASE_DIR)

dev_environment = os.getenv("dev_environment", 'True').lower() in ('true', '1', 't')
uat_environment = os.getenv("uat_environment", 'False').lower() in ('true', '1', 't')
live_environment = os.getenv("live_environment", 'False').lower() in ('true', '1', 't')
send_sms= os.getenv("send_sms", 'True').lower() in ('true', '1', 't')

if dev_environment:
    CSRF_TRUSTED_ORIGINS = ["http://localhost:5005"
                            ]
    CSRF_COOKIE_SECURE = False
    
elif uat_environment:
    CSRF_TRUSTED_ORIGINS = ["http://localhost:5005"
                            ]
    CSRF_COOKIE_SECURE = False
else:
    DEBUG_VAL = False
    CSRF_TRUSTED_ORIGINS = ["http://localhost:1337",
                            ]
    CSRF_COOKIE_SECURE = True