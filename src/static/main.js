// JS
let enctype = 'encrypt';
let algorithm = 'vigenere';
let inputtype = 'text';
let submitURL = ''
const form = document.getElementById('form');
const resultDiv = document.getElementById('result');

window.onload = () => {
    console.log("OK");
}

function setRequestToJSON() {
    // Get form data
    const formData = new FormData(form);

    // Convert form data to JSON
    const jsonData = {};
    formData.forEach((value, key) => {
        jsonData[key] = value;
    });

    return jsonData;
}

function setURL(algorithm, enctype, inputtype) {
    let url = ''
    if (enctype === 'encrypt' && inputtype === 'text') {
        url = `/${algorithm}/encrypt`
    }
    else if (enctype === 'encrypt' && inputtype === 'file') {
        url = `/${algorithm}/encryptfile`
    }
    else if (enctype === 'decrypt' && inputtype === 'text') {
        url = `/${algorithm}/decrypt`
    }
    else if (enctype === 'decrypt' && inputtype === 'file') {
        url = `/${algorithm}/decryptfile`
    }
    document.getElementById("form").action = url;
    submitURL = url
    console.log(url);
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    let reqBody = setRequestToJSON();
    console.log(submitURL);
    console.log(JSON.stringify(reqBody));
    fetch(`${submitURL}`, {
        method: "POST",
        headers: {
            applicationType: "application/json",
        },
        body: JSON.stringify(reqBody)
    })
    .then(response => response.json())
    .then(data => {
        // Display response in the result div
        resultDiv.innerHTML = `${JSON.stringify(data, null, 2)}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
})

document.getElementById("encryptselect").addEventListener("click", () => {
    enctype = "encrypt";
    setURL(algorithm, enctype, inputtype);
})

document.getElementById("decryptselect").addEventListener("click", () => {
    enctype = "decrypt";
    setURL(algorithm, enctype, inputtype);
})

document.getElementById("textselect").addEventListener("click", () => {
    inputtype = "text";
    setURL(algorithm, enctype, inputtype);
})

document.getElementById("fileselect").addEventListener("click", () => {
    inputtype = "file";
    setURL(algorithm, enctype, inputtype);
})

document.getElementById("algoselect").addEventListener("change", () => {
    algorithm = document.getElementById("algoselect").value;
    setURL(algorithm, enctype, inputtype);
})
