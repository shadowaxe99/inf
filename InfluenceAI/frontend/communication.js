import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { API_KEYS } from './utils.js';

const Communication = () => {
  const [pitchDeck, setPitchDeck] = useState([]);
  const [callScript, setCallScript] = useState('');

  useEffect(() => {
    generatePitchDeck();
    generateCallScript();
  }, []);

  const generatePitchDeck = async () => {
    try {
      const response = await axios.get(`https://api.powerpoint.com/v1/pitchdeck?apiKey=${API_KEYS.POWERPOINT}`);
      setPitchDeck(response.data);
    } catch (error) {
      console.error('Error generating pitch deck:', error);
    }
  };

  const generateCallScript = async () => {
    try {
      const response = await axios.get(`https://api.voip.com/v1/callscript?apiKey=${API_KEYS.VOIP}`);
      setCallScript(response.data);
    } catch (error) {
      console.error('Error generating call script:', error);
    }
  };

  return (
    <div>
      <h2>Marketing and Communication</h2>
      <div id="marketing-pitch">
        <h3>Pitch Deck</h3>
        {pitchDeck.map((slide, index) => (
          <div key={index}>
            <h4>{slide.title}</h4>
            <p>{slide.content}</p>
          </div>
        ))}
      </div>
      <div id="ai-call">
        <h3>AI Call Script</h3>
        <p>{callScript}</p>
      </div>
    </div>
  );
};

export default Communication;