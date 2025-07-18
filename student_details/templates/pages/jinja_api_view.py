import frappe

def get_context(context):
    context.jinja_docs = frappe.get_all("Jinja API", fields=["name", "title", "description"])