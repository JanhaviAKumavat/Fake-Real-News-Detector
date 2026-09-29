// // ==============================
// // Scroll to Top Button
// // ==============================

// const scrollBtn = document.getElementById("scrollTopBtn");

// if (scrollBtn) {

//     window.addEventListener("scroll", function () {

//         if (window.scrollY > 300) {

//             scrollBtn.style.display = "block";

//         } else {

//             scrollBtn.style.display = "none";

//         }

//     });

//     scrollBtn.addEventListener("click", function () {

//         window.scrollTo({

//             top: 0,

//             behavior: "smooth"

//         });

//     });

// }


// // ==============================
// // Auto Hide Flash Messages
// // ==============================

// const alerts = document.querySelectorAll(".alert");

// alerts.forEach(function (alert) {

//     setTimeout(function () {

//         alert.style.transition = "0.5s";

//         alert.style.opacity = "0";

//         setTimeout(function () {

//             alert.remove();

//         }, 500);

//     }, 3000);

// });


// // ==============================
// // Smooth Scroll
// // ==============================

// document.querySelectorAll('a[href^="#"]').forEach(function(anchor){

//     anchor.addEventListener("click", function(e){

//         e.preventDefault();

//         const target = document.querySelector(this.getAttribute("href"));

//         if(target){

//             target.scrollIntoView({

//                 behavior:"smooth"

//             });

//         }

//     });

// });


// // ==============================
// // Current Year in Footer
// // ==============================

// const year = document.getElementById("currentYear");

// if(year){

//     year.innerHTML = new Date().getFullYear();

// }


// // ==============================
// // Disable Empty Forms
// // ==============================

// document.querySelectorAll("form").forEach(function(form){

//     form.addEventListener("submit", function(e){

//         let valid = true;

//         const requiredFields = form.querySelectorAll("[required]");

//         requiredFields.forEach(function(field){

//             if(field.value.trim() === ""){

//                 valid = false;

//                 field.classList.add("is-invalid");

//             }else{

//                 field.classList.remove("is-invalid");

//             }

//         });

//         if(!valid){

//             e.preventDefault();

//         }

//     });

// });


// // ==============================
// // Remove Validation Border
// // ==============================

// document.querySelectorAll("input, textarea").forEach(function(input){

//     input.addEventListener("input", function(){

//         this.classList.remove("is-invalid");

//     });

// });


// // ==============================
// // Button Loading Effect
// // ==============================

// document.querySelectorAll(".loading-btn").forEach(function(button){

//     button.addEventListener("click", function(){

//         button.disabled = true;

//         button.innerHTML =

//         '<span class="spinner-border spinner-border-sm"></span> Please Wait...';

//     });

// });


// // ==============================
// // Console Message
// // ==============================

// console.log("FakeDetect AI Loaded Successfully");


// ==========================================
// MAIN JAVASCRIPT
// Fake News Detector AI
// ==========================================



document.addEventListener(
    "DOMContentLoaded",
    function(){





// ==========================================
// AUTO HIDE FLASH MESSAGES
// ==========================================


const alerts = document.querySelectorAll(
    ".alert"
);



alerts.forEach(
    function(alert){


        setTimeout(
            function(){


                alert.style.transition =
                "0.5s";


                alert.style.opacity =
                "0";


                setTimeout(
                    function(){

                        alert.remove();

                    },
                    500
                );


            },
            4000
        );


    }
);









// ==========================================
// PASSWORD SHOW / HIDE
// ==========================================


const passwordFields =
document.querySelectorAll(
    "input[type='password']"
);



passwordFields.forEach(
    function(field){


        const button =
        field.parentElement.querySelector(
            ".password-toggle"
        );



        if(button){


            button.addEventListener(
                "click",
                function(){


                    if(
                        field.type === "password"
                    ){

                        field.type =
                        "text";


                        button.innerHTML =
                        '<i class="fa-solid fa-eye-slash"></i>';

                    }


                    else{


                        field.type =
                        "password";


                        button.innerHTML =
                        '<i class="fa-solid fa-eye"></i>';

                    }



                }
            );


        }



    }
);









// ==========================================
// DETECTOR LOADING BUTTON
// ==========================================


const detectorForm =
document.querySelector(
    "#detectorForm"
);



if(detectorForm){


    detectorForm.addEventListener(
        "submit",
        function(){


            const button =
            detectorForm.querySelector(
                "button[type='submit']"
            );



            if(button){


                button.disabled =
                true;



                button.innerHTML =
                `
                <span class="spinner-border spinner-border-sm"></span>
                Analyzing...
                `;


            }



        }
    );


}









// ==========================================
// SMOOTH SCROLL
// ==========================================


const links =
document.querySelectorAll(
    "a[href^='#']"
);



links.forEach(
    function(link){


        link.addEventListener(
            "click",
            function(e){


                const target =
                document.querySelector(
                    this.getAttribute("href")
                );


                if(target){


                    e.preventDefault();


                    target.scrollIntoView({

                        behavior:"smooth"

                    });


                }


            }
        );


    }
);









// ==========================================
// LOGOUT CONFIRMATION
// ==========================================


const logoutLinks =
document.querySelectorAll(
    ".logout-link"
);



logoutLinks.forEach(
    function(link){


        link.addEventListener(
            "click",
            function(e){


                let confirmLogout =
                confirm(
                    "Are you sure you want to logout?"
                );



                if(!confirmLogout){

                    e.preventDefault();

                }



            }
        );



    }
);






});