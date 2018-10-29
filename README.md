# Settled In

## The 'Turing Team: Phone Home' was thrilled to participate in the 2018 Space Apps NASA hackathon! 

### We chose the "Land where Displaced People Settle" challenge.

With our application, Settled In, we hope to address the perpetual lack of resources which exists in refugee settlements.

The MODIS API and VIIRS datasets can inform organizations and individuals who want to help.

Settled In will analyze a given settlement's environment and conditions so that partnering organizations can make

informed decisions, work alongside camps to reduce waste, and provide relevant resources for these communities.

Our dream is that this data analysis tool humanizes the experienced of displaced people.

## Tech Stack

JavaScript, React.js, Ruby on Rails, UNHCR / Earthdata / MODIS & VIIRS APIs

## Data

Currently, mock data is seeded based on real data sets:

```Settlement.create(name: 'Kutupalong Settlement', lat: 21.2153522, lon: 92.172192, region: 'Coxs Bazaar', country: 'Bangladesh', population: 886778)
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

# Mock conditions data based on figures from World Resources Institute```

# Wireframes, Iteration 0

## Responsive:

<a href="https://ibb.co/nJdk8A"><img src="https://preview.ibb.co/ivH1gV/Settled-In-Responsive-Wireframe.png" alt="Settled-In-Responsive-Wireframe" border="0"></a>

## Web:

<a href="https://ibb.co/h0VyTA"><img src="https://preview.ibb.co/fLBSMV/Settled-In-Wireframe.png" alt="Settled-In-Wireframe" border="0"><br />
  

# Wireframes, Iteration 1

## Responsive:


<a href="https://ibb.co/dYGa5q"><img src="https://preview.ibb.co/jqc4yA/Home-Screen-2x.png" alt="Home-Screen-2x" border="0"></a>



## Web:


<a href="https://ibb.co/mjpv5q"><img src="https://preview.ibb.co/c7qPyA/Clean-Water-Screen-2x-1.png" alt="Clean-Water-Screen-2x-1" border="0"></a>


<a href="https://ibb.co/bBH4yA"><img src="https://preview.ibb.co/haMWdA/Clean-Water-Screen-2x.png" alt="Clean-Water-Screen-2x" border="0"></a>


<a href="https://ibb.co/fcbWdA"><img src="https://preview.ibb.co/fWcF5q/Settlement-Example-Screen-2x.png" alt="Settlement-Example-Screen-2x" border="0"></a>


## Next Steps

* consume the UNHCR API to find settlement camp locations (API was temporarily unavailable as of 10-20-2018)

* implement logic to handle MODIS & VIIRS data

* convert app styling into a responsive layout for various screen sizes

* implement data visualizations using a tool like processing or D3

## Contributing

Fork and clone this repo to interact with our app in the development stages.

More information about versioning, dependencies, and environments coming soon. Feel free to create an issue as well!
