import re
def validate_phone(phone):
    phone_pattern = re.compile(r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$')
    phone=phone.replace(' ','')
    return  phone_pattern.match(phone)  is not None
def validate_name(name):
    name_pattern = re.compile(r'^[A-Za-zА-Яа-яЁё]+(?:\s[A-Za-zА-Яа-яЁё]+)*$')
    return name_pattern.match(name) is not None
    
def validate_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return  email_pattern.match(email)  is not None