/*
=====================================================
 Fake News Detector AI
 Admin Error 404 JavaScript
=====================================================
*/


document.addEventListener(
    "DOMContentLoaded",
    function(){






        /*
        ===============================================
        Error Card Animation
        ===============================================
        */


        const errorCard =
            document.querySelector(
                ".error-card"
            );



        if(errorCard){


            errorCard.style.opacity = "0";


            errorCard.style.transform =
                "translateY(30px)";




            setTimeout(

                function(){


                    errorCard.style.transition =
                    "all .6s ease";



                    errorCard.style.opacity =
                    "1";



                    errorCard.style.transform =
                    "translateY(0)";



                },

                100

            );


        }









        /*
        ===============================================
        Button Click Loading Effect
        ===============================================
        */


        const buttons =
            document.querySelectorAll(
                ".error-btn"
            );





        buttons.forEach(

            function(button){



                button.addEventListener(

                    "click",

                    function(){



                        this.style.opacity =
                        "0.7";



                    }

                );



            }

        );









        /*
        ===============================================
        Console Debug
        ===============================================
        */


        console.log(
            "Admin 404 page loaded successfully"
        );






    }
);