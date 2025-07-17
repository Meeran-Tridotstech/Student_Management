# Copyright (c) 2025, Meeran Sheik and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DatabaseAPI(Document):
	pass

#get_list()		#Worked Only Outof the Class
# @frappe.whitelist()
# def db_api():
# 	doc_list = frappe.get_list("Database API", fields=["name"])
# 	frappe.msgprint(f"All Records {doc_list} and Number of Records {len(doc_list)}.")


#get_list() using Pluck
# @frappe.whitelist()
# def db_api():
# 	doc = frappe.get_list("Database API",pluck = "name")
# 	frappe.msgprint(f"Only Records Name...{doc}")


#Combining filters and other arguments:[Date,Between,Like,Count]
# @frappe.whitelist()
# def db_api():
	# doc = frappe.db.get_list("Database API", filters={'status':'fail'},fields = ['user_name','password'])
	# frappe.log_error(title = "Database" , message = f"get_list {doc}")
	# frappe.msgprint(f"Records Status is Failed : {doc}")

	#Date:
	# date = frappe.db.get_list("Database API",filters={
	# 	'date' :['<=','2025-04-15']
	# })
	# frappe.msgprint(f"Particular records : {date}")


	#Between:
	# between = frappe.db.get_list(
    # "Database API",
    # filters={
    #     "date": ["between", ["2025-04-01", "2025-07-07"]]
    # },
    # fields=["user_name"]
	# )
	# frappe.msgprint(f"Between records '2025-04-01' to '2025-07-07': {between}")


	#Like:
	# like = frappe.db.get_list(
    # "Database API",
    # filters={'user_name': ['like', 's%']},
    # fields=["user_name"]
	# )
	# matched_users = [entry["user_name"] for entry in like]
	# frappe.msgprint(f"Starting Letter 'S':\n" + "\n".join(matched_users))


	#Count:
	# count = frappe.db.get_list("Database API",
	# fields = ['count(name) as count','status'],
	# group_by = 'status'
	# )
	# status_count = [entry['status'] for entry in count]
	# frappe.msgprint(f"Count: {status_count} :{count} ")

	#Count another way
	# result = frappe.db.sql("""
	# 	SELECT status, COUNT(name) AS count
	# 	FROM `tabDatabase API`
	# 	GROUP BY status
	# """, as_dict=True)

	# msg = "\n".join([f"{row['status']}: {row['count']}" for row in result])
	# frappe.msgprint(f"Status Counts:\n{msg}")


#farppe.db.get_value():
# @frappe.whitelist()
# def db_api():
	#Get the Single field value
	# get_value = frappe.db.get_value("Database API","DB-0005","user_name") 
	# frappe.msgprint(f"Get Value of User name:\n{get_value}")


	#Got the multiple value
	# get_multiple_val = frappe.db.get_value('Database API',"DB-0005",['user_name','password'])
	# frappe.log_error(title = "DB error", message = f"{get_multiple_val}")
	# frappe.msgprint(f"Get Value of User name:\n{ get_multiple_val }")

	#Got the multiple value(with (as_dict()))
	# get_multiple_val = frappe.db.get_value('Database API',"DB-0005",['user_name','password'],as_dict=True)  #Got the multiple value
	# val1 = get_multiple_val.user_name
	# val2 = get_multiple_val.password
	# frappe.msgprint("User Name : "+val1)
	# frappe.msgprint("User Name : "+val2)

	# with filters, will return the first record that matches filters
	# first_record,second_record = frappe.db.get_value("Database API",{"status":'fail'},["user_name","password"])
	# frappe.msgprint(f"first_record : {first_record} and {second_record}")



#frappe.db.get_single_value()	#It is not worked
# @frappe.whitelist()
# def db_api():
# 	single_value = frappe.db.get_single_value('Single_docType','name1')
# 	frappe.msgprint("Single Doc type Value : ",single_value)


# frappe.db.set_value() and Refresh the page
# @frappe.whitelist()
# def db_api():
	#Chage the user_name
	# value = frappe.db.set_value('Database API',"DB-0005",'user_name','Gokul')


	# Update multiple values
	# frappe.db.set_value('Database API', 'DB-0005', {
	# 	'user_name': 'Raju',
	# 	'password': '23456789'
	# })
	# user_info = frappe.db.get_value('Database API', 'DB-0005', ['user_name', 'password'], as_dict=True)
	# frappe.msgprint(f"User Name  : {user_info.user_name}\nPassword   : {user_info.password}")


	#without update modify timestamp
	# frappe.db.set_value("Database API","DB-0005","user_name","Suresh",update_modified = False)


#frappe.db.exists()
# @frappe.whitelist()
# def db_api():
	#If Records check
# 	val = frappe.db.exists("Database API",'DB-0050')
# 	if val:
# 		frappe.msgprint()
# 	else:
# 		frappe.msgprint("False")


	#If particular fields are check
	# val = frappe.db.exists({
	# 	"doctype" : "Database API",
	# 	"user_name" : "Mee",
	# })
	# if val:
	# 	frappe.msgprint("Data Exist")
	# else:
	# 	frappe.msgprint("Data Not Exist")



#frappe.db.count()
# @frappe.whitelist()
# def db_api():
# 	val = frappe.db.count('Database API')
# 	frappe.msgprint("Total Database Count :"+str(val))


#frappe.db.delete()		#Not worked
@frappe.whitelist()
def db_api():
    # Identify latest record to keep for user 'Nithish'
    last_record_to_keep = frappe.get_list("Database API",
        filters={"user_name": "Nithish"},
        fields=["user_name", "modified"],
        order_by="modified desc",
        limit=1
    )

    if not last_record_to_keep:
        frappe.throw("No record found to retain. Deletion aborted.")

    cutoff = last_record_to_keep[0]['modified']

    frappe.log_error(
        title="Delete the Particular records",
        message=f"Deleting records for Nithish before: {cutoff}"
    )

    frappe.db.delete("Database API", {
        "modified": ("<", cutoff),
        "user_name": "Nithish"
    })

    return {"status": "success", "cutoff": cutoff}

