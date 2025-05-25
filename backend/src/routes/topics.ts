import type { Request, Response } from 'express';

const { Router } = require('express');
const { searchTopics } = require('../../services/github.service');

const router = Router();

router.get('/', async (req: Request, res: Response) => {
    try {
        const { q } = req.query;

        if (!q) {
            return res.status(400).json({ error: 'Search query (q) is required.'});
        }

        console.log('Topics route - recieved query: ', q);

        // Type cast req.query to fit types for req and res
        const SearchParams = {
            q: String(q),
            per_page: req.query.per_page ? Number(req.query.per_page) : undefined,
            page: req.query.page ? Number(req.query.page) : undefined
        };

        console.log('Topics route - calling searchTopics with: ', SearchParams);

        // Call the service function
        const data = await searchTopics(SearchParams);
        res.json(data);
    } catch (error: any) {
        console.error('Error searching Topics: ', error.message);
        res.status(error.response?.status || 500).json({
            message: error.message,
            githubError: error.response?.data
        });
    }
});

module.exports = router;