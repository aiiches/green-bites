import React, {Component} from 'react';
import {StyleSheet,View,Text,Image,Button,ImageBackground} from 'react-native';
import LoginScreen from './screen/Login';
import { NavigationContainer } from '@react-navigation/native';
import { Assets, createStackNavigator } from '@react-navigation/stack';
const Stack = createStackNavigator();

function splashScreen({navigation}) {
  setTimeout(() => {
    navigation.replace('LoginPage') // Stack Name
  }, 3000);
  return (
    <View>
      <ImageBackground source={require('./assets/background.png')} style={{height:'100%', width:'100%'}}>
        <Image source={require('./assets/logo.png')} style={{position: 'absolute', bottom: '50%'}}/>
        
      </ImageBackground>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "column"
  },
  image: {
    flex: 1,
    resizeMode: "cover",
    justifyContent: "center"
  },
  text: {
    color: "white",
    fontSize: 42,
    fontWeight: "bold",
    textAlign: "center",
    backgroundColor: "#000000a0"
  }
});

export default function App() {
  return (
     <NavigationContainer>
       <Stack.Navigator headerMode="none">
         <Stack.Screen name="splash_Screen" component={splashScreen}/>
         <Stack.Screen name="LoginPage" component={LoginScreen}/>
       </Stack.Navigator>
     </NavigationContainer>
  );
}