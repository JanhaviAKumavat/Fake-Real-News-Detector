/* =====================================================
   Fake News Detector AI
   Admin Prediction Management JavaScript
===================================================== */



document.addEventListener(
    "DOMContentLoaded",
    function(){






    // ==========================================
    // Prediction Search
    // ==========================================


    const searchInput =
        document.getElementById(
            "predictionSearch"
        );



    const table =
        document.getElementById(
            "predictionTable"
        );





    if(searchInput && table){



        searchInput.addEventListener(

            "keyup",

            function(){



                let searchValue =
                    searchInput.value
                    .toLowerCase();




                let rows =
                    table
                    .getElementsByTagName(
                        "tbody"
                    )[0]
                    .getElementsByTagName(
                        "tr"
                    );





                for(
                    let i = 0;
                    i < rows.length;
                    i++
                ){



                    let rowText =
                        rows[i]
                        .innerText
                        .toLowerCase();





                    if(
                        rowText.includes(
                            searchValue
                        )
                    ){


                        rows[i].style.display =
                        "";


                    }

                    else{


                        rows[i].style.display =
                        "none";


                    }



                }



            }


        );



    }









    // ==========================================
    // View Prediction Details
    // ==========================================


    const viewButtons =
        document.querySelectorAll(
            ".view-btn"
        );




    viewButtons.forEach(

        function(button){



            button.addEventListener(

                "click",

                function(event){


                    event.preventDefault();



                    alert(
                        "Prediction details page will open here."
                    );



                }


            );



        }

    );









    // ==========================================
    // Export Report Button
    // ==========================================


    const exportButton =
        document.querySelector(
            ".admin-btn-primary"
        );





    if(exportButton){



        exportButton.addEventListener(

            "click",

            function(){



                alert(
                    "Prediction report export started."
                );



            }


        );



    }








    // ==========================================
    // Table Row Animation
    // ==========================================


    const rows =
        document.querySelectorAll(
            ".prediction-table tbody tr"
        );



    rows.forEach(

        function(row,index){



            row.style.opacity="0";


            row.style.transform=
            "translateY(10px)";





            setTimeout(

                function(){


                    row.style.transition=
                    "0.4s ease";



                    row.style.opacity="1";


                    row.style.transform=
                    "translateY(0)";



                },

                index * 80

            );



        }

    );






});