import React, { Component } from 'react';
import { Text,View, StyleSheet, Image } from 'react-native';


export default class App extends Component {
  render() {
    return (
      <View style={styles.container}>
        <View style={{ borderBottomWidth:0.5,borderTopWidth:0.5,bordercolor:'black', flexDirection: 'row', height: 100, paddingLeft:'3%', marginTop:'7%',paddingTop:'5%',paddingBottom:'5%'}}>
          <Image
                style={[styles.img,{ flex: 1}]}
                source={require('../assets/img1.png')}
            />
          <Text style={[styles.paragraph, {flex: 3, paddingLeft:'5%'}]}>May 19, 2021 {"\n"}{"\n"}<Text style={{fontWeight:'normal'}}>Carbon Footprint: 323 CO2 eq/kg</Text></Text>
        </View>
        <View style={{ borderBottomWidth:0.1,borderTopWidth:0.1,bordercolor:'black', flexDirection: 'row', height: 100, paddingLeft:'3%',paddingTop:'5%',paddingBottom:'5%'}}>
          <Image
                style={[styles.img,{ flex: 1}]}
                source={require('../assets/img2.png')}
            />
          <Text style={[styles.paragraph, {flex: 3,paddingLeft:'5%'}]}>May 7, 2021{"\n"}{"\n"}<Text style={{fontWeight:'normal'}}>Carbon Footprint: 323 CO2 eq/kg</Text></Text>
        </View>
        <View style={{ borderBottomWidth:0.1,borderTopWidth:0.5,bordercolor:'black', flexDirection: 'row', height: 100, paddingLeft:'3%',paddingTop:'5%',paddingBottom:'5%'}}>
          <Image
                style={[styles.img,{ flex: 1}]}
                source={require('../assets/img3.png')}
            />
          <Text style={[styles.paragraph, {flex: 3,paddingLeft:'5%'}]}>April 20, 2021{"\n"}{"\n"}<Text style={{fontWeight:'normal'}}>Carbon Footprint: 323 CO2 eq/kg</Text></Text>
        </View>
        <View style={{ borderBottomWidth:0.5,borderTopWidth:0.5,bordercolor:'black', flexDirection: 'row', height: 100, paddingLeft:'3%',paddingTop:'5%',paddingBottom:'5%'}}>
          <Image
                style={[styles.img,{ flex: 1}]}
                source={require('../assets/img4.png')}
            />
          <Text style={[styles.paragraph, {flex: 3,paddingLeft:'5%'}]}>April 11, 2021{"\n"}{"\n"}<Text style={{fontWeight:'normal'}}>Carbon Footprint: 323 CO2 eq/kg</Text></Text>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
        top: '5%',
        left: 0,
        right: 0,
    justifyContent: 'flex-end',
  },
    img: {
      resizeMode: 'cover',
      flex: 1,
      width: '5%',
      height: null,
      resizeMode: 'contain',
    },
    paragraph: {
      fontSize: 10,
      //fontWeight: 'bold',
      textAlign: 'left',
      fontFamily:'Roboto-Regular', 
      fontWeight:'bold', 
      fontSize: 13
    },
});