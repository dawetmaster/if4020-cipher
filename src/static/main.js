// JS
let enctype = 'encrypt';
let algorithm = 'vigenere';
let inputtype = 'text';

window.onload = () => {
    console.log("OK");
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
    console.log(url);
}

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
