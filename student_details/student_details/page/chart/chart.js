frappe.pages['chart'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Parliamentary Election - [1983 - 2023]',
        single_column: true
    });

    let $container = $('<div id="chart"></div>').appendTo(page.body);

    let chart = new frappe.ui.RealtimeChart("#chart", {
        title: "Finnish Parliamentary Elections",
        type: "bar",
        height: 400,
        colors: ['#f54b4b','#ffe55','#006288','#349a29','#61bf1a','#f00a64','#ffdd93','#0135a5'],
        labels: [],
        datasets: []
    });

    frappe.realtime.on("election_data_updated", ({ labels, parties }) => {
        chart.set_values({
            labels: labels,
            datasets: parties.map(p => ({
                name: p.name,
                values: p.values
            }))
        });
    });
};