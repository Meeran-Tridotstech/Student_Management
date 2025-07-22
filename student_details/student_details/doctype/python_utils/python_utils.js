// Copyright (c) 2025, Meeran Sheik and contributors
// For license information, please see license.txt

frappe.ui.form.on("Python Utils", {
	refresh(frm) {
        frm.add_custom_button("Python Utils",()=>{
            frappe.call({
                method : "student_details.student_details.doctype.python_utils.python_utils.python_utility",
                callback : (r)=>{
                    console.log(r.message)
                }
            })
        })
	},
});
