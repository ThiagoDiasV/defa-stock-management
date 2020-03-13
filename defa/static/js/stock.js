function drawTable(data) {
    let table = $("#table-category");
    table.css('opacity', '1');
    let tableBody = $("#table-body");
    tableBody.empty();
    for (let i = 0; i < data.length; i ++) {
        let row1 = (`<td>${data[i].fields.category}</td>`);
        let row2 = (`<td>${data[i].fields.description}</td>`);
        let row3 = (`<td>${data[i].fields.presentation}</td>`);
        let row4 = (`<td>${data[i].fields.quantity}</td>`);
        let rowArray = [row1, row2, row3, row4];
        let fullRow = '';
        for (let i = 0; i < rowArray.length; i++) {
            fullRow += rowArray[i];
        }
        tableBody.append(`<tr>${fullRow}</tr>`);
    }
}

$("#submit-category").click((e) => {
    e.preventDefault();
    let selectedCategory = $("#id_category option:selected").text();
    $.ajax({
        type:"GET",
        url: "category",
        dataType: "json",
        data:{category: selectedCategory},
        success: (data) => {
            drawTable(data);
        }
    })
});