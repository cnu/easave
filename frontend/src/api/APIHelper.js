import API from './api';

// import axiosHelper from 'axiosHelper'
const processRequest = async (reqType, url, data) => {
  switch (reqType) {
    case 'GET':
      try {
        var apiGetResponse = await apiGetRequest(url, data);
        return apiGetResponse;
      } catch (error) {
        console.log(error);
      }
      break;
    case 'POST':
      try {
        var apiPostResponse = await apiPostRequest(url, data);
        return apiPostResponse;
      } catch (error) {
        console.log(error);
      }
      break;
    case 'PUT':
      try {
        var apiPutResponse = await apiPutRequest(url, data);
        return apiPutResponse;
      } catch (error) {
        console.log(error);
      }
      break;
      case 'PATCH':
        try {
          var apiPatchResponse = await apiPatchRequest(url, data);
          return apiPatchResponse;
        } catch (error) {
          console.log(error);
        }
        break;
    case 'DELETE':
      try {
        var apiDeleteResponse = await apiDeleteRequest(url, data);
        return apiDeleteResponse;
      } catch (error) {
        console.log(error);
      }
      break;
  }
};
const apiGetRequest = async (url, data) => {
  try {
    return API.get(url, data);
  } catch (error) {
    return error
  }
};

const apiPostRequest = async (url, data) => {
  try {
    return API.post(url, data)
  } catch (error) {
    return error
  }
};

const apiDeleteRequest = async (url, data) => {
  try {
    return API.delete(url, data)
  } catch (error) {
    return error
  }
};

const apiPutRequest = async (url, data) => {
  try {
    return API.put(url, data)
  } catch (error) {
    return error
  }
};

const apiPatchRequest = async (url, data) => {
  try {
    return API.patch(url, data)
  } catch (error) {
    return error
  }
};

export default processRequest;