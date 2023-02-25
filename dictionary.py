mydata ={"AHMEDABAD": 300,"RAJKOT": 150,"SURAT" : 410}

print(mydata)
print(mydata["RAJKOT"])

mydata1 ={"AHMEDABAD": 300,"RAJKOT": 150,"SURAT" : [410,500,2]}
print(mydata1["SURAT"][1])

mydata2 = {"AHMEDABAD" : [{"date":"25 july 22", "cases":110},
                          {"date":"26 july 22", "cases":210},
                          {"date":"27 july 22", "cases":310}],
            "RAJKOT": 150,"SURAT" : [410,500,2]}

print(mydata2["AHMEDABAD"][2]["date"])

mydata3 = {"AHMEDABAD" : [{"date":{"d":25,"m":7,"y":22}, "cases":110},
                          {"date":"26 july 22", "cases":210},
                          {"date":"27 july 22", "cases":310}],
            "RAJKOT": 150,"SURAT" : [410,500,2]}
print(mydata3["AHMEDABAD"][0]["date"]["m"])



http://data.covid19indian.org/data.json
http://api.coindesk.com/v1/bpi/currentprise.json
http://api.mfapi.in/mf
