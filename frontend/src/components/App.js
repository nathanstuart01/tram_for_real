import React from 'react';
import '../css/styles.css';
import Login from './login';

class App extends React.Component {

  render() {
    return (
      <div>
          <p>
            <Login />
          </p>
      </div>
    );
  }
}

export default App;
