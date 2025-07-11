
const jsonQuery = {
  "query": [
    {
      "code": "Sukupuoli",
      "selection": {
        "filter": "item",
        "values": [
          "SSS",
          "1",
          "2"
        ]
      }
    },
    {
      "code": "Vaalipiiri ja kunta vaalivuonna",
      "selection": {
        "filter": "item",
        "values": [
          "SSS"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}

const getData = async()=>{
    const url = "https://pxdata.stat.fi:443/PxWeb/api/v1/en/StatFin/evaa/statfin_evaa_pxt_13sv.px"

    const res = await fetch(url,{
        method:"POST",
        headers:{"content-type":"script/json"},
        body:JSON.stringify(jsonQuery)
    })
    if(!res.ok){
        return;
    }

    const data = await res.json()

    return data
}

const buildChart = async()=>{
    const data = await getData()
    // console.log(data)

    const parties = Object.values(data.dimension.Sukupuoli.category.label)
    const labels = Object.values(data.dimension.Vuosi.category.label)
    const values = data.value

    // console.log(parties)
    // console.log(labels)
    // console.log(values)
    

    parties.forEach((party,index)=>{
        let partySupport = []
        for(i=0;i<10;i++){
            partySupport.push(values[i * 8 + index])
        }
        parties[index] = {
            name : party,
            values : partySupport.reverse()
        }
    })

    // console.log(parties)

    const chartData = {
        labels:labels,
        datasets : parties
    }

    const chart = new frappe.Chart("#chart",{
        title :"Finnish Parlimentary elections",
        data :chartData,
        type :"bar",
        height:400,
        colors:['#f54b4b','#ffe55','#006288','#349a29','#61bf1a','#f00a64','#ffdd93','#0135a5'],
    })

}

buildChart()