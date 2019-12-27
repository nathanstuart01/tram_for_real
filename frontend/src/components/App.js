import React from 'react';
import { Switch, Route } from 'react-router-dom'; 
import '../css/styles.css';
import Login from './login';
import Signup from './signup';
import NotFound from './notFound';
import UserHomePage from './userHomePage';
import About from './about';
import ProtectedRoute from './protectedRoute';

const  App = () => (
      <div>
        <Switch>
            <ProtectedRoute exact path='/user_home_page' exact={true} component={UserHomePage} />
            <Route exact path='/' exact={true} component={About} />
            <Route exact path="/login" exact={true} component={Login} />
            <Route exact path='/signup' exact={true} component={Signup} />
            <Route exact component={NotFound} />
        </Switch>
      </div>
)

export default App;
