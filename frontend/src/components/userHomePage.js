import React from 'react';
import {withRouter} from 'react-router-dom';
import { logout } from './Auth';
import { authenticatedUser } from './Auth';
import DriverTrips  from './Driver';

class UserHomePage extends React.Component {

    render(){
        return (
            <div>Authenticated User Home Page
                <DriverTrips />
                <button onClick={ (history) => {logout(); this.props.history.push('/')}}>Logout</button>
            </div>
            
        )
    }
}

export default withRouter(UserHomePage);