# Copyright (c) 2025, Meeran Sheik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import frappe
import json
from frappe.model.document import Document
from frappe.utils import now
from frappe.utils import getdate
from frappe.utils import today
from frappe.utils import get_datetime
from datetime import datetime
from frappe.utils import add_to_date
from frappe.utils import date_diff
from frappe.utils import days_diff
from frappe.utils import month_diff
from frappe.utils import pretty_date
from frappe.utils import format_duration
from frappe.utils import comma_and
from frappe.utils import money_in_words
from frappe.utils import validate_json_string
from frappe.utils import random_string
from frappe.utils import unique
from frappe.utils.pdf import get_pdf
from frappe.utils import get_abbr
from frappe.utils import validate_url
from frappe.utils import validate_email_address
from frappe.utils import validate_phone_number
from frappe import _, get_all
from frappe.utils import nowdate


class PythonUtils(Document):
	pass
 
 
# @frappe.whitelist()
# def python_utility():
# Utility Functions
# now()
    # data = now()
    # frappe.msgprint(f"This is a Python utility function now(): {data}")
# ----------------------------------------------------------------------------------------------------------------
# getdate
    # data = getdate()
    # frappe.msgprint(f"This is a Python utility function getdate(): {data}")
# ----------------------------------------------------------------------------------------------------------------
# today
    # data = today()
    # frappe.msgprint(f"This is a Python utility function today(): {data}")
# ----------------------------------------------------------------------------------------------------------------
# add_to_date calculate the current now()
    # today = datetime.now().strftime('%Y-%m-%d')
    # frappe.msgprint(f"This is a Python utility function add_to_date(): {today}")
 
    # after_10_days = add_to_date(datetime.now(), days=10, as_string=True)
    # frappe.msgprint(f"This is a Python utility function add_to_date(): {after_10_days}")
 
    # after_2_months = add_to_date(datetime.now(), months=2)
    # frappe.msgprint(f"This is a Python utility function add_to_date(): {after_2_months}")
 
    # after_10_days_datetime = add_to_date(datetime.now(), days=10, as_string=True, as_datetime=True)
    # frappe.msgprint(f"This is a Python utility function add_to_date(): {after_10_days_datetime}")
 
    # after_2_years = add_to_date(None, years=2)
    # frappe.msgprint(f"This is a Python utility function add_to_date(): {after_2_years} ")
# ----------------------------------------------------------------------------------------------------------------
# date_diff today + 10 days =>date_diff(date_2, date_1)=>10
    # date_1 = today()
    # date_2 = add_to_date(date_1, days=10)
    # date_diff_data = date_diff(date_2, date_1)
    # frappe.msgprint(f"This is a Python utility function date_diff(): {date_diff_data} days")
# ----------------------------------------------------------------------------------------------------------------
# days_diff days like mon,tue,wed
    # date_1 = today()
    # date_2 = add_to_date(date_1, days=5)
    # days_diff_data = days_diff(date_2, date_1)
    # frappe.msgprint(f"This is a Python utility function days_diff(): {days_diff_data} days")
# ----------------------------------------------------------------------------------------------------------------
# month_diff
    # date_1 = today()
    # date_2 = add_to_date(date_1, days=30)
    # month_diff_data = month_diff(date_2, date_1)
    # frappe.msgprint(f"This is a Python utility function month_diff(): {month_diff_data} months")
# ----------------------------------------------------------------------------------------------------------------
# pretty_date now() → Gets current date & time -> Converts that into a friendly format -> get_datetime->"2025-07-25" → datetime.datetime(2025, 7, 25, 0, 0)
    # date_1 = today()
    # data = pretty_date(get_datetime(date_1))
    # frappe.msgprint(f"This is a Python utility function pretty_date(): {data}")
 
    # date_1 = today()
    # date_2 = add_to_date(date_1, days=10)
    # data = pretty_date(get_datetime(date_2))  
    # frappe.msgprint(f"This is a Python utility function pretty_date(): {data} ")
# ----------------------------------------------------------------------------------------------------------------
# format_duration 60 sec = 1 minutes, 5000 sec = 1h 23m 20s, 1000000 sec = 11d 13h 46m 40s ,1000000 sec = 277h 46m 40s
    # format_duration_data = format_duration(120)
    # frappe.msgprint(f"This is a Python utility function format_duration(): {format_duration_data}")
 
    # format_duration_data = format_duration(5000)
    # frappe.msgprint(f"This is a Python utility function format_duration(): {format_duration_data}")
 
    # format_duration_data = format_duration(1000000)
    # frappe.msgprint(f"This is a Python utility function format_duration(): {format_duration_data}")
 
    # format_duration_data = format_duration(1000000, hide_days=True)
    # frappe.msgprint(f"This is a Python utility function format_duration(): {format_duration_data}")
# ----------------------------------------------------------------------------------------------------------------
# comma_and
    # comma_and_data = comma_and(['1','2','3','4'])
    # frappe.msgprint(f"This is a Python utility function comma_and(): {comma_and_data}")
 
    # comma_and_data = comma_and(['Apple','Orange','Banana'], add_quotes=True)
    # frappe.msgprint(f"This is a Python utility function comma_and(): {comma_and_data}")
 
    # comma_and_data = comma_and('abcd')
    # frappe.msgprint(f"This is a Python utility function comma_and(): {comma_and_data}")
# ----------------------------------------------------------------------------------------------------------------
# money_in_words USA->USD, India->INR, UK->GBP, Japan->JPY, China->CNY
    # money_in_data = money_in_words(100)
    # frappe.msgprint(f"This is a Python utility function money_in_words(): {money_in_data}")
 
    # money_in_data = money_in_words(500.50)
    # frappe.msgprint(f"This is a Python utility function money_in_words(): {money_in_data}")
 
    # money_in_data = money_in_words(900.50,'USD')
    # frappe.msgprint(f"This is a Python utility function money_in_words(): {money_in_data}")
 
    # money_in_data = money_in_words(900.50, 'USD', 'Cents')
    # frappe.msgprint(f"This is a Python utility function money_in_words(): {money_in_data}")
# ----------------------------------------------------------------------------------------------------------------
# validate_json_string  not working
    # json_data = '{"name":"imran", "age": "67"}'
    # json_validate = validate_json_string(json_data)
    # frappe.msgprint(f"This is a Python utility function validate_json_string(): {json_validate}")
# ----------------------------------------------------------------------------------------------------------------
# random_string
    # random_string_data = random_string(40)
    # frappe.msgprint(f"This is a Python utility function random_string(): {random_string_data}")
 
    # random_string_data = random_string(5)
    # frappe.msgprint(f"This is a Python utility function random_string(): {random_string_data}")
# ----------------------------------------------------------------------------------------------------------------
# unique
    # unique_data = unique(['1','2','3','1','1','1','2'])
    # frappe.msgprint(f"This is a Python utility function unique(): {unique_data}")
 
    # unique_data = unique('adgfdgfdhh')
    # frappe.msgprint(f"This is a Python utility function unique(): {unique_data}")
 
    # unique_data = unique(('Apple', 'Apple', 'Banana', 'Apple'))
    # frappe.msgprint(f"This is a Python utility function unique(): {unique_data}")
# ----------------------------------------------------------------------------------------------------------------
# get_pdf
    # cart = {
    #     'Samsung Galaxy s20': 10,
    #     'iphone 13': 80,
    #     'Redmi 13C': 50,
    #     'Vivo': 40,
    #     'Nokia': 80
    # }
 
    # html = '<h1>Invoice from Star Electronics e-store!</h1><ol>'
    # for item, qty in cart.items():
    #     html += f'<li>{item} - {qty}</li>'
    # html += '</ol>'
 
    # pdf = get_pdf(html)
    # timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    # file_doc = frappe.get_doc({
    #   "doctype": "File",
    #   "file_name": f"invoice_{timestamp}.pdf",
    #   "content": pdf,
    #   "is_private": 0
    # }).insert(ignore_permissions=True)
    # return file_doc.file_url
# ----------------------------------------------------------------------------------------------------------------
# get_abbr
    # get_abbr_data = get_abbr('meeran' , max_len=3)
    # return get_abbr_data
 
    # get_abbr_data = get_abbr('This is saba', max_len=4)
    # return get_abbr_data
 
    #  get_abbr_data = get_abbr('Mohammad Hussain Nagaria Frappe', max_len=4)
    #  return get_abbr_data
# ----------------------------------------------------------------------------------------------------------------
# validate_url
    # validate_url_data = validate_url('google')
    # return validate_url_data
 
    # validate_url_data = validate_url('https:google')
    # return validate_url_data
 
    # validate_url_data = validate_url('w:google.com', throw=True)
    # return validate_url_data
# ----------------------------------------------------------------------------------------------------------------
# validate_email_address
# Single valid email address
    # validate_email_address_data = validate_email_address('meeran@gmail.com')
    # return validate_email_address_data
 
    # validate_email_address_data = validate_email_address('other text, meeran@erpnext.com, some other text')
    # return validate_email_address_data
 
# Multiple valid email address
    # validate_email_address_data = validate_email_address('some text, meeran@erpnext.com, some other text, frappe@erpnext.com, yet another no-emailic phrase.')
    # return validate_email_address_data
 
# Invalid email address
    #  validate_email_address_data = validate_email_address('meeran@erpnext.ac.in')
    #  return validate_email_address_data
# ----------------------------------------------------------------------------------------------------------------
# validate_phone_number
# Valid phone numbers
    # validate_phone_number_data = validate_phone_number('753858375')
    # return validate_phone_number_data
 
    # validate_phone_number_data = validate_phone_number('+753858375787877')
    # return validate_phone_number_data
 
    # validate_phone_number_data = validate_phone_number('invalid')
    # return validate_phone_number_data
 
    # validate_phone_number_data = validate_phone_number('87345%%', throw=True)
    # return validate_phone_number_data
# ----------------------------------------------------------------------------------------------------------------
# frappe.cache()
    # cache = frappe.cache()
    # set_cache = cache.set('name', 'meeran')
    # get_cache = cache.get('name')
 
 
    # data = {
    # 'name': 'meeran',
    # 'age': 25,
    # 'city': 'chennai'
    # }
 
    # cache.set('user_info', json.dumps(data))  
    # user_info = json.loads(cache.get('user_info'))
    # print(user_info['age'])  
# -------------------------------------------------------------------------------------------------------------
 
 #frappe.sendmail()
@frappe.whitelist()
def python_utility():
    recipients = ['meeranf36@gmail.com']
    today = nowdate()

    birthday_employees = frappe.get_all(
        "Employee",
        filters={"date_of_birth": today},
        fields=["employee_name"]
    )

    birthday_persons = [emp.employee_name for emp in birthday_employees]

    if birthday_persons:
        frappe.sendmail(
            recipients=recipients,
            subject=_('Birthday Reminder'),
            template='birthday_reminder',  # filename without .html
            args=dict(
                reminder_text="Here's who you need to celebrate today 🎉",
                birthday_persons=birthday_persons,
                message="Make it extra special with a surprise or kind words!"
            ),
            headers={"Custom-Header": _("Birthday Reminder")}
        )
