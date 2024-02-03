export default function Image(requestData) {
  async function fetchURL(requestData) {
    try {
      const response = fetch("http://127.0.0.1:8000/image/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: {
          prompt: requestData,
        },
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      console.log("URL from backend:", data); // 'data.url' should be replaced with the actual key used in the JSON response
      return data.url;
    } catch (error) {
      console.error("Error fetching URL from backend:", error);
      return null;
    }
  }

  fetchURL(requestData);
}
