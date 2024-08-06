---
layout: blog
title:  "Azure AI Language on 7/26/24 Journal Entry!"
#date:   2024-07-26 10:29:40 -0500
categories: jekyll update
---

Welcome to a foray into using the Azure AI service in the backend on one of my handwritten journal entries for today! This was published on {{ page.date }}. (Not connected to active Azure AI Service...)

<h1>Extract Text from Image</h1>
<form id="uploadForm">
    <input type="file" id="imageInput" name="image">
</form>
<img id="uploadedImage" alt="Uploaded Image">
<button id="runAIButton">Run AI Service</button>
<div id="result"></div>

<script>
    document.getElementById('imageInput').addEventListener('change', function(event) {
        const imageInput = event.target.files[0];
        const reader = new FileReader();
        
        reader.onload = function(e) {
            const uploadedImage = document.getElementById('uploadedImage');
            uploadedImage.src = e.target.result;
            uploadedImage.style.display = 'block';
            document.getElementById('runAIButton').style.display = 'block';
        }
        
        reader.readAsDataURL(imageInput);
    });

    document.getElementById('runAIButton').addEventListener('click', async function(event) {
        const imageInput = document.getElementById('imageInput').files[0];
        const formData = new FormData();
        formData.append('image', imageInput);

        console.log("Running AI service...");  // Log AI service start

        try {
            const response = await fetch('http://localhost:5000/extract-text', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            console.log("Extracted Text:", result.text);  // Log the extracted text

            document.getElementById('result').innerText = result.text;
        } catch (error) {
            console.error("There was an error with the request:", error);
            document.getElementById('result').innerText = "Error extracting text. Please try again.";
        }
    });
</script>