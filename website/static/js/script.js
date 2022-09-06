// Sidebar Trigger
document.addEventListener("DOMContentLoaded", function () {
    const options = {
        "edge": "left"
    }

    var elems = document.querySelectorAll(".sidenav");
    var instances = M.Sidenav.init(elems, options);
});

function clearFilters() {
    document.getElementsByName("checkbox").forEach(element => {
        element.checked = false;
    });
}

// Materialize Select
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems);
});




// Back to login
function changeBack() {
    window.location.href = "/"
}

// Change Password
function changePass(){
    const form = document.getElementById("changeform");
    const email = document.getElementById("userEmail");
    const pswd1 = document.getElementById("userPass1");
    const pswd2 = document.getElementById("userPass2");
    
    
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        console.log("Inside eventListener");
        var success = checkInputs(email, pswd1, pswd2);
        console.log('Inputs checked!');
        if (success) {
            console.log('Success');
            fetch("/changepassword", {
                method: "POST",
                body: JSON.stringify({
                    email: email.value,
                    pass: pswd1.value
                })
            })
            .then(() => {window.location.href = window.location.href})
        }
    });
}

function checkInputs(email, pswd1, pswd2) {
    const emailValue = email.value.trim();
    const pswdValue = pswd1.value.trim();
    const pswd2Value = pswd2.value.trim();
    var success = true

    if(emailValue === '') {
        success = false;
        setErrorFor(email, 'Email cannot be blank');
    }else if(!isEmail(emailValue)) {
        success = false;
        setErrorFor(email, "Email is not valid");
    }else{
        success = true;
        setSuccessFor(email);
    }

    if(pswdValue === '') {
        success = false;
        setErrorFor(pswd1, 'Password cannot be blank');
    }else if (!(pswd2Value.length >= 6 && pswd2Value.length <= 20)) {
        success = false;
        setErrorFor(pswd1, 'Password must be 6-20 characters long');
    }else {
        success = true;
        setSuccessFor(pswd1);
    }

    if(pswd2Value === '') {
        success = false;
        setErrorFor(pswd2, 'Password cannot be blank');
    }else if (pswdValue !== pswd2Value) {
        success = false;
        setErrorFor(pswd2, 'Passwords do not match');
    }else {
        success = true;
        setSuccessFor(pswd2);
    }

    function setErrorFor(input, message) {
        const formControl = input.parentElement.parentElement;
        const small = formControl.querySelector("small");

        small.innerText = message;

        formControl.className = "input-field col s12 err";
    }

    function setSuccessFor(input) {
        const formControl = input.parentElement;
        formControl.className = "input-field col s12 success";
    }

    function isEmail(email) {
        return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
    }

    return success;
}

