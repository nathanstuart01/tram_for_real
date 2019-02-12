import React from 'react';
import { Switch, Route } from 'react-router-dom'; 
import '../css/styles.css';
import Login from './login';
import Signup from './signup';
import NotFound from './notFound';
import UserHomePage from './userHomePage';

const  App = () => (
      <div>
        <Switch>
            <Route path="/" exact={true} component={Login} />
            <Route path='/signup' exact={true} component={Signup} />
            <Route path='/user_home_page' exact={true} component={UserHomePage} />
            <Route component={NotFound} />
        </Switch>
      </div>
)

export default App;
