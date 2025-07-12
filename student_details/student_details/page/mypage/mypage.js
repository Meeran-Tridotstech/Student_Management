// frappe.pages['mypage'].on_page_load = function(wrapper) {
// 	var page = frappe.ui.make_app_page({
// 		parent: wrapper,
// 		title: 'Chart',
// 		single_column: true
// 	});
// }

frappe.pages['mypage'].on_page_load = function(wrapper) {
    console.log("Page loaded");

    // Create the app page
    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Disease Count Realtime',
        single_column: true
    });

    // Add chart container
    const $wrapper = $(wrapper);
    $wrapper.find('.page-content').html(`
        <div id="chart" style="padding: 20px;"></div>
    `);

    // Initial empty chart data
    const data = {
        datasets: [
            { name: "Fever", values: [] },
            { name: "Cold", values: [] }
        ]
    };

    // Create Realtime Chart instance
    const chart = new frappe.ui.RealtimeChart("#chart", "disease_realtime_event", 10, {
        title: "Disease Count Realtime",
        data: data,
        type: "bar",
        height: 300,
        colors: ["#ff6f69", "#247ba0"]
    });

    // Start listening to the socket event
    chart.start_updating();

    // Debug: Log realtime data
    frappe.realtime.on("disease_realtime_event", (data) => {
        console.log("Realtime event data received:", data);
    });
};