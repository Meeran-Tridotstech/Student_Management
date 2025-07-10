// frappe.pages['student-details-page'].on_page_load = function (wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Student',
// 		single_column: true
// 	});

// 	page.set_title('My Page')
// 	page.set_indicator('Pending', 'orange')
// 	// page.clear_indicater()
// 	// let $btn = page.set_primary_action('New', () => create_new(), 'octicon octicon-plus')

// 	let $btn = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync')

// 	// add a normal menu item
// 	page.add_menu_item('Send Email', () => open_email_dialog())

// 	// add a standard menu item
// 	page.add_menu_item('Send Email', () => open_email_dialog(), true)

// 	// add a normal menu item
// 	page.add_action_item('Delete', () => delete_items())

// 	// add a normal inner button
// 	page.add_inner_button('Update Posts', () => update_posts())
// 	// add a dropdown button in a group
// 	page.add_inner_button('New Post', () => new_post(), 'Make')
// 	// change type of ungrouped button
// 	page.change_inner_button_type('Update Posts', null, 'primary');

// 	// change type of a button in a group
// 	page.change_inner_button_type('Delete Posts', 'Actions', 'danger');

// 	// remove inner button
// 	// page.remove_inner_button('Update Posts')

// 	// // remove dropdown button in a group
// 	// page.remove_inner_button('New Posts', 'Make')


// 	let field = page.add_field({
// 		label: 'Status',
// 		fieldtype: 'Select',
// 		fieldname: 'status',
// 		options: [
// 			'Open',
// 			'Closed',
// 			'Cancelled'
// 		],
// 		change() {
// 			console.log(field.get_value());
// 		}
// 	});


// 	let values = page.get_form_values()
// 	// { status: 'Open', priority: 'Low' }






// }


frappe.pages['student-details-page'].on_page_load = function (wrapper) {
    const page = frappe.ui.make_app_page({
        title: 'Student Details',
        parent: wrapper,
        single_column: true
    });

    page.set_title_sub('Status: Verified ✅');

    // Add detailed content
    $(`
        <div class="student-details-section">
            <h4>🎓 Personal Info</h4>
            <p><strong>Full Name:</strong> Johnathan Doe</p>
            <p><strong>Date of Birth:</strong> 2001-06-15</p>
            <p><strong>Email:</strong> john.doe@uni.edu</p>
            <p><strong>Phone:</strong> +91 91234 56789</p>

            <h4>📚 Academic Info</h4>
            <p><strong>Department:</strong> Computer Science</p>
            <p><strong>Program:</strong> B.Tech</p>
            <p><strong>Batch:</strong> 2021 – 2025</p>
            <p><strong>Roll No:</strong> CS21045</p>
            <p><strong>CGPA:</strong> 8.6</p>

            <h4>🗂️ Administrative Info</h4>
            <p><strong>Enrollment Status:</strong> Active</p>
            <p><strong>Hostel:</strong> Block C</p>
            <p><strong>Fee Status:</strong> Paid (₹65,000)</p>
            <p><strong>Last Updated:</strong> 2025-07-10</p>
        </div>

        <div class="actions-section" style="margin-top: 20px;">
            <button class="btn btn-primary" id="refresh-info">🔄 Refresh Info</button>
            <button class="btn btn-success" id="generate-report">📄 Generate Report</button>
        </div>
    `).appendTo(page.main);

    // Event handlers
    $(document).on('click', '#refresh-info', function () {
        frappe.msgprint(__('Student info refreshed!'));
        // Add frappe.call() here to fetch latest info if needed
    });

    $(document).on('click', '#generate-report', function () {
        frappe.call({
            method: 'your_app.api.generate_student_report',
            args: { student_id: 'CS21045' },
            callback: function (r) {
                frappe.msgprint(__('Report generated: ' + r.message));
            }
        });
    });
};