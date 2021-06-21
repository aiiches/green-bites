import React, { Component } from 'react';
import { Image, StyleSheet, View, Text, SafeAreaView, ScrollView, StatusBar} from 'react-native';
import Slideshow from './Slideshow';
import Article from './Article'

export default class App extends Component<{}> {
  render() {
    return (
      <View>
        <ScrollView 
        style={styles.scrollView} 
        //contentContainerStyle={styles.contentContainer}
        >
        <Text style={[styles.text, { paddingTop: '20%', paddingLeft: '8%'}]}>
        Discover
        </Text>
        <Text style={[{ paddingTop: '5%',paddingLeft: '8%', fontFamily:'Roboto-Regular', fontWeight:'bold', fontSize: 13}]}>
        DAILY REMINDERS
        </Text>
          <View style={[styles.paragraph, styles.contentContainer]}>
            <Text style={styles.paragraph}>
              - eat more fruits and vegetables{"\n"}{"\n"}
              - eat locally when in season{"\n"}{"\n"}
              - swap animal protein for plant-based ones{"\n"}{"\n"}
              - choose sustainably sourced sea food{"\n"}{"\n"}
              - eat dairy products in moderation{"\n"}{"\n"}
              - avoid unecessary packaging 
            </Text>
          </View>
        <Slideshow></Slideshow>
        <Article></Article>
      </ScrollView>
      </View>
    );
  }
}
 
const styles = StyleSheet.create({
  paragraph: {
    margin: 24,
    fontSize: 10,
    //fontWeight: 'bold',
    textAlign: 'left',
  },
  scrollView: {
    height: '100%',
    width: '90%',
    marginTop: '5%',
    alignSelf: 'center',

  },
  contentContainer: {
    justifyContent: 'center',
    alignItems: 'flex-start',
    backgroundColor: '#BFDAD5',
    borderRadius: 20,
  },
  text: {
    fontSize: 36,
    fontFamily: 'Roboto-Light'
  }
});