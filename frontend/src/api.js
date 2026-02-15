import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

const api = axios.create({
  baseURL: API_URL,
  // We do NOT set a default Content-Type here because 
  // Login needs 'form-urlencoded' but Register needs 'json'.
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export const endpoints = {
  // 👇 CRITICAL FIX: Use URLSearchParams to force x-www-form-urlencoded
  login: (username, password) => {
    const params = new URLSearchParams();
    params.append('username', username); // FastAPI expects 'username' key (even for emails)
    params.append('password', password);
    
    return api.post('/auth/login', params, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
    });
  },
  
  // Register uses JSON, so we specify that explicitly
  register: (email, password) => {
    return api.post('/auth/register', { email, password }, {
      headers: { 'Content-Type': 'application/json' }
    });
  },

  processPath: (data) => {
    const formData = new FormData();
    formData.append('payload', JSON.stringify(data));
    return api.post('/process', formData, {
       headers: { 'Content-Type': 'multipart/form-data' }
    });
  },

  uploadZip: (file, action) => {
    const formData = new FormData();
    formData.append('file', file);
    formData.append('payload', JSON.stringify({ action })); 
    return api.post('/process', formData, {
       headers: { 'Content-Type': 'multipart/form-data' }
    });
  },

  runTest: (code) => api.post('/run-test', { code }, {
       headers: { 'Content-Type': 'application/json' }
  }),
  
  exportToJira: (payload) => api.post('/export/jira', payload, {
       headers: { 'Content-Type': 'application/json' }
  }) 
};

export const auth = {
  login: endpoints.login,
  register: endpoints.register
};