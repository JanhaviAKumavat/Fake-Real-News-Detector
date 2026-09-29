/* =====================================================
   Fake News Detector AI
   Admin Analytics Dashboard JavaScript
===================================================== */



document.addEventListener(
    "DOMContentLoaded",
    function(){







    // ==========================================
    // Fake vs Real News Chart
    //   (reads real counts from data attributes
    //    instead of hardcoded numbers)
    // ==========================================



    const newsChart =
        document.getElementById(
            "newsResultChart"
        );




    if(newsChart){



        const fakeCount =
            Number(
                newsChart.dataset.fake
            ) || 0;



        const realCount =
            Number(
                newsChart.dataset.real
            ) || 0;




        new Chart(

            newsChart,

            {


                type:"doughnut",



                data:{


                    labels:[

                        "Fake News",

                        "Real News"

                    ],



                    datasets:[

                        {

                            data:[

                                fakeCount,

                                realCount

                            ],



                            borderWidth:1


                        }

                    ]



                },



                options:{


                    responsive:true,


                    plugins:{


                        legend:{


                            position:"bottom"


                        }



                    }


                }



            }


        );


    }









    // ==========================================
    // Daily Prediction Chart
    //   (reads real last-7-days data from
    //    data attributes instead of hardcoded
    //    week numbers)
    // ==========================================



    const dailyChart =
        document.getElementById(
            "dailyPredictionChart"
        );






    if(dailyChart){



        let labels = [];

        let counts = [];



        try{


            labels = JSON.parse(
                dailyChart.dataset.labels || "[]"
            );



            counts = JSON.parse(
                dailyChart.dataset.counts || "[]"
            );


        }

        catch(e){


            console.error(
                "Could not parse daily chart data:",
                e
            );


        }




        new Chart(

            dailyChart,

            {



                type:"line",




                data:{



                    labels:labels,





                    datasets:[


                        {


                            label:
                            "Predictions",




                            data:counts,




                            borderWidth:2,




                            tension:0.4



                        }



                    ]



                },




                options:{



                    responsive:true,



                    plugins:{


                        legend:{


                            position:"top"


                        }



                    },



                    scales:{


                        y:{


                            beginAtZero:true


                        }



                    }



                }




            }



        );


    }









    // ==========================================
    // Animate Performance Bars
    // ==========================================



    const performanceBars =
        document.querySelectorAll(
            ".performance-bar"
        );






    performanceBars.forEach(

        function(bar){



            let width =
                bar.style.width;



            bar.style.width =
                "0%";





            setTimeout(


                function(){


                    bar.style.transition =
                    "1s ease";



                    bar.style.width =
                    width;



                },


                300



            );



        }


    );







});