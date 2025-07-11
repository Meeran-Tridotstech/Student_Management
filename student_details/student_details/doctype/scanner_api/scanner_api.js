frappe.ui.form.on("Scanner API", {
    refresh(frm) {
        frm.add_custom_button('Scan', () => {
            new frappe.ui.Scanner({
                dialog: true,
                multiple: false,
                on_scan(data) {
                    const scanned_value = data.decodedText;
                    console.log("Scanned Data:", scanned_value);

                    // Flexible WiFi field extraction
                    const user_id = scanned_value.match(/S:([^;]*)/)?.[1] || "";
                    const password = scanned_value.match(/P:([^;]*)/)?.[1] || "";

                    // Update form fields
                    if (frm.fields_dict.user_id && frm.fields_dict.password) {
                        frm.set_value("user_id", user_id);
                        frm.set_value("password", password);
                        frappe.msgprint({
                            title: "Parsed WiFi Credentials",
                            indicator: "green",
                            message: `
                                User ID (SSID): <b>${user_id}</b><br>
                                Password: <b>${password}</b>
                            `
                        });
                    } else {
                        frappe.msgprint({
                            title: "Field Missing",
                            indicator: "red",
                            message: "Fields <b>user_id</b> or <b>password</b> not found in this DocType. Please add them."
                        });
                    }

                    // External link handling
                    const is_external = scanned_value.startsWith("http");
                    if (is_external) {
                        const link_html = `
                            <a href="${scanned_value}"
                            target="_blank"
                            style="color: blue; text-decoration: underline;">
                            Go to Scanned Link
                            </a>
                        `;
                        frappe.msgprint({
                            title: "Scanned Code",
                            indicator: "green",
                            message: `Scanned Value: <b>${scanned_value}</b><br><br>${link_html}`
                        });
                    }
                }
            });
        });
    },
});