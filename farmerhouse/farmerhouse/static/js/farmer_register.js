function myFunction() {
  var x = document.querySelector("#confirm2");
  var y = document.querySelector("#password2");
  if (x.type == "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }

  if (y.type == "password") {
    y.type = "text";
  } else {
    y.type = "password";
  }
}
function checkPass() {
  //Store the password field objects into variables ...
  var password = document.getElementById("password2");
  var confirm = document.getElementById("confirm2");
  //Store the Confirmation Message Object ...
  var message = document.getElementById("confirm-message2");
  //Set the colors we will be using ...
  var good_color = "#66cc66";
  var bad_color = "#ff6666";
  var empty_color = "#fff";
  //Compare the values in the password field
  //and the confirmation field
  if (password.value == confirm.value) {
    //The passwords match.
    //Set the color to the good color and inform
    //the user that they have entered the correct password
    confirm.style.backgroundColor = good_color;
    password.style.backgroundColor = good_color;
    message.style.color = good_color;
    message.textContent = "Passwords Match";
    // message.innerHTML = '<img src="/images/tick.jpg" alt="Passwords Match!">';
  } else if (password.value == "" || confirm.value == "") {
    confirm.style.backgroundColor = empty_color;
    password.style.backgroundColor = empty_color;
  } else {
    //The passwords do not match.
    //Set the color to the bad color and
    //notify the user.
    confirm.style.backgroundColor = bad_color;
    password.style.backgroundColor = bad_color;
    message.style.color = bad_color;
    message.textContent = "Passwords Do Not Match";
    // message.innerHTML =
    // '<img src="/wp-content/uploads/2019/04/publish_x.png" alt="Passwords Do Not Match!">';
  }
}