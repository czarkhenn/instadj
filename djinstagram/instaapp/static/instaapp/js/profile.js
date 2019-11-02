$(document).ready(function() {
    "use strict";

    var opts = {
        beforeSubmit: beforesub,
        success: successcall
    }

    $('#uploadDp').on('submit', function(e) {
        e.preventDefault();

        $(this).ajaxSubmit(opts);

    });

    function beforesub(formData, jqForm, options) {
        console.log("submitting")
    }

    function successcall(responseText, statusText, xhr, $form) {
        console.log(responseText);
        console.log(xhr);
    }
    function UploadClick(e) {
        e.preventDefault();
    
        var t = $(this),
        user_to_unfollow = t.data('user');
    
        $.ajax({
          url: '/insta/viewprofile/',
          data: {uid: user_to_unfollow},
          dataType: 'json',
          type: 'post',
          success: function(data) {
            if (data.status == 1) {
              window.location.reload();
            } else {
              $('#notLoggedInModal').modal('show');
            }
          }
        });
      }
});
