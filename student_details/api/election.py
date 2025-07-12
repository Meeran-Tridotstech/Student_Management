import frappe
import requests

@frappe.whitelist()
def publish_election_data():
    url = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/evaa/statfin_evaa_pxt_13sv.px"
    json_query = {
        "query": [
            {"code": "Sukupuoli", "selection": {"filter": "item", "values": ["SSS", "1", "2"]}},
            {"code": "Vaalipiiri ja kunta vaalivuonna", "selection": {"filter": "item", "values": ["SSS"]}}
        ],
        "response": {"format": "json-stat2"}
    }

    res = requests.post(url, json=json_query)
    if not res.ok:
        frappe.throw("Failed to fetch data from Finland API")

    data = res.json()

    # Extract labels (years) and party names
    labels = list(data["dimension"]["Vuosi"]["category"]["label"].values())
    parties_raw = list(data["dimension"]["Sukupuoli"]["category"]["label"].values())
    values = data["value"]

    # Dynamically calculate the number of years
    years_count = len(labels)

    # Calculate offset length for each party block
    items_per_year = int(len(values) / years_count)

    parties = []
    for index, party in enumerate(parties_raw):
        party_support = []
        for year in range(years_count):
            offset = year * items_per_year
            party_support.append(values[offset + index])
        parties.append({
            "name": party,
            "values": party_support
        })

    frappe.publish_realtime("election_data_updated", {
        "labels": labels,
        "parties": parties
    })