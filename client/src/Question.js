export default function Question() {
    async function fetchQuestions() {
        try {
        const response = await fetch('http://127.0.0.1:8000/generate_question/', {  // Adjust the endpoint if necessary
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            // You can include body data if your Django view expects it
        });
    
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
    
        const data = await response.json();
        console.log('Received list of strings:', data.question);  // Process the list of strings as needed
    
        return data.question;  // Return the list for further processing
        } catch (error) {
        console.error('Error fetching string list:', error);
        return [];  // Return an empty array or handle the error as needed
        }
    }
}
    