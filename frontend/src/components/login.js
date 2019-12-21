import React from 'react';
import '../css/styles.css';
import { Link, Redirect } from 'react-router-dom';
import {login, logout } from './Auth';

class Login extends React.Component {
        //eventually make a function for email that makes an authenticated user
    state = { username: '', password: '', token: '' }

    handleChange = (event) => {
        let element = event.target;
        let key = element.id;
        this.setState({ [key]: element.value });
    }

    handleErrors = (response) => {
        if (!response.ok) {
            throw Error(response.statusText);
        }
        return response;
    }

    authenticate = (event) => {
        event.preventDefault();
        let { username, password } = this.state;
        fetch("http://127.0.0.1:5000/api/login", {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({"username": username, "password": password})
        }).then(this.handleErrors)
            .then(res => res.json())
            .then(data => login(data['access_token']))
            .catch(error => console.error('Error:', error));
        }
    // after calling login function, mark that user is authenticated and set it to true for protected routes

    render() {
        return (
        <div>
            <h1>Tram Home Page with Information about the Ride Board App</h1>
            <h2>Login to tram</h2>
            <form onSubmit={this.authenticate}>
                <input id='username' type='text' autoFocus required placeholder='Username' onChange={this.handleChange} />
                <input id='password' type='password' autoFocus required placeholder='Password' onChange={this.handleChange} />
                <input type='submit' value='Submit' />
            </form>
            <Link to ='/register'>New User? Register for Tram here</Link>
            <button onClick={logout}>Log Out</button>
        </div>
        );
    }
}

export default Login;