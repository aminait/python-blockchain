import React, { useState, useEffect } from 'react';
import logo from './assets/logo.png';
import Blockchain from './components/Blockchain';

function App() {
  const [walletInfo, setWalletInfo] = useState({});
  console.log('useEffect -> process.env.REACT_API_URL', process.env);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/wallet/info`)
      .then((response) => response.json())
      .then((json) => setWalletInfo(json));
  }, []);

  return (
    <div className="App">
      <img className="logo" src={logo} alt="logo" />
      <h3>App</h3>
      <br />
      <div className="WalletInfo">
        <div>Address: {walletInfo.address}</div>
        <div>Balance: {walletInfo.balance}</div>
        <Blockchain />
      </div>
    </div>
  );
}

export default App;
