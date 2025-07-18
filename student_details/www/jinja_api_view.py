import frappe
 
 
# All records of the Jinja API(DocTyep)
def get_context(context):
    context.jinja_docs = frappe.get_all(
        "Jinja API",
        fields=["user_name", "mail","password", "status","name",]
    )
 