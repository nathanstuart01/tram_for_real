import React from 'react';
import { StyleSheet, Text, View, TextInput, Button } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'skyblue',
    alignItems: 'center',
    justifyContent: 'center',
    fontWeight: 'bold',
  },
});

class SignIn extends React.Component {
  
  state = {username: '', password: ''};

  authenticate = () => {
    let {username, password} = this.state;
    console.log({username, password});
    fetch("http://localhost:5000/api/login", {
            method: "POST",
            body: JSON.stringify({username, password}),
            headers: {
              "Content-Type": "application/json"
            },
        }).then(res => {
          return res.json()
        }).then(data =>{
          console.log(data)
        })
        .catch(error => console.error('Error:', error)); 
  }

  render() {
    return (
      <View>
        <Text>Sign In</Text>
        <TextInput
          style={{height:80, width: 80}}
          placeholder="Username"
          onChangeText={(username) => this.setState({username})}
          value={this.state.username}
        />
        <TextInput 
        style={{height:80, width: 80}}
        placeholder="Password"
        onChangeText={(password) => this.setState({password})}
        value={this.state.password}
        />
        <Button 
          onPress={this.authenticate}
          title="Sign In"
        />
      </View>
    );
  }
}

export default function App() {
  return (
    <View>
      <SignIn />
    </View>
  );
}

