export default function Image(requestData, cb) {
  async function fetchURL(requestData) {
    fetch("http://127.0.0.1:8000/image/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
    })
    .then(response => response.json())
    .then(data => {
      console.log("URL from backend:", data["url"]); // 'data.url' should be replaced with the actual key used in the JSON response
      cb(data["url"]);
    })
    .catch (error => {
      console.error("Error fetching URL from backend:", error);
      return null;
    })
  }

  fetchURL(requestData);
}

// if (!response.ok) {
//   throw new Error(`HTTP error! status: ${response.status}`);
// }
