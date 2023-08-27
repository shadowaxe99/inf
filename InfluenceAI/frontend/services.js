import axios from 'axios';

const API_URL = process.env.API_URL;

export const scrapeSocialMedia = async () => {
  try {
    const response = await axios.get(`${API_URL}/scrape_social_media`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const predictInfluencerPotential = async (influencerData) => {
  try {
    const response = await axios.post(`${API_URL}/predict_influencer_potential`, influencerData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const optimizeContent = async (contentData) => {
  try {
    const response = await axios.post(`${API_URL}/optimize_content`, contentData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const matchBrandInfluencer = async (matchData) => {
  try {
    const response = await axios.post(`${API_URL}/match_brand_influencer`, matchData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const generateContract = async (contractData) => {
  try {
    const response = await axios.post(`${API_URL}/generate_contract`, contractData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const processPayment = async (paymentData) => {
  try {
    const response = await axios.post(`${API_URL}/process_payment`, paymentData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const monitorCompliance = async () => {
  try {
    const response = await axios.get(`${API_URL}/monitor_compliance`);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const generatePitchDeck = async (pitchData) => {
  try {
    const response = await axios.post(`${API_URL}/generate_pitch_deck`, pitchData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};

export const makeAiCall = async (callData) => {
  try {
    const response = await axios.post(`${API_URL}/make_ai_call`, callData);
    return response.data;
  } catch (error) {
    console.error(error);
  }
};