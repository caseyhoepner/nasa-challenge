import React from 'react';
import Card from './Card';

const CardContainer = ({ camps }) => {
  const cards = camps.map(camp => {
  return <Card 
            name={camp.name}
            country={camp.country}
            region={camp.region}
            population={camp.population}
            key={camp.name}
         />
})

  return (
    <section>
      { cards }
    </section>
    )
  }

export default CardContainer;