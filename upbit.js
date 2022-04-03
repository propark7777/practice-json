const options = {method: 'GET', headers: {Accept: 'application/json'}};
const response = [];
const a = [];
fetch('https://api.upbit.com/v1/candles/minutes/1?market=KRW-ETH&count=1', options)
  .then(response => response.json())
  // .then(response => console.log(response[0].market))
  .then(response => {
    console.log(response);
    for(let i = 0 ; i< response.length; i++){
      console.log(response[0].candle_acc_trade_price);
      console.log(response[0].market);
    }
  })
  .catch(err => console.error(err));

  