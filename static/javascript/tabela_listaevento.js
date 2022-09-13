   /* Initialization of datatables */
      $(document).ready(function () {

        // Paging and other information are
        // disabled if required, set to true
        var myTable = $("#example").DataTable({
          paging: true,
          searching: true,
          info: false,
        });

      });