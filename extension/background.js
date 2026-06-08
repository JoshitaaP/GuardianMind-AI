
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

    console.log("Message received:", request);

    if (request.type === "analyze") {

        console.log("Calling Flask API");

        fetch("http://127.0.0.1:5000/analyze")
            .then(response => response.json())
            .then(data => {
                console.log("Flask returned:", data);
                sendResponse(data);
            })
            .catch(error => {
                console.error("Fetch error:", error);
            });

        return true;
    }
});