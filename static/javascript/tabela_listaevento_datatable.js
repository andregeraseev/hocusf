$(function() {
        $("#export").click(function(e){
          var table = $("#example");
          if(table && table.length){
            $(table).table2excel({
              exclude: ".noExl",
              name: "Excel Document Name",
              filename: "ListaEntrada" + new Date().toISOString().replace(/[\-\:\.]/g, "") + ".xls",
              fileext: ".xls",
              exclude_img: true,
              exclude_links: true,
              exclude_inputs: true,
              preserveColors: false
            });
          }
        });

      });
