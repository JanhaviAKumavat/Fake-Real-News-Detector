/* =====================================================
   Fake News Detector AI
   Admin Settings JavaScript
===================================================== */



document.addEventListener(

    "DOMContentLoaded",

    function(){





    // ==========================================
    // Save Settings Button
    // ==========================================


    const saveButton =
        document.querySelector(
            ".admin-btn-primary"
        );





    if(saveButton){



        saveButton.addEventListener(

            "click",

            function(){



                showNotification(

                    "Settings saved successfully"

                );



            }


        );



    }









    // ==========================================
    // Password Validation
    // ==========================================



    const passwordInputs =
        document.querySelectorAll(
            'input[type="password"]'
        );





    if(passwordInputs.length >= 3){



        const currentPassword =
            passwordInputs[0];



        const newPassword =
            passwordInputs[1];



        const confirmPassword =
            passwordInputs[2];






        saveButton.addEventListener(

            "click",

            function(event){



                if(
                    newPassword.value !==
                    confirmPassword.value
                ){



                    event.preventDefault();



                    showNotification(

                        "New password and confirm password do not match",

                        "error"

                    );


                }



            }



        );



    }









    // ==========================================
    // Toggle Switch Events
    // ==========================================


    const switches =
        document.querySelectorAll(
            ".switch input"
        );






    switches.forEach(

        function(toggle){



            toggle.addEventListener(

                "change",

                function(){



                    if(toggle.checked){



                        console.log(
                            "Setting enabled"
                        );



                    }

                    else{



                        console.log(
                            "Setting disabled"
                        );


                    }



                }


            );



        }

    );









    // ==========================================
    // Form Change Detection
    // ==========================================


    const inputs =
        document.querySelectorAll(
            ".form-control"
        );






    inputs.forEach(

        function(input){



            input.addEventListener(

                "input",

                function(){



                    saveButton.classList.add(
                        "active"
                    );



                }


            );


        }


    );









});









// ==========================================
// Notification Function
// ==========================================


function showNotification(

    message,

    type="success"

){



    const notification =
        document.createElement(
            "div"
        );




    notification.className =
        "settings-notification " + type;




    notification.innerHTML = `

        <i class="fa-solid fa-check"></i>

        ${message}

    `;






    document.body.appendChild(
        notification
    );







    setTimeout(

        function(){


            notification.remove();



        },

        3000


    );



}