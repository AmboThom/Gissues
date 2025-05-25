import { User } from './user.model';
import { Label } from './label.model';

export interface IssueSearchResponse {
    total_count: number;
    incomplete_results: boolean;
    items: Issue[];
}

export interface Issue {
    id: number;
    number: number;
    title: string;
    state: 'open' | 'closed';
    user: User;
    labels: Label[];
    body: string;
    created_at: string;
    updated_at: string;
    html_url: string;
    locked: boolean;
    closed_at: string | null;
    comments: number;
}