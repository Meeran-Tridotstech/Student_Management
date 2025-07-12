# Copyright (c) 2025, Meeran Sheik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PythonAPI(Document):
	pass
	#Realtime Event:
	# def before_save(self):
	# 	# frappe.msgprint("Helo")
	# 	frappe.publish_realtime("event_name",{
	# 		'message':'hello from the server',
	# 		'status':'Success'
	# 	})

	#Document Api:
	#------------
	#get_doc
	#------
    # def before_save(self):
        # try:
        #     doc = frappe.get_doc("Python API", "Py-API-0001")
        #     frappe.log_error(message=frappe.as_json(doc), title="PythonAPI Document")
        #     doc.title = 'Title Changed'

        # except Exception as e:
        #     frappe.log_error(message=str(e), title="PythonAPI Document")

	# get a single doctype:
	#----------------------
	# def before_save(self):
	# 	doc = frappe.get_doc("Single_docType")
	# 	frappe.msgprint("Single Doctype Get")
	# 	frappe.log_error(title="Single doctype GET",message = frappe.as_json(doc))


#Record created
#--------------
# @frappe.whitelist()
# def document_api():
# 	try:
# 		doc = frappe.get_doc({
# 			'doctype': 'Python API',
# 			'title': 'New Task'
# 		})
# 		frappe.log_error(title="get_doc", message=frappe.as_json(doc))
# 		doc.insert()
# 		return {"message": "Document inserted"}
# 	except Exception:
# 		frappe.log_error(title="document_api_error", message=frappe.get_traceback())
# 		frappe.throw("Failed to insert document.")


#Create With The New Field Name
#-----------------------------
# @frappe.whitelist()
# def document_api():
# 	try:
# 		doc = frappe.get_doc(doctype = "Python API",docname = "Py-API-0016",user_name="Meeran")
# 		frappe.log_error(title="get_doc", message=frappe.as_json(doc))
# 		doc.insert()
# 		return {"message": "Document inserted"}
# 	except Exception:
# 		frappe.log_error(title="document_api_error", message=frappe.get_traceback())
# 		frappe.throw("Failed to insert document.")


#Get the Last Document
# @frappe.whitelist()
# def document_api():
#     try:
#         doc = frappe.get_last_doc('Python API', filters={"Status": "Approved"})
#         frappe.log_error(title="get_doc", message=frappe.as_json(doc))
#         return {
#             "message": doc.name
#         }
#     except Exception:
#         frappe.log_error(title="document_api_error", message=frappe.get_traceback())
#         frappe.throw("Failed to fetch document.")

#frappe.get_cached_doc(It is not working)
#----------------------------------------
# @frappe.whitelist()
# def document_api():
#     try:
#         doc = frappe.get_doc('Python API')
#         return {
#             "message": doc.name
#         }
#     except Exception as e:
#         frappe.log_error(title="document_api_error", message=frappe.get_traceback())
#         frappe.throw("Failed to fetch document.")


#frappe.delete_doc(It is not working)
#---------------------------------
# @frappe.whitelist()
# def document_api():
#     try:
#         doc_name = "Py-API-0006"
#         frappe.delete_doc("Python API", doc_name, force=True)  # force=True bypasses permission checks
#         frappe.log_error(title="document_deleted", message=f"Deleted doc: {doc_name}")
#         return {
#             "message": f"Document {doc_name} deleted successfully"
#         }
#     except Exception:
#         frappe.log_error(title="document_api_error", message=frappe.get_traceback())
#         frappe.throw("Failed to delete document.")

#Allow Rename:
# @frappe.whitelist()
# def document_api():
#     try:
#         old_name = "Py-API-0008"
#         new_name = "TASK00003"
#         frappe.rename_doc("Python API", old_name, new_name)
#         frappe.log_error(title="document_renamed", message=f"Renamed doc from {old_name} to {new_name}")
#         return {
#             "message": f"Document renamed to {new_name} successfully"
#         }
#     except Exception:
#         frappe.log_error(title="document_api_error", message=frappe.get_traceback())
#         frappe.throw("Failed to rename document.")
