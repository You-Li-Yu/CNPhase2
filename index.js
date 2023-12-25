const login = document.getElementById('login')
    login.addEventListener('click', ()=>{
        var username = document.getElementById("username").value
        var password = document.getElementById("password").value
        fetch('http://127.0.0.1:4000/login', {
            method: "POST",
            body: (username + ' ' + password),
        })
        .then(response => {
            console.log(response)
            return response.json
        })
        .then(data => {
            console.log("Response data:", data)
        })
    })

    register.addEventListener('click', ()=>{
        var username = document.getElementById("username").value
        var password = document.getElementById("password").value
        fetch('http://127.0.0.1:4000/register', {
            method: "POST",
            body: (username + ' ' + password),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
        })
    })    