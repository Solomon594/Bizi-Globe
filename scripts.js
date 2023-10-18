document.addEventListener("DOMContentLoaded", function () {
    const panels = document.querySelectorAll(".panel");

    panels.forEach(panel => {
        const section = panel.closest(".section");
        const heading = section.querySelector("h2");

        heading.addEventListener("click", () => {
            panel.classList.toggle("active");
        });
    });


    const dataForm = document.getElementById("dataForm");
    dataForm.addEventListener("submit", function (event) {
        event.preventDefault();
        
        const formData = new FormData(dataForm);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        // Send the data to the server for storage (using AJAX or Fetch API)
        // Example: Use fetch to send data to a server endpoint
        fetch("/store_data", {
            method: "POST",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json"
            }
        })
        .then(response => response.json())
        .then(result => {
            console.log("Data stored:", result);
        })
        .catch(error => {
            console.error("Error storing data:", error);
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const rightPanel = document.getElementById("rightPanel"); // Get the right panel by ID

    // Add click event listener to toggle the active class on right panel
    rightPanel.addEventListener("click", function() {
        this.classList.toggle("active");
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const imageGallery = document.querySelector(".image-gallery");
    const images = imageGallery.getElementsByTagName("img");
    let currentIndex = 0;

    function showImage(index) {
        for (let i = 0; i < images.length; i++) {
            images[i].style.display = "none";
        }
        images[index].style.display = "block";
    }

    function switchImage() {
        currentIndex = (currentIndex + 1) % images.length;
        showImage(currentIndex);
    }

    // Initially show the first image
    showImage(currentIndex);

    // Set interval to switch images every 3 seconds
    setInterval(switchImage, 5000);
});


//Switch text in sidebar
document.addEventListener("DOMContentLoaded", function() {
    const imageGallery = document.querySelector(".image-gallery");
    const images = imageGallery.getElementsByTagName("img");
    const paragraphList = document.querySelector(".paragraph-list");
    const paragraphs = paragraphList.getElementsByTagName("p");
    
    let currentIndexImages = 0;
    let currentIndexParagraphs = 0;

    function showImage(index) {
        for (let i = 0; i < images.length; i++) {
            images[i].style.display = "none";
        }
        images[index].style.display = "block";
    }

    function showParagraph(index) {
        for (let i = 0; i < paragraphs.length; i++) {
            paragraphs[i].style.display = "none";
        }
        paragraphs[index].style.display = "block";
    }

    function switchContent() {
        currentIndexImages = (currentIndexImages + 1) % images.length;
        currentIndexParagraphs = (currentIndexParagraphs + 1) % paragraphs.length;
        
        showImage(currentIndexImages);
        showParagraph(currentIndexParagraphs);
    }

    // Initially show the first image and paragraph
    showImage(currentIndexImages);
    showParagraph(currentIndexParagraphs);

    // Set interval to switch content every 5 seconds
    setInterval(switchContent, 5000);
});
