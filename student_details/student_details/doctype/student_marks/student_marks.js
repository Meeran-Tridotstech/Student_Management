
frappe.ui.form.on("Student_Marks", {
    marks:function(frm) {
            if(frm.doc.marks >= 35) {
                frm.set_value('status','Pass');
                frappe.msgprint("This Student Is Passed");
            }
            else {
                frm.set_value('status','Fail');
                frappe.msgprint("This Student Is Failed");
            }
        } ,
       
        before_save: function(frm){
        if(frm.doc.marks==null){
            frappe.throw("fill the marks")
        }
       
    },
       
 
    refresh:function(frm) {
        frm.add_custom_button('Submit to Server', function() {
            if(!frm.doc.marks) {
                frappe.msgprint(__("Fill The Student Marks"));
                return;
            }
 
           frm.call({
            method: "student",
            doc: frm.doc,
            callback: function(r) {
                if (r.message) {
                    frappe.msgprint(r.message);
                }
            }
        });
 
        });
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