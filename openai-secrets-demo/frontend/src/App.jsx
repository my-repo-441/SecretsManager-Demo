import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  const fetchResponse = async () => {
    setLoading(true);
    setError('');
    try {
      const result = await axios.post('https://785o0bqb6d.execute-api.ap-northeast-1.amazonaws.com/invoke-openai', {
        prompt: input,
      });
      setResponse(result.data.message);
    } catch (err) {
      setError('Error fetching response from the server.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ fontFamily: 'Arial, sans-serif', padding: '20px' }}>
      <h1>OpenAI API Test</h1>
      <textarea
        rows="4"
        cols="50"
        placeholder="Enter your prompt here..."
        value={input}
        onChange={handleInputChange}
        style={{ padding: '10px', marginBottom: '10px' }}
      />
      <br />
      <button
        onClick={fetchResponse}
        disabled={loading}
        style={{
          padding: '10px 20px',
          backgroundColor: '#007BFF',
          color: 'white',
          border: 'none',
          cursor: 'pointer',
          marginBottom: '20px',
        }}
      >
        {loading ? 'Loading...' : 'Submit'}
      </button>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {response && (
        <div style={{ marginTop: '20px', border: '1px solid #ddd', padding: '10px' }}>
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
