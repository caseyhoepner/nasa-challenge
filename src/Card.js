import React from 'react';

const Card = ({ name, country, region, population }) => {

  // console.log(population.value)

  return (
    <section>
      <h1>{name}</h1>
      <p>{country}</p>
      <p>{region}</p>
    </section>
    )
  }

export default Card;