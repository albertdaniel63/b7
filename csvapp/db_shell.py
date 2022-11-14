from csvapp.models import Csv_emp
import random
import string
# exec(open('G:\Python\Practice_python\csv_gen\csvapp\db_shell.py').read())
'''
des = ['Software Engineer','Sr. Software Engineer','Python Developer','linux administrator','CEO','Data scientist']

for i in range(50):
    letters = string.ascii_lowercase
    nam = ''.join(random.choice(letters) for i in range(10))

    digits = string.digits
    sal = ''.join(random.choice(digits) for i in range(5))
    
    letters = string.ascii_uppercase
    comp = ''.join(random.choice(letters) for i in range(10))

    desgn = random.choice(des)

    emp = Csv_emp(name = nam, company = comp, salary = sal, designation = desgn)
    emp.save()
'''
from django.core.mail import send_mail
from django.conf import settings
send_mail(
    subject='A cool subject',    
    message='A stunning message',
    from_email=settings.EMAIL_HOST_USER,    
    recipient_list=[settings.RECIPIENT_ADDRESS])
1
