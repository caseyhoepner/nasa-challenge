import React, { Component } from 'react';

class Form extends Component {
  constructor() {
    super()

    this.state = {

    }
  }

  render() {
    return (
      <form>
        <select name='countries'>
          <option value='liberia'>Liberia</option>
        </select>
      </form>
      )
    }
  }

export default Form;