import os
from django.core import signing

# 引入环境变量DjangoTest2.settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'DjangoTest2.settings'
value = signing.dumps({"foo":"bar"})
src = signing.loads(value)
print(value)
print(src)
print(type(src))

