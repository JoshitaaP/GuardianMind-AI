console.log("GuardianMind Content Script Loaded");

const currentUrl = window.location.href;
console.log("Current URL:", currentUrl);

chrome.runtime.sendMessage(
    {
        type: "analyze",
        url: currentUrl
    },
    (response) => {

        console.log(
            "GuardianMind Response:",
            response
        );
    }
);