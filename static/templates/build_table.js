document.getElementById("uploadForm").addEventListener("submit", async function(event) {
    event.preventDefault();
    let fileInput = document.getElementById("fileInput");
    let status = document.getElementById("status");
    let tableBody = document.getElementById("dataTable");

    if (fileInput.files.length === 0) {
        status.innerText = "Please select a file.";
        return;
    }

    let formData = new FormData();
    formData.append("text_file", fileInput.files[0]);

    try {
        let response = await fetch("/build_table/", {
            method: "POST",
            body: formData
        });

        if (response.status === 415) {
            status.innerText = "Not a UTF-8 text file.";
            return;
        }

        let result = await response.json();

        if (result.rows) {
            status.innerText = "Upload successful!";
            tableBody.innerHTML = "";
            Object.entries(result.rows).forEach(([id, values]) => {
                let row = `<tr class='border hover:bg-blue-50 transition'>
                    <td class='px-6 py-3 border'>${id}</td>
                    <td class='px-6 py-3 border'>${values[0]}</td>
                    <td class='px-6 py-3 border'>${values[1]}</td>
                    <td class='px-6 py-3 border'>${values[2]}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        } else {
            status.innerText = "Unexpected response format!";
        }
    } catch (error) {
        console.error("Error:", error);
        status.innerText = "Upload failed.";
    }
});