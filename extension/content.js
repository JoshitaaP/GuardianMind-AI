console.log("GuardianMind Content Script Loaded");

const currentUrl = window.location.href;

console.log("Current URL:", currentUrl);

chrome.runtime.sendMessage(
    {
        type: "analyze",
        url: currentUrl
    },
    (response) => {

        console.log("GuardianMind Response:", response);

        if (response.action === "block") {

            document.body.innerHTML = `
                <div style="
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    height:100vh;
                    font-family:Arial;
                    background:#111;
                    color:white;
                    flex-direction:column;
                ">
                    <h1>Access Blocked</h1>

                    <h2>${response.category}</h2>

                    <p>Risk Score: ${response.risk}</p>
                </div>
            `;
        }
        if(response.action==="warn"){
        const originalPage=document.body.innerHTML;
            document.body.innerHTML=`
                <div style="
                    display:flex;
                    justify-content:center;
                    height:100vh;
                    background:#111;
                    color:white;
                    font-family:Arial;
                    flex-direction:column;
                ">
                    <h1> !!Waring!! </h1>
                    <h2>${response.category}</h2>
                    <p>Risk Score: ${response.risk}</p>
                    <button id="continueBtn"
                        style="
                            padding:12px 20px;
                            font-size:18px;
                            cursor:pointer;
                            margin-top:20px;
                    ">
                        Continue
                    </button>
                </div>
            `;
            document
                .getElementById("continueBtn")
                .addEventListener("click",()=>{
                    document.body.innerHTML=originalPage;
                });
        }
    }
);