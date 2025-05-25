import { error } from 'console';
import type { Request, Response } from 'express';
const { Router } = require('express');
const { searchLabels } = require('../../services/github.service');

const router = Router();

// interface SearchParams {
//     q: string;
//     sort?: string;
//     order?: string;
//     per_page?: number;
//     page?: number;
//   }

router.get('/', async (req: Request, res: Response) => {
    try {
        const { repository_id, q } = req.query;

        if (!repository_id) {
            return res.status(400).json({ error: 'Repository ID is required for label search.'})
        }

        if (!q) {
            return res.status(400).json({ error: 'Search query (q) is required.'});
        }

        // Type cast req.query to fit types for req and res
        const SearchParams = {
            repository_id: String(repository_id),
            q: String(q),
            sort: req.query.sort ? String(req.query.sort) : undefined,
            order: req.query.order ? String(req.query.order) : undefined,
            per_page: req.query.per_page ? Number(req.query.per_page) : undefined,
            page: req.query.page ? Number(req.query.page) : undefined
        };

        // Call the service function
        const data = await searchLabels(SearchParams);
        res.json(data);
    } catch (error: any) {
        console.error('Error searching labels: ', error.message);
        res.status(error.response?.status || 500).json({
            message: error.message,
            githubError: error.response?.data
        });
    }
});

module.exports = router;