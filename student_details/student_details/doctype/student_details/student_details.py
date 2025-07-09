# Copyright (c) 2025, Meeran Sheik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student_Details(Document):
	pass
# @frappe.whitelist()
# def get_data(std_id):
# 	data = frappe.get_doc("Student_Details", std_id)
# 	filter_data = {
# 		"first": data.first_name,
# 		"last": data.last_name,
# 		"age": data.dob,
# 		"mobile": data.mobile_number
# 	}
# 	return filter_data
# 	frappe.log_error(message=str(filter_data), title="Student Info Debug")