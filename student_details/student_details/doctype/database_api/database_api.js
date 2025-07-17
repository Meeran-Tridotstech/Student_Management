// Copyright (c) 2025, Meeran Sheik and contributors
// For license information, please see license.txt

frappe.ui.form.on("Database API", {
    refresh(frm) {
        frm.add_custom_button("DB API", () => {
            frappe.call({
                method: "student_details.student_details.doctype.database_api.database_api.db_api",
                callback: (r) => {
                    if (!r.exc) {
                        frappe.msgprint(r.message)
                    }
                }
            })
        })
    },
});
