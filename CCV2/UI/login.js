// Login Function
function Login() {
    var username = document.getElementById("username").value;
    //alert("Your name is " + username);

    var password = document.getElementById("password").value;
    //alert("Your name password " + password);

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var raw = { "user_name": username, "password": password };


    // Used to fetch backend request
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: JSON.stringify(raw),
        redirect: 'follow'
    };

    fetch("http://0.0.0.0:5678/login", requestOptions)
        .then(response => response.json())
        .then(result => {

            if (result.valid === false) {
                document.getElementById("error_message").innerHTML = result.message;
            }
            else {
                window.location.replace("Home.html")
            }
        })
        .catch(error => console.log('error', error));
}

