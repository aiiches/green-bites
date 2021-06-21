import * as React from 'react';
import {
  Text, 
  View,
  SafeAreaView,ImageBackground } from 'react-native';

import Carousel from 'react-native-snap-carousel';

export default class App extends React.Component {

 
    constructor(props){
        super(props);
        this.state = {
          activeIndex:0,
          carouselItems: [
          {
              title:"Sustainable Diet: Everything you need to know",
              text: "MEDLIFE DAILY",
          },
          {
              title:"Ethical Eating Habits You Should Adopt Now",
              text: "PLANET FITNESS",
          },
          {
              title:"Best Practices for Green Living",
              text: "FRESH CO",
          },
        ]
      }
    }

    _renderItem({item,index}){
        return (
          <View style={{
            
              backgroundColor:'floralwhite',
              borderRadius: 20,
              height: 500,
              padding: 50,
              marginTop: 50,
              marginLeft: 40,
              marginRight: -10,
              justifyContent: 'center', 
              alignItems: 'center'}}>
            
            <View style={{textAlign:'center',justifyContent: 'center',alignItems: 'center',width:'150%',marginTop:'190%',backgroundColor:'#bfdad5', borderRadius:20}}>
              <Text style={{fontWeight:'bold',fontFamily: 'Roboto-Light',paddingTop: 20,fontSize: 12, paddingLeft:7}}>{item.title}</Text>
              <Text style={{fontFamily: 'Roboto-Light',paddingLeft:15, padding: 10,fontSize: 8}}>{item.text}</Text>
            </View>
            
          </View>
        )
    }

    render() {
        return (
          <SafeAreaView style={{flex: 1, paddingTop: 50, }}>
            <View style={{ flex: 1, flexDirection:'row', justifyContent: 'center', }}>
                <Carousel
                  layout={"default"}
                  ref={ref => this.carousel = ref}
                  data={this.state.carouselItems}
                  sliderWidth={300}
                  itemWidth={300}
                  renderItem={this._renderItem}
                  onSnapToItem = { index => this.setState({activeIndex:index}) } />
            </View>
          </SafeAreaView>
        );
    }
}

