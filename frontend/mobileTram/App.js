import React, { Component } from 'react';
import { StyleSheet, Text, View, TextInput, Button } from 'react-native';

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'skyblue',
    alignItems: 'center',
    justifyContent: 'center',
    color: 'green',
    fontWeight: 'bold',
  },
});

class SignIn extends Component {
  constructor(props) {
    super(props);
    this.state = {username: '', password: ''};
  }

  render() {
    return (
      <View style={{color: 'red'}}>
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
          onPress={() => {
            alert(this.state.password);
          }}
          title="Sign In"
        />
      </View>
    );
  }
}

export default function App() {
  return (
    <View style={styles.container}>
      <SignIn />
    </View>
  );
}

