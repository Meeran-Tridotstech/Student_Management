# Copyright (c) 2025, Meeran Sheik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student_Marks(Document):
    @frappe.whitelist()
    def student(self):
        # a = f"{self.student_name} : {self.subject} - {self.marks} ({self.status})"
        frappe.log_error(f"{self.student_name} : {self.subject} - {self.marks} ({self.status})", "hello")
        return f"Received Marks For {self.student_name} : {self.subject} - {self.marks} ({self.status})"