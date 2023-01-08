inputs = [
    { name: "small_bags", value: "number" },
    { name: "large_bags", value: "number" },
    { name: "XL_bags", value: "number" },
    { name: "type", value: "text" },
    { name: "year", value: "number" },
    { name: "region", value: "text" }
]


function createInput(element) {
    const input = document.createElement("input")

    input.type = element.value
    input.id = element.name
    input.name = element.name
    input.className = "input"

    return input
}

function createLabel(element) {
    const label = document.createElement("label");

    label.for = element.name
    label.className = "placeholder"
    label.innerHTML = element.name

    return label
}

function createContainer(element) {
    const input = createInput(element)
    const cut = document.createElement("div")
    cut.className = "cut"
    const label = createLabel(element)
    const container = document.createElement("div")
    container.className = "input-container ic2"

    container.appendChild(input)
    container.appendChild(cut)
    container.appendChild(label)

    return container
}

function main() {
    const form = document.getElementById("form")

    inputs.forEach((element) => {
        form.appendChild(createContainer(element))
    })

    const button = document.createElement("button")
    button.className = "submit"
    button.textContent = "submit"
    button.type = "button"
    button.onclick = sendPostReq

    const body = document.getElementById("body")
    body.appendChild(button)
}

main()