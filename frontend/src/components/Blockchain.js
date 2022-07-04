import React, { useState, useEffect } from 'react';
import Block from './Block';

const Blockchain = () => {
  const [blockchain, setBlockchain] = useState([]);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_API_URL}/blockchain`)
      .then((response) => response.json())
      .then((json) => setBlockchain(json));
  }, []);
  return (
    <div className="Blockchain">
      <h3>Blockchain</h3>
      <div>
        {blockchain.map((block) => (
          //   <div key={block.hash}>{JSON.stringify(block)}</div>
          <Block key={block.hash} block={block} />
        ))}
      </div>
    </div>
  );
};

export default Blockchain;
