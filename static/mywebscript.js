function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    if (!textToAnalyze || textToAnalyze.trim() === "") {
        document.getElementById("system_response").innerHTML = "Invalid text! Please try again!";
        return;
    }

    fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze))
        .then(response => response.text())
        .then(result => {
            if (result.includes("Invalid text!")) {
                document.getElementById("system_response").innerHTML = result;
            } else {
                document.getElementById("system_response").innerHTML = result;
            }
        })
        .catch(err => {
            document.getElementById("system_response").innerHTML = "An error occurred. Please try again.";
            console.error(err);
        });
}