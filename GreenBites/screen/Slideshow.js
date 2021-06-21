import * as React from 'react';
import {
  Text, 
  View,
  SafeAreaView,ImageBackground,Image } from 'react-native';

import Carousel from 'react-native-snap-carousel';

export default class App extends React.Component {

 
    constructor(props){
        super(props);
        this.state = {
          activeIndex:0,
          carouselItems: [
          {
              title:"Ayesha Liaqat",
              text: "@aliaqat",
              imgUrl: "https://picsum.photos/id/10/200/300"
            },
          {
              title:"Lama Khalil",
              text: "@lkhalil",
          },
          {
              title:"Kate Szabo",
              text: "@kszabo",
          },
          {
              title:"Meriem Khalfoun",
              text: "@mkhalfoun",
          },
          {
              title:"Victoria Wang",
              text: "@vwang",
          },
        ]
      }
    }

    _renderItem({item,index}){
        return (
          <View style={{borderRadius:20}}>
            <ImageBackground style={{backgroundColor:'floralwhite',
            overflow:'hidden',
              borderRadius: 20,
              height: 250,
              paddingTop: 160,
              padding: 30,
              marginLeft: 45,
              marginRight: 0,}} source={{ uri: item.imgUrl }}>
                <View style={{padding:10,borderRadius:20,backgroundColor:'#6e9484'}}>
                  <Text style={{fontSize: 15}}>{item.title}</Text>
                  <Text style={{paddingTop:8}}>{item.text}</Text>
                </View>
              
            </ImageBackground>
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

