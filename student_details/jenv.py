import frappe

jenv = {
    "methods" : [
        "get_fullname:app.jinja.get_fullname"
    ],
    "filters" : [
        "format_currency:app.jinja.currency_filter"
    ]
}