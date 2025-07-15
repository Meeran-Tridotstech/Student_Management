# Copyright (c) 2025, Meeran Sheik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PythonAPI(Document):
	pass
	# # Realtime Event:
	# def before_save(self):
	# 	frappe.publish_realtime("event_name", {
	# 		"message": "hello from the server",
	# 		"status": "Success"
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
#-----------------------------------
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


#frappe.get_meta():
# @frappe.whitelist()
# def document_api():
# 	try:
# 		meta = frappe.get_meta('Python API')
# 		val1=meta.has_field('status')
# 		val2=meta.get_custom_fields()
# 		frappe.log_error(title = "Documemnt API",message = f" This is {val1} and \n this is {val2}")
# 	except Exception as e:
# 		frappe.log_error(title = "Document_api",message = e)

#Doc.insert(): #Mandatory it is not work
# @frappe.whitelist()
# def document_api():
# 	try:
# 		doc = frappe.new_doc("Python API")
# 		doc.user_name = "Meeran"
# 		val= doc.insert(ignore_mandatory = False)
# 		frappe.log_error(title = "Documemnt API",message = f" This is {val}")
# 	except Exception as e:
# 		frappe.log_error(title = "Document_api",message = e)


#Doc.insert
# @frappe.whitelist()
# def document_api():
# 	try:
# 		before_save()
# 	except Exception as e:
# 		frappe.log_error(title = "Document_api",message = e)

# def before_save():
# 	try:
# 		doc = frappe.new_doc("Python API")
# 		doc.mail_id = "meeran@gmail.com"
# 		val= doc.insert(ignore_mandatory = False)
# 		frappe.log_error(title = "Documemnt API",message = f" This is {val}")
# 	except:
# 		frappe.log_error(title = "Document_api",message = e)



#doc.delete()
# @frappe.whitelist()
# def document_api():
#     try:
#         doc = frappe.get_doc("Python API", "Py-API-0011")
#         doc.delete()
#         frappe.msgprint(f"Document Name is: {doc.name}")
#     except Exception as e:
#         frappe.msgprint(str(e))


#doc.get_doc_before_save() #It is not worked
# @frappe.whitelist()
# def document_api():
#     try:
#         doc = frappe.get_doc("Python API", "Py-API-0003")
#         old_doc = doc.get_doc_before_save()

#         # Displaying old document details
#         frappe.msgprint(f"Old doc username: {old_doc.user_name}")

#         # Comparing values to check for changes
#         if old_doc.user_name != doc.user_name:
#             frappe.msgprint(f"Username changed from {old_doc.user_name} to {doc.user_name}")
        
#     except Exception as e:
#         frappe.msgprint(str(e))




#doc.has_value_changed Retur (True)
# @frappe.whitelist()
# def document_api():
# 	try:
# 		doc = frappe.get_doc("Python API", "Py-API-0003")
# 		field_changed = doc.has_value_changed("user_name")
# 		if field_changed:
# 			frappe.msgprint("True")
# 	except Exception as e:
# 		frappe.msgprint(str(e))



#doc.reload:
# @frappe.whitelist()
# def document_api():
#     try:
#         doc = frappe.get_doc("Python API", "Py-API-0003")
#         doc.reload()  # No need to assign result; reload updates the object in-place

#         frappe.msgprint(f"Reloaded Document: {doc.name}")
        
#     except Exception as e:
#         frappe.msgprint(str(e))



#doc.check_permission(permtype='write')
# @frappe.whitelist()
# def document_api():
#     try:
#         doc = frappe.get_doc("Python API", "Py-API-0004")
#         doc.check_permission(permtype='write')
#         doc.save()
#         frappe.msgprint("You have write access to this document.")
#     except frappe.PermissionError:
#         frappe.msgprint("You don't have write access to this document.")
#     except Exception as e:
#         frappe.msgprint(f"An unexpected error occurred: {str(e)}")



#title = doc.get_title()
# @frappe.whitelist()
# def document_api():
#     try:
#         doc = frappe.get_doc("Python API", "Py-API-0004")
#         doc.notify_update()  # Not meant to return anything
        
#         frappe.msgprint(f"Document '{doc.name}' update notification triggered.")
#     except Exception as e:
#         frappe.msgprint(f"Error: {str(e)}")



#doc.db_set
# @frappe.whitelist()
# def document_api():
#     try:
#         doc = frappe.get_doc("Python API", "Py-API-0004")
#         doc.db_set("user_name", "Sheik", notify=True)
#         frappe.msgprint(f"Document '{doc.name}' has been updated with user_name = 'Sheik'")
#     except Exception as e:
#         frappe.msgprint(f"Error: {frappe.get_traceback()}")




#doc.append(): #The Child Table Value has been added
# @frappe.whitelist()
# def document_api():
#     try:
#         doc = frappe.get_doc("Python API", "Py-API-0013")
#         # Appending to the child table
#         doc.append("table_xcrk", {
#             "name1": "Meeran",
#             "age": "39",
#             "loaction": "kayalpatinam"
#         })

#         # Save the updated document
#         doc.save()
#         frappe.msgprint(" Child table value has been added.")
#     except Exception as e:
#         frappe.msgprint(f"Child table value was not added: {str(e)}")




#doc.get_url()
# @frappe.whitelist()
# def document_api():
# 	doc = frappe.get_doc("Python API","Py-API-0013")
# 	url = doc.get_url()
# 	frappe.msgprint("Get the URL : "+url)


#doc.add_comment()
# @frappe.whitelist()
# def document_api():
# 	doc = frappe.get_doc("Python API","Py-API-0013")
# 	# comment = doc.add_comment("Comment",text = "This is my First Comment")
# 	comment = doc.add_comment("Edit","Values changed")
# 	frappe.msgprint("Comment : "+ comment)


#doc.run_method('validate')
# @frappe.whitelist()
# def document_api():
#     doc = frappe.get_doc("Python API", "Py-API-0013")
#     doc.run_method('validate')
#     frappe.msgprint(f"Validation completed for document: {doc.name}")


#frappe.send_email()
@frappe.whitelist()
def document_api(self,emails,message):
	for email in emails:
		frappe.sendmail(recipients = email,subject = f"Notification from {self.name}",
		message =  message,
		reference_doctype = self.doctype,
		reference_name = self.name
		)
	return f"Emails  sent to :{','.join(emails)}"

doc = frappe.get_doc("Python API", "Py-API-0009")
email_list = ["meeran@example.com", "sheik@example.com"]

# Queue the task to send emails
doc.queue_action('document_api', emails=email_list, message="Howdy from the server!")