// This keeps Colab running
function clickConnect() {
    console.log("Keeping Colab alive...");
    document.querySelector("#connect")?.click();
}
setInterval(clickConnect, 60000);
