import React, { Component } from 'react';
import { Image, StyleSheet, View, Text, SafeAreaView, ScrollView, StatusBar} from 'react-native';
 
export default class App extends Component<{}> {
  render() {
    return (
      <View>
        <Image
            style={[styles.img]}
            source={require('../assets/profile.png')}
        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
    img: {
      marginTop: '10%',
      flexDirection: 'row',
      flexWrap: 'wrap',
      height:'95%',
      width: '100%'
    },
});