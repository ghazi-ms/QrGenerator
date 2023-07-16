$("form").submit(function (e) {
  e.preventDefault();

  var firstName = $("#firstName").val();
  var LastName = $("#LastName").val();
  var email = $("#email").val();
  var phoneNumber = $("#phoneNumber").val();
  var data = [
    {
      Fname: firstName,
      Lname: LastName,
      email: email,
      phoneNumber: phoneNumber,
    },
  ];
  fetch("/createQr", {
    headers: {
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify(data),
  })
    .then(function (response) {
      if (response.ok) {
        response.json().then(function (response) {
          $("#secondLayout").addClass("hide");
          $("#Success").removeClass("hide");

          window.open("static/users/"+response.filename, '_blank');
        });
      } else {
           $("#secondLayout").addClass("hide");
          $("#invalid").removeClass("hide");

        throw Error("Something went wrong");
      }
    })
    .catch(function (error) {
      console.log(error);
    });
});
