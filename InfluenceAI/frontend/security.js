```javascript
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const secureFetch = async (url, options = {}) => {
  const token = localStorage.getItem('token');
  if (token) {
    options.headers = {
      ...options.headers,
      Authorization: `Bearer ${token}`,
    };
  }
  const response = await axios(`${API_URL}${url}`, options);
  return response.data;
};

export const login = async (username, password) => {
  const response = await secureFetch('/auth/login', {
    method: 'POST',
    data: {
      username,
      password,
    },
  });
  if (response.token) {
    localStorage.setItem('token', response.token);
  }
  return response;
};

export const logout = () => {
  localStorage.removeItem('token');
};

export const isAuthenticated = () => {
  return !!localStorage.getItem('token');
};

export const register = async (username, password, email) => {
  const response = await secureFetch('/auth/register', {
    method: 'POST',
    data: {
      username,
      password,
      email,
    },
  });
  return response;
};
```