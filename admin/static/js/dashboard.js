/* =====================================================
   Fake News Detector AI
   Admin Dashboard JavaScript
===================================================== */



document.addEventListener(
    "DOMContentLoaded",
    function(){



    // ==========================================
    // Prediction Analytics Chart
    // ==========================================


    const chartElement =
        document.getElementById(
            "predictionChart"
        );




    if(chartElement){



        const fakeCount =
            Number(
                chartElement.dataset.fake
            ) || 0;



        const realCount =
            Number(
                chartElement.dataset.real
            ) || 0;





        new Chart(
            chartElement,
            {


            type:"doughnut",


            data:{


                labels:[

                    "Fake News",

                    "Real News"

                ],



                datasets:[{


                    label:
                    "News Detection",



                    data:[

                        fakeCount,

                        realCount

                    ],



                    borderWidth:2


                }]


            },



            options:{


                responsive:true,


                plugins:{


                    legend:{


                        position:"bottom"


                    }


                }


            }



        });



    }









    // ==========================================
    // Dashboard Card Animation
    // ==========================================


    const cards =
        document.querySelectorAll(
            ".dashboard-card"
        );



    cards.forEach(
        function(card,index){


            card.style.opacity="0";


            card.style.transform=
            "translateY(20px)";



            setTimeout(
                function(){


                    card.style.transition=
                    "0.5s ease";



                    card.style.opacity="1";


                    card.style.transform=
                    "translateY(0)";



                },

                index * 120

            );



        }

    );








    // ==========================================
    // Auto Refresh Notification
    // ==========================================


    const notification =
        document.querySelector(
            ".notification-count"
        );



    if(notification){



        notification.classList.add(
            "pulse"
        );


    }






});