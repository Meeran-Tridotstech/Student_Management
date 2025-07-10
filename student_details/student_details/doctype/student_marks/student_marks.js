
frappe.ui.form.on("Student_Marks", {
    marks: function (frm) {
        if (frm.doc.marks >= 35) {
            frm.set_value('status', 'Pass');
            frappe.msgprint("This Student Is Passed");
        }
        else {
            frm.set_value('status', 'Fail');
            frappe.msgprint("This Student Is Failed");
        }
    },

    before_save: function (frm) {
        if (frm.doc.marks == null) {
            frappe.throw("fill the marks")
        }

    },


    refresh: function (frm) {
        frm.add_custom_button('Submit to Server', function () {
            if (!frm.doc.marks) {
                frappe.msgprint(__("Fill The Student Marks"));
                return;
            }

            frm.call({
                method: "student",
                doc: frm.doc,
                callback: function (r) {
                    if (r.message) {
                        frappe.msgprint(r.message);
                    }
                }
            });

        });


//Dialog API
//----------
        //1.Just warning
        // frm.add_custom_button("Dialog API", () => {
        //     frappe.msgprint({
        //         title: "Error",
        //         message: "This file does not exist",
        //         indicator: "red"
        //     });
        // });

        //2.Input Type:
        // frm.add_custom_button("Dialog API", () => {
        //     let d = new frappe.ui.Dialog({
        //         title: "Student Marks",
        //         fields: [
        //             { label: "First Name", fieldname: "first_name", fieldtype: "Data", reqd: true },
        //             { label: "Age", fieldname: "age", fieldtype: "Int" },
        //             { label: "Location", fieldname: "location", fieldtype: "Data" }
        //         ],
        //         primary_action_label: "Submit",
        //         primary_action(values) {
        //             if (!values.first_name || !values.age || !values.location) {
        //                 frappe.msgprint("All fields are mandatory.");
        //                 return;
        //             }

        //             frappe.confirm("Are you sure you want to submit?", () => {
        //                 console.log("Submitted values:", values);
        //                 frappe.msgprint("Thanks for submitting!");
        //                 d.hide();
        //             });
        //         },
        //         is_wide: true
        //     });

        //     d.show();
        // });


//SOCKET -IO: (Not Complete Yet)
//-----------
        // frappe.realtime.on("custom_event",()=>{
        //     console.log("custom_event happed in backend")
        //     frappe.msgprint("custom_event")
        // })



    }

});



// frappe.ui.form.on("Student_Marks", {
// 	refresh(frm) {

//         frm.add_custom_button("BUTTON 1",()=>{
//         // frappe.set_route("list","Student_Marks")     //Nvigate to the Listview Page
//         // frappe.set_route("app/student_marks/SD0007")   //Path Is set
//         frappe.set_route("list","Student_Marks",filter={'status':'Pass'})

//     })
//     },

// });