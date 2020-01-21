import React from 'react';
import { logout } from './Auth';
import { authenticatedUser } from './Auth';
import DriverTrips  from './DriverTrips';
import RiderTrips from './RiderTrips';
import { BASE_URL } from './Url';

class UserHomePage extends React.Component {

    constructor(props) {
        super(props);
        this.state = { driverTrips: [], riderTrips: [] };
      }

    getDriverTrips = (token) => {
        fetch(`${BASE_URL}/${'show_driver_trips'}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
            }).then(res => res.json())
                .then( result => {
                    this.setState({driverTrips: result['Current active driver trips']});
                })
                .catch( error => {
                    console.log(error.message);
                })
            }
    
    getRiderTrips = (token) => {
        fetch(`${BASE_URL}/${'show_rider_trips'}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
            }).then(res => res.json())
                .then( result => {
                    this.setState({riderTrips: result['rider_trips']});
                })
                .catch( error => {
                    console.log(error.message);
                })
            }
    
    componentDidMount() {
        var token = localStorage.getItem('access_token');
        this.getDriverTrips(token);
        this.getRiderTrips(token);
    }
    
    render(){
        return (
            <div>Authenticated User Home Page
                <DriverTrips driverTrips={this.state.driverTrips} />
                <RiderTrips riderTrips={this.state.riderTrips} />
                <button onClick={ (history) => {logout(); this.props.history.push('/')}}>Logout</button>
            </div>
            
        )
    }
}

export default UserHomePage;