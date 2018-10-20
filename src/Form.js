import React, { Component } from 'react';

class Form extends Component {
  constructor() {
    super()

    this.state = {
    }
  }

  render() {

  const campNames = this.props.camps.map( camp => {
    return <option value='camp.name'>{camp.name}</option>
  })

    return (
      <form>
        <select name='countries'>
          <option value='liberia'>Liberia</option>
        </select>
        <select name="camps" id="camp">
          {campNames}
        </select>
      </form>

      )
    }
  }

export default Form;