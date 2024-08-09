function signup() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var email = document.getElementById("email").value;
    // var go_to_login = document.getElementById("go_to_login").value;
    // location.href = "/home/chinmay/CCV2/CCV2/UI/login.html";
    //alert("Your prog is " + head);
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = JSON.stringify({
        "user_name": username,
        "password": password,
        "email": email
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("http://0.0.0.0:5678/signup", requestOptions)
        .then(response => response.json())
        .then(result => {
            alert(result.message)
            location.href = "/home/chinmay/CCV2/CCV2/UI/login.html";
        })
        .catch(error => console.log('error', error));
}