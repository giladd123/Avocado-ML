async function sendPostReq() {
    const form = document.getElementById("form");
    const formData = new FormData(form);
    const formDataObj = {};
    formData.forEach((value, key) => (formDataObj[key] = value));

    const response = await fetch("/api", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formDataObj)
    })
    const res = await response.text()
    printResponse(res)
}

function printResponse(res) {
    const body = document.getElementById('body')
    const text = document.getElementById('text')
    if (!text) {
        const p = document.createElement('p')
        p.innerHTML = res
        p.className = "answer"
        p.id = 'text'
        body.appendChild(p)
    } else {
        text.innerHTML = res
    }

}