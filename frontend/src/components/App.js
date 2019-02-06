import React from 'react';
import { Switch, Route } from 'react-router-dom'; 
import '../css/styles.css';
import Login from './login';
import Signup from './signup';
import NotFound from './notFound';

const  App = () => (
      <div>
        <Switch>
            <Route path="/" exact={true} component={Login} />
            <Route path='/signup' exact={true} component={Signup} />
            <Route component={NotFound} />
        </Switch>
      </div>
)

export default App;
