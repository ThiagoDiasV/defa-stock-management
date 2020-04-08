function drawTable(data) {
  let table = $('#table-list-name');
  table.css('opacity', '1');
  let tableBody = $('#table-body');
  tableBody.empty();
  for (let i = 0; i < data.length; i++) {
    let row1 = `<td>${data[i].fields.list_name}</td>`;
    let row2 = `<td>${data[i].fields.product_description}</td>`;
    let row3 = `<td>${data[i].fields.catmat}</td>`;
    let row4 = `<td>${data[i].fields.unit}</td>`;
    let rowArray = [row1, row2, row3, row4];
    let fullRow = '';
    for (let i = 0; i < rowArray.length; i++) {
      fullRow += rowArray[i];
    }
    tableBody.append(`<tr>${fullRow}</tr>`);
  }
}

$('#submit-list-name').click((e) => {
  e.preventDefault();
  let selectedListName = $('#id_list_name option:selected').text();
  $.ajax({
    type: 'GET',
    url: 'list_name',
    dataType: 'json',
    data: { list_name: selectedListName },
    success: (data) => {
      drawTable(data);
    },
  });
});
