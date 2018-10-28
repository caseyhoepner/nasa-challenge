Settlement.create(name: 'Kutupalong Settlement', lat: 21.2153522, lon: 92.172192, region: 'Coxs Bazaar', country: 'Bangladesh', population: 886778)
Settlement.create(name: 'Bidi Bidi Settlement', lat: 3.5222462, lon: 31.3337782, region: 'Yumbe', country: 'Uganda', population: 285000)
Settlement.create(name: 'Dadaab Refugee Complex Settlement', lat: 0.1044344, lon: 40.3050372, region: 'Dadaab', country: 'Kenya', population: 235269)
Settlement.create(name: 'Jabalya Settlement', lat: 31.5301972, lon: 34.475033, region: 'Gaza', country: 'Israel', population: 119486)

# Mock data based on figures from https://www.raptim.org/largest-refugee-camps-in-2018/

WaterCondition.create(settlement_id: Settlement.first.id, 
                      cons_use: 15, baseline_stress: 'Low', 
                      drought_severity: 'Low', flood_occurence: 'Extremely High', 
                      total_withdrawl: 100, blue_water: 100, 
                      variability: 'Low', access: 'High')

WaterCondition.create(settlement_id: Settlement.last.id,
                      cons_use: 10, baseline_stress: 'Medium to High',
                      drought_severity: 'Medium', flood_occurence: 'High',
                      total_withdrawl: 10, blue_water: 100,
                      variability: 'Medium', access: 'Medium')

# Mock conditions data based on figures from World Resources Institute