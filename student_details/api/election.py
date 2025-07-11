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
    parties_raw = list(data["dimension"]["Sukupuoli"]["category"]["label"].values())
    labels = list(data["dimension"]["Vuosi"]["category"]["label"].values())
    values = data["value"]

    parties = []
    for index, party in enumerate(parties_raw):
        party_support = [values[i * 8 + index] for i in range(10)]
        parties.append({
            "name": party,
            "values": list(reversed(party_support))
        })

    frappe.publish_realtime("election_data_updated", {
        "labels": labels,
        "parties": parties
    })