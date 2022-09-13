
      /* Initialization of datatables */
      $(document).ready(function () {

        // Paging and other information are
        // disabled if required, set to true
        var myTable = $("#example").DataTable({
          paging: true,
          searching: true,
          info: false,
        });

        // 2d array is converted to 1D array
        // structure the actions are
        // implemented on EACH column
        myTable
          .columns(3)
          .flatten()
          .each(function (colID) {

            // Create the select list in the
            // header column header
            // On change of the list values,
            // perform search operation
            var mySelectList = $("<select />")
              .appendTo(myTable.column(3).header())
              .on("change", function () {
                myTable.column(3).search($(this).val());

                // update the changes using draw() method
                myTable.column(colID).draw();
              });

            // Get the search cached data for the
            // first column add to the select list
            // usinh append() method
            // sort the data to display to user
            // all steps are done for EACH column
            myTable
              .column(3)
              .cache("search")
              .sort()
              .each(function (param) {
                mySelectList.append(
                  $('<option value="' + param + '">'
                    + param + "</option>")
                );
              });
          });
      });