const options = {method: 'GET', headers: {Accept: 'application/json'}};
const response = [];
const a = [];
fetch('https://api.upbit.com/v1/candles/minutes/5?market=KRW-ETH&count=10', options)
  .then(response => response.json())
  // .then(response => console.log(response[0].market))
  .then(response => {
    console.log(response);
    for(let i = 0 ; i< response.length; i++){
      console.log(response[0].high_price);
      console.log(response[0].low_price);
      console.log(response[0].candle_acc_trade_price);
      console.log(response[0].market);
    }
  })
  // .catch(err => console.error(err));

const options1 = {method: 'GET', headers: {Accept: 'application/json'}};

fetch('https://api.upbit.com/v1/market/all?isDetails=false', options1)
  .then(response => response.json())
  .then(response => {
    const coin_name = [];
    for(let i= 0; response.length; i ++){
      if(response[i].market.startsWith('KRW')){
        console.log(response[i].market);
      }
    }
    console.log(coin_name);
  })
  

  