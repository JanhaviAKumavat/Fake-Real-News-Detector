/*
==================================================
   FAKE NEWS DETECTOR JAVASCRIPT
==================================================
*/


document.addEventListener(
    "DOMContentLoaded",
    function(){



        const detectorForm = document.querySelector(
            ".detector-card form"
        );



        const detectButton = document.querySelector(
            ".detect-btn"
        );





        if(detectorForm && detectButton){



            detectorForm.addEventListener(
                "submit",
                function(){



                    // Disable button

                    detectButton.disabled = true;




                    // Change button text


                    detectButton.innerHTML = `

                    <i class="fa-solid fa-spinner fa-spin"></i>

                    Analyzing News...

                    `;




                }
            );


        }



    }
);