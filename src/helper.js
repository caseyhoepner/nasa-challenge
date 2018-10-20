import liberiaData from './data/LiberiaSettlements.js'

class CountryData {
  constructor() {
    this.camps = this.cleanData(liberiaData);
  }

  cleanData = (country) => {
    const cardData = country.map(entry => {
      return { 
        name: entry.name, 
        country: entry.country, 
        region: entry.region, 
        population: entry.population[0],
        latitude: entry.latitude, 
        longitude: entry.longitude
      }
    })
    return cardData;
  }
}

export default CountryData;