const { Router } = require('express');
const repositoryRoutes = require('./repositories');
const issueRoutes = require('./issues');
const labelRoutes = require('./labels');
const topicRoutes = require('./topics');

const router = Router();

// Register routes
router.use('/search/repositories', repositoryRoutes);
router.use('/search/issues', issueRoutes);
router.use('/search/labels', labelRoutes);
router.use('/search/topics', topicRoutes);

module.exports = router;