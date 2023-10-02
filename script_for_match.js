<script>
        const searchForm = document.getElementById("searchForm");
        const resultDiv = document.getElementById("result");

        searchForm.addEventListener("submit", function (event) {
            event.preventDefault();

            const region = document.getElementById("region").value;
            const town = document.getElementById("town").value;

            fetch("/search_businesses", {
                method: "POST",
                body: JSON.stringify({ region, town }),
                headers: {
                    "Content-Type": "application/json"
                }
            })
            .then(response => response.json())
            .then(data => {
                const businesses = data.matching_businesses;
                if (businesses.length > 0) {
                    resultDiv.innerHTML = `<h2>Matching Businesses:</h2><ul>${businesses.map(business => `<li>${business}</li>`).join("")}</ul>`;
                } else {
                    resultDiv.innerHTML = "<p>No matching businesses found.</p>";
                }
            })
            .catch(error => {
                console.error("Error searching businesses:", error);
            });
        });
    </script>