import React, {Component} from 'react';
import { Searchbar } from 'react-native-paper';

import {Input,StyleSheet,View,Text,Image,Button,SafeAreaView,ScrollView,StatusBar} from 'react-native';

const MyComponent = () => {
  const [searchQuery, setSearchQuery] = React.useState('');
  const [searchResult, setSearchResult] = React.useState('');
  const onChangeSearch = query => setSearchQuery(query);

  return (
    <View>
      <Text style={[styles.text, {paddingTop: '25%'}]}>
        Search
      </Text>
      <Searchbar
        style={{marginTop:'7%', width:'90%', marginLeft:'5%'}}
        placeholderTextColor='black' 
        placeholder="Enter an item"
        onChangeText={onChangeSearch}
        onSubmitEditing={ ()=> fetch('http://localhost:5000/search?item='+searchQuery).then((response) => response.text()).then(result => setSearchResult(result))      }
        value={searchQuery}
        inputStyle={{'fontFamily': 'Roboto-Light', 'fontSize':15}}
      />
      <View style={{margin:'10%',backgroundColor:'#539c8b', borderRadius:20}}>
        <Text style={[styles.text,{paddingTop: '5%'}]}>
          {searchQuery}
        </Text>
        <Text style={[{textAlign:'left',fontSize:8,paddingTop:'-10%',paddingBottom: '5%',paddingLeft: '8%',paddingRight: '8%'}]}>{"\n"}{searchResult}</Text>
      </View>
      
    </View>
  );
};

export default MyComponent;

const styles = StyleSheet.create({
  container: {
    marginTop: '50%',
    flex: 1,
  },
  text: {
    paddingBottom:'-10%',
    paddingLeft: '8%',
    fontSize: 30,
    fontFamily: 'Roboto-Light',
    paddingRight: '8%'
  },
  textboxfield: {
    fontFamily: 'Roboto-Light'
  }
});

