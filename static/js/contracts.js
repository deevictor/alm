$(document).ready(function(){

  $("label").addClass("checkbox-inline");

  $("#aggr_table").on("click", "td", function(){

    var month_id_selected = $(this).attr('id')

    var contracts = {};

    var js_obj_dict = JSON.parse(json_dict)
    for (var month_id in js_obj_dict) {
      contracts[month_id] = JSON.parse(js_obj_dict[month_id]);
    }
    console.log(js_obj_dict)

    contracts_month = contracts[month_id_selected]

    $("#table_ct").html(build_details_table(contracts_month));

    $('html, body').animate({
      scrollTop: $("#aggr_table").offset().top
    }, 'slow');



  });

  function build_details_table(contracts_array) {
    if (contracts_array.length != 0) {
      var details_table = $('<table>').addClass('table table-bordered');
      var head = $('<thead>').html('<tr><th>Организация</th><th>Тип контракта</th><th>Валюта</th><th>Сумма контракта</th></tr>');
      details_table.append(head)

      for(var i=0; i<contracts_array.length; i++){
        var row = $('<tr>')
        for (var arg in contracts_array[i].fields) {
          row.append($('<td>').text(contracts_array[i].fields[arg]));
        }
        details_table.append(row)
      }
      return details_table;
    }
    else {return ''}
  }

});