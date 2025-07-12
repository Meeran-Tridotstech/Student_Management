frappe.pages['chart'].on_page_load = function(wrapper) {
    const page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Parliamentary Election - [1983 - 2023]',
        single_column: true
    });

    // Chart container with height and width styling
    const $container = $(`
        <div id="chart" style="width: 100%; height: 400px;"></div>
    `).appendTo(page.body);

    // Initialize chart
    const chart = new frappe.ui.RealtimeChart("#chart", {
        title: "Finnish Parliamentary Elections",
        type: "bar",
        height: 400,
        colors: ['#f54b4b','#ffe55','#006288','#349a29','#61bf1a','#f00a64','#ffdd93','#0135a5'],
        labels: [],
        datasets: []
    });

    // Log real-time updates and apply data
    frappe.realtime.on("election_data_updated", ({ labels, parties }) => {
        console.log("Received data:", labels, parties); // Debug log

        if (Array.isArray(labels) && Array.isArray(parties)) {
            chart.set_values({
                labels: labels,
                datasets: parties.map(p => ({
                    name: p.name,
                    values: p.values
                }))
            });
        } else {
            console.error("Invalid realtime data structure");
        }
    });
};