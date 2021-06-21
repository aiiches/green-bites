import * as React from 'react';
import { Linking } from 'react-native';
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
              text: "THE NUTRITION SOURCE",
              imgUrl: "https://picsum.photos/id/123/200/300"
          },
          {
              title:"Ethical Eating Habits You Should Adopt Now",
              text: "PLANET FITNESS",
              imgUrl: "https://picsum.photos/id/223/200/300"
          },
          {
              title:"Best Practices for Green Living",
              text: "FRESH CO",
              imgUrl: "https://picsum.photos/id/1023/200/300"
          },
        ]
      }
    }

    _renderItem({item,index}){
        return (
          <View style={{borderRadius:20, marginTop:'10%'}}>
            <ImageBackground style={{backgroundColor:'floralwhite',
              overflow:'hidden',
              borderRadius: 20,
              height: 400,
              paddingTop: 160,
              padding: 30,
              marginLeft: 45,
              marginRight: 0,}} source={{ uri: item.imgUrl }}>
                <View style={{textAlign:'center',justifyContent: 'center',alignItems: 'center',width:'100%',marginTop:'60%',backgroundColor:'#bfdad5', borderRadius:20}}>
                  <Text style={{fontWeight:'bold',fontFamily: 'Roboto-Light',paddingTop: 20,fontSize: 12, paddingLeft:7}} onPress={() => Linking.openURL('https://www.hsph.harvard.edu/nutritionsource/sustainability/')}>{item.title}</Text>
                  <Text style={{fontFamily: 'Roboto-Light',paddingLeft:15, padding: 10,fontSize: 8}}>{item.text}</Text>
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

