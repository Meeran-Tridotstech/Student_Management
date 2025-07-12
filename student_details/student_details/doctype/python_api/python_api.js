// Copyright (c) 2025, Meeran Sheik and contributors
// For license information, please see license.txt

frappe.ui.form.on("Python API", {
    refresh(frm) {

        //Realtime Event:
        //-------------
        // frappe.realtime.on('event_name',(data)=>{
        //     console.log(data)
        // })
    console.log(frm)
        frm.add_custom_button("Document API", () => {
            frappe.call({
                method: "student_details.student_details.doctype.python_api.python_api.document_api",
                callback: (r) => {
                    if (!r.exc) {
                        frappe.msgprint(r.message);
                    }
                }
            });
        });
    },
});
