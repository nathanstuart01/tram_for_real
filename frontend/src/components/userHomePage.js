import React from 'react';
import {withRouter} from 'react-router-dom';
import { logout } from './Auth';
import { authenticatedUser } from './Auth';
import DriverTrips  from './DriverTrips';
import RiderTrips from './RiderTrips';

class UserHomePage extends React.Component {

    render(){
        return (
            <div>Authenticated User Home Page
                <div id='driverTrips'><DriverTrips /></div>
                <div id='riderTrips'><RiderTrips /></div>
                <button onClick={ (history) => {logout(); this.props.history.push('/')}}>Logout</button>
            </div>
            
        )
    }
}

export default withRouter(UserHomePage);