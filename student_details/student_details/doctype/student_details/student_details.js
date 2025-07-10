// Copyright (c) 2025, Meeran Sheik and contributors
// For license information, please see license.txt


// GET DATA(get_route)
//--------------------
frappe.ui.form.on("Student_Details", {
	refresh(frm) {
        //Utilities API
        //-------------
        // frm.add_custom_button("GET Route",()=>{
        //     let route = frappe.get_route();
        //     // console.log(route)
        //     student_id=route[2]
        //     // console.log(student_id)
        //     frappe.call({
        //         method:"student_details.student_details.doctype.student_details.student_details.get_data",
        //         args:{
        //             std_id:student_id,
        //         },
        //         callback:function(r){
        //             console.log(r)
        //             msgprint("Student Details:"+JSON.stringify(r.message))
        //         }
        //     })
        // })

    //SET ROUTE():
    //-----------
    // frm.add_custom_button("BUTTON 1",()=>{
    //     // frappe.set_route("list","Student_Marks")     //Nvigate to the Listview Page
    //     // frappe.set_route("app/student_marks/SD0007")   //Path Is set
    //     frappe.set_route("list","Student_Marks",filter={'status':'Pass'})
    // })


    //Page API:
    //--------
    frm.add_custom_button("Page API",()=>{
        let page = frappe.ui.make_app_page({
            title:"My Page",
            parent : wrapper,
            single_column : true,
        })
        page.set_title("My Page")
    })




    },

});