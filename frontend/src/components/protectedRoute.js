import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { authenticatedUser } from './Auth';

const ProtectedRoute = ({ component: Component, ...rest}) => (
    <Route {...rest} render={props=> (
        Object.keys(authenticatedUser()).length ? (
            <Component {...props} />
        ) : (
            <Redirect to={{
                pathname: '/login',
                state: { from: props.location}
            }}/>
        )
    )}/>
)

export default ProtectedRoute;