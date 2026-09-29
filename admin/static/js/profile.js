/* =====================================================
   Fake News Detector AI
   Admin Profile JavaScript
===================================================== */



document.addEventListener(

    "DOMContentLoaded",

    function(){





    // ==========================================
    // Modal Open / Close Helpers
    // ==========================================


    function openModal(id){

        document.getElementById(id)
        .classList.add("active");

    }



    function closeModal(id){

        document.getElementById(id)
        .classList.remove("active");

    }




    document.querySelectorAll(
        "[data-close]"
    ).forEach(

        function(btn){


            btn.addEventListener(

                "click",

                function(){


                    closeModal(
                        btn.getAttribute(
                            "data-close"
                        )
                    );


                }

            );


        }

    );




    document.querySelectorAll(
        ".modal-overlay"
    ).forEach(

        function(overlay){


            overlay.addEventListener(

                "click",

                function(e){


                    if(e.target === overlay){


                        overlay.classList.remove(
                            "active"
                        );


                    }


                }

            );


        }

    );








    // ==========================================
    // Edit Profile Button
    // ==========================================


    const editButton =
        document.getElementById(
            "openEditProfileBtn"
        );





    if(editButton){



        editButton.addEventListener(

            "click",

            function(){



                openModal(
                    "editProfileModal"
                );



            }


        );


    }









    // ==========================================
    // Change Password Button
    // ==========================================


    const passwordButton =
        document.getElementById(
            "openChangePasswordBtn"
        );






    if(passwordButton){



        passwordButton.addEventListener(

            "click",

            function(){



                openModal(
                    "changePasswordModal"
                );



            }


        );


    }









    // ==========================================
    // Two Factor Authentication Toggle
    //   (cosmetic only — no backend wired
    //    up for this yet)
    // ==========================================


    const twoFactorToggle =
        document.querySelector(
            ".switch input"
        );







    if(twoFactorToggle){



        twoFactorToggle.addEventListener(

            "change",

            function(){



                if(this.checked){



                    showProfileNotification(

                        "Two Factor Authentication Enabled"

                    );


                }

                else{


                    showProfileNotification(

                        "Two Factor Authentication Disabled",

                        "warning"

                    );


                }



            }


        );



    }









    // ==========================================
    // Profile Card Animation
    // ==========================================



    const cards =
        document.querySelectorAll(
            ".profile-card"
        );






    cards.forEach(

        function(card,index){



            card.style.opacity =
            "0";



            card.style.transform =
            "translateY(20px)";





            setTimeout(

                function(){



                    card.style.transition =
                    "0.5s ease";



                    card.style.opacity =
                    "1";



                    card.style.transform =
                    "translateY(0)";



                },

                index * 150


            );



        }


    );









});









// ==========================================
// Notification Function
// ==========================================


function showProfileNotification(

    message,

    type="success"

){



    const notification =
        document.createElement(
            "div"
        );






    notification.className =
        "profile-notification " + type;






    notification.innerHTML = `

        <i class="fa-solid fa-circle-check"></i>

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