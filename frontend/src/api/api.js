import axios from 'axios';

const API = axios.create({
  baseURL: 'localhost:3000',
  withCredentials: false,
  headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
  }
});
API.interceptors.request.use(
  request => {
    /** TODO: Add any request interceptors */
    return request;
  },
  error => {
    /** TODO: Do something with response error */
    return Promise.reject(error);
  }
);

API.interceptors.response.use(
  response => {
    /** TODO: Add any response interceptors */
    return response;
  },
  error => {
    /** TODO: Do something with response error */
    return Promise.reject(error);
  }
);

export default API;