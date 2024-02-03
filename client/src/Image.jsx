import React from 'react'
import openai from 'openai'

export default function Image() {

  async function fetchURL() {
    try {
      const response = fetch('/your-backend-endpoint/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData)
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      console.log('URL from backend:', data.url); // 'data.url' should be replaced with the actual key used in the JSON response
    } 
    catch (error) {
      console.error('Error fetching URL from backend:', error);
    }

  return (
    <div>{data.url}</div>
  )}

  fetchURL()
}
