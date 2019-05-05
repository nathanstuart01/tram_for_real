import React from 'react';
import '../css/styles.css';
import { Link, Redirect } from 'react-router-dom';

class Login extends React.Component {
        //eventually make a function for email that makes an authenticated user
    state = { username: '', password: ''}

    handleChange = (event) => {
        let element = event.target;
        let key = element.id;
        this.setState({ [key]: element.value });
    }

    authenticate = (event) => {
        event.preventDefault();
        let { username, password } = this.state;
        fetch("http://127.0.0.1:5000/api/login", {
            method: "POST",
            body: JSON.stringify({username: username, password: password}),
            headers: {
              "Content-Type": "application/json"
            },
        }).then(res => console.log(res))
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error)); 
        }

    render() {
        return (
        <div>
            <h2>Login to tram</h2>
            <form onSubmit={this.authenticate}>
                <input id='username' type='text' autoFocus required placeholder='Username' onChange={this.handleChange} />
                <input id='password' type='password' autoFocus required placeholder='Password' onChange={this.handleChange} />
                <input type='submit' value='Submit' />
            </form>
            <Link to ='/register'>New User? Register for Tram here</Link>
        </div>
        );
    }
}

export default Login;