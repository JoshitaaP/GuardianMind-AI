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
                    align-items:center;
                    height:100vh;
                    background:#111;
                    color:white;
                    font-family:Arial;
                ">
                    <div style="
                        text-align: center;
                            padding:40px;
                        background:#1e1e1e;
                        border-radius:15px;
                        box-shadoq: 0 0 20pc rgba(255,255,0,0,3);
                        width: 500px;
                    ">
                        <h1> 🛡 GuardianMind Warning </h1>
                        <h2>${response.category}</h2>
                        <p style ="font-size:20px;">Risk Score: ${response.risk}%</p>
                        <p> This website may impact productivity and increase screen time.</p>
                        <div style="margin-top:25px;">
                            <button id="goBackBtn"
                                style="
                                padding:12px 20px;
                                margin-right:10px;
                                background:#d9534f;
                                color:white;
                                border:none;
                                cursor:pointer;
                                ">
                                Go Back
                            </button>

                            <button id="continueBtn"
                                style="
                                padding:12px 20px;
                                background:#f0ad4e;
                                color:white;
                                border:none;
                                cursor:pointer;
                                ">
                                Continue Anyway
                            </button>
                        </div>
                    </div>
                </div>
            `;
            document
                .getElementById("continueBtn")
                .addEventListener("click",()=>{
                    document.body.innerHTML=originalPage;
                });
            document
                .getElementById("goBackBtn")
                .addEventListener("click",()=>{
                console.log("Go Back clicked");
                    if(window.history.length>1){
                        window.history.back();
                    }else{
                        window.location.href="https://www.google.com";
                    }
                });
        }
    }
);