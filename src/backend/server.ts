import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import routes from './routes';

// Loads the environment variables
dotenv.config();

// Creates Express app
const app = express();
const PORT = process.env.PORT || 3000;

// Applies middleware
app.use(cors());
app.use(express.json());

// Checks endpoint health
app.get('/api/health', (req, res) => {
    res.json({
        status: 'ok',
        message: 'Server is running.'
    });
});

// Register API routes
app.use('/api', routes);

// Start server
app.listen(PORT, () => {
    console.log('Server running on http://localhost:{PORT}');
});