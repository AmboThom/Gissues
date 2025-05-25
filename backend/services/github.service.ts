const axios = require('axios');
const { getGitHubHeaders, GITHUB_API_BASE } = require('../config/github');

interface SearchParams {
    q: string;
    sort?: string;
    order?: string;
    per_page?: number;
    page?: number;
  }  

interface LabelSearchParams {
    repository_id: string;
    q: string;
    sort?: string;
    order?: string;
    per_page?: number;
    page?: number;
}

const searchRepositories = async (params) => {
  console.log('Making GitHub API request to:', `${GITHUB_API_BASE}/search/repositories`);
  console.log('Search params:', params);
  
  const headers = getGitHubHeaders();
  console.log('Headers being sent:', {
    Accept: headers.Accept,
    Authorization: headers.Authorization ? 'Bearer [TOKEN]' : 'No token',
    'X-GitHub-Api-Version': headers['X-GitHub-Api-Version']
  });
  
  try {
    const response = await axios.get(`${GITHUB_API_BASE}/search/repositories`, {
      headers,
      params
    });
    console.log('GitHub API request successful');
    return response.data;
  } catch (error: any) {
    console.error('GitHub API Error:', error.response?.status, error.response?.data);
    throw error;
  }
};

const searchIssues = async (params) => {
  try {
    const response = await axios.get(`${GITHUB_API_BASE}/search/issues`, {
    headers: getGitHubHeaders(),
    params
    });
    return response.data;
  } catch (error: any) {
    throw error;
  } 
};

const searchLabels = async (params: SearchParams): Promise<any> => {
    console.log('Making GitHub API request to:', `${GITHUB_API_BASE}/search/labels`);
    console.log('Search params:', params);
    console.log('Full URL would be:', `${GITHUB_API_BASE}/search/labels?${new URLSearchParams(params as any).toString()}`);

    const cleanParams = Object.fromEntries(
        Object.entries(params).filter(([_, value]) => value !== undefined)
    );

    console.log('Cleaned params: ', cleanParams);
    
    try {
      const response = await axios.get(`${GITHUB_API_BASE}/search/labels`, {
        headers: getGitHubHeaders(),
        params: cleanParams
      });
      console.log('GitHub API request successful');
      return response.data;
    } catch (error: any) {
      console.error('GitHub API Error for labels:');
      console.error('Status:', error.response?.status);
      console.error('Error Data:', error.response?.data);
      console.error('Request URL:', error.config?.url);
      console.error('Request params:', error.config?.params);
      throw error;
    }
  };

const searchTopics = async (params: SearchParams): Promise<any> => {
    console.log('Making GitHub API request to:', `${GITHUB_API_BASE}/search/topics`);
    console.log('Search params:', params);
    console.log('Full URL would be:', `${GITHUB_API_BASE}/search/topics?${new URLSearchParams(params as any).toString()}`);
    
    const cleanParams = Object.fromEntries(
      Object.entries(params).filter(([_, value]) => value !== undefined)
    );
      
    console.log('Cleaned params:', cleanParams);

    try {
      const response = await axios.get(`${GITHUB_API_BASE}/search/topics`, {
        headers: getGitHubHeaders(),
        params
      });
      console.log('GitHub API request successful');
      return response.data;
    } catch (error: any) {
      console.error('GitHub API Error for topics:');
      console.error('Status:', error.response?.status);
      console.error('Error Data:', error.response?.data);
      console.error('Request URL:', error.config?.url);
      console.error('Request params:', error.config?.params);
      throw error;
    }
  };

module.exports = {
  searchRepositories,
  searchIssues,
  searchLabels,
  searchTopics
};