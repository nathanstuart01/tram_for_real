import React from 'react';
import '../css/styles.css';
import { Link } from 'react-router-dom';

class Login extends React.Component {

  render() {
    return (
      <div>
        <h2>Login to tram</h2>
        <form>
            <input id='email' autoFocus required placeholder='Email' />
            <input id='password' autoFocus required placeholder='Password' />
            <button>Login</button>
        </form>
        <Link to ='/register'>New User? Register for Tram here</Link>
      </div>
    );
  }
}

export default Login;