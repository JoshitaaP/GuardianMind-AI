console.log("GuardianMind Content Script Loaded");

chrome.runtime.sendMessage(
    { type: "analyze" },
    (response) => {

        console.log(
            "GuardianMind Response:",
            response
        );
    }
);