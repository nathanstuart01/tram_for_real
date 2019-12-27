import React from 'react';
import '../css/styles.css';
import { Link, Redirect } from 'react-router-dom';
import {auth, authenticatedUser } from './Auth';

class Login extends React.Component {
    state = { user: authenticatedUser(), username: '', password: ''}

    handleChange = (event) => {
        let element = event.target;
        let key = element.id;
        this.setState({ [key]: element.value });
    }

    authenticate = (event) => {
        event.preventDefault();
        let { username, password } = this.state
        auth({username, password }, 'login', () => {
            this.setState({ user: authenticatedUser() });
        });
    }

    render() {
        let { user, username, password } = this.state;
        return (
        <div>
            { Object.keys(user).length ? 
            <Redirect to='/user_home_page' />
            :
            <div>
                <h2>Login to tram</h2>
            <form onSubmit={this.authenticate}>
                <input id='username' type='text' autoFocus required placeholder='Username' onChange={this.handleChange} />
                <input id='password' type='password' autoFocus required placeholder='Password' onChange={this.handleChange} />
                <input type='submit' value='Submit' />
            </form>
            <Link to ='/register'>New User? Register for Tram here</Link>
            </div>
        }
        </div>
        );
    }
}

export default Login;