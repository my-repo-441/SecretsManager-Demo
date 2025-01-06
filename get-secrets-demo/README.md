# AI-Powered Blog Generation and Content Fetching Tool

This project is a React-based web application that leverages AI to generate blog content and fetch relevant articles based on user input.

The application consists of two main features: a blog generation tool that uses OpenAI's API to create blog posts, and a content fetching tool that retrieves articles based on user-specified keywords. It provides a user-friendly interface for content creation and research, making it useful for bloggers, content creators, and researchers.

## Repository Structure

```
.
├── frontend/
│   ├── dist/
│   ├── src/
│   │   ├── components/
│   │   │   ├── common/
│   │   │   ├── FetchContent/
│   │   │   ├── GenerateBlog/
│   │   │   ├── Layout.jsx
│   │   │   └── Navbar.jsx
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   ├── index.jsx
│   │   └── Root.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── Lambda/
    └── .serverless/
        └── requirements/
```

### Key Files:
- `frontend/src/index.jsx`: Entry point of the React application
- `frontend/src/components/GenerateBlog/GenerateBlog.jsx`: Component for blog generation
- `frontend/src/components/FetchContent/FetchContent.jsx`: Component for content fetching
- `frontend/src/hooks/useGenerateBlog.js`: Custom hook for blog generation logic
- `frontend/package.json`: Project dependencies and scripts
- `Lambda/.serverless/requirements/`: Backend dependencies for serverless functions

## Usage Instructions

### Installation

1. Ensure you have Node.js (version 14 or later) and npm installed.
2. Clone the repository:
   ```
   git clone <repository-url>
   ```
3. Navigate to the frontend directory:
   ```
   cd frontend
   ```
4. Install dependencies:
   ```
   npm install
   ```

### Getting Started

1. Start the development server:
   ```
   npm run dev
   ```
2. Open your browser and navigate to `http://localhost:3000` (or the port specified by Vite).

### Blog Generation

1. Navigate to the blog generation page.
2. Enter a blog title, keywords, and iteration parameters.
3. Click "Generate Blog" to start the AI-powered blog creation process.
4. Monitor the status log for progress updates.
5. Once complete, view the generated blog content and use the "Preview" button for a formatted view.

### Content Fetching

1. Go to the content fetching page.
2. Enter search keywords and specify the number of articles to fetch.
3. Click "Fetch Articles" to retrieve relevant content.
4. View the fetched articles displayed as cards.

### Configuration

- The application uses environment variables for API endpoints. In development, it uses a local `/api` endpoint, while in production it uses a deployed AWS Lambda function.
- To change the API endpoint, modify the `BASE_URL` variable in `frontend/src/hooks/useGenerateBlog.js`.

### Troubleshooting

- If you encounter CORS issues, ensure that your backend API is configured to allow requests from your frontend's domain.
- For API-related errors, check the browser console and the application's error messages for more details.

## Data Flow

1. User inputs blog title, keywords, and parameters in the frontend.
2. Frontend sends a POST request to the backend API to initiate blog generation.
3. Backend processes the request, potentially using OpenAI's API for content generation.
4. Frontend polls the backend for results at regular intervals.
5. Once complete, the generated blog content is displayed to the user.
6. For content fetching, the frontend sends a request with search parameters.
7. Backend retrieves relevant articles and returns them to the frontend.
8. Frontend displays the fetched articles to the user.

```
[User Input] -> [Frontend] -> [Backend API] -> [OpenAI API]
                    ^                |
                    |                v
              [Display Results] <- [Process & Return Data]
```

## Deployment

The frontend is built using Vite and can be deployed to any static hosting service. The backend uses AWS Lambda functions, which can be deployed using the Serverless Framework.

1. Build the frontend:
   ```
   npm run build
   ```
2. Deploy the generated `dist` folder to your chosen hosting service.
3. Deploy the Lambda functions using the Serverless Framework (ensure AWS credentials are configured).