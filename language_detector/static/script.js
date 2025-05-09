function detectLanguage() {
    const text = document.getElementById("inputText").value;

    fetch("/detect", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: text }),
    })
    .then(response => response.json())
    .then(data => {
        const message = `${data.language} `;
        document.getElementById("output").innerText = message;
        speak(message + ". The sentence is: " + data.sentence);
    });
}

function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(utterance);
}
