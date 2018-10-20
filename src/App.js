import React, { Component } from 'react';
import './App.css';
import Form from './Form';
import CardContainer from './CardContainer'
import CountryData from './helper'

class App extends Component {
  constructor() {
    super()

    this.state = {
      camps: [],
    }
  }

  componentDidMount() {
    const dataCleaner = new CountryData();
    const camps = dataCleaner.camps
    this.setState({ camps })
  }

  render() {
    const { camps } = this.state
    return (
      <div className="App">
        <Form />
        <CardContainer camps={camps} />
      </div>
    );
  }
}

export default App;