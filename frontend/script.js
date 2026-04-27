async function sendMessage() {

    const input = document.getElementById("question");
    const question = input.value.trim();

    if (!question) return;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user">${question}</div>`;

    input.value = "";

    chatBox.innerHTML += `<div class="bot" id="loading">Thinking...</div>`;

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question })
    });

    const data = await response.json();

    document.getElementById("loading").remove();

    chatBox.innerHTML += `
        <div class="bot">
            <b>${data.answer}</b>

            <div class="raw">
                <details>
                    <summary>View Raw Result</summary>
                    <pre>${JSON.stringify(data.raw_result, null, 2)}</pre>
                </details>
            </div>
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}