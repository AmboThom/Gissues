export const GITHUB_API_BASE = 'https://api.github.com';

export const getGitHubHeaders = () => ({
    'Accept': 'application/vnd.github+json',
    'Authorization' : `Bearer ${process.env.GITHUB_TOKEN}`,
    'X-GitHub-Api-Version' : '2022-11-28'
});

module.exports = {
    GITHUB_API_BASE,
    getGitHubHeaders
};