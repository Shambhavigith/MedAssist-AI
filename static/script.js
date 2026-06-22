const form = document.getElementById("chat-form");

form.addEventListener("submit", async (e) => {

    e.preventDefault();

    const message = document.getElementById("message").value;

    const formData = new FormData();
    formData.append("message", message);

    const response = await fetch("/chat", {
        method: "POST",
        body: formData
    });

    const answer = await response.text();

    document.getElementById("response").innerHTML =
        `<strong>Answer:</strong><br><br>${answer}`;
});
