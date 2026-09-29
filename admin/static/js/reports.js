/* =====================================================
   Fake News Detector AI
   Admin Reports Management JavaScript
===================================================== */


document.addEventListener(
    "DOMContentLoaded",
    function(){



    /* ==========================================
       Report Search Functionality
    ========================================== */


    const searchInput =
        document.getElementById(
            "reportSearch"
        );



    const table =
        document.getElementById(
            "reportsTable"
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









    /* ==========================================
       Table Row Animation
    ========================================== */


    const rows =
        document.querySelectorAll(
            ".report-table tbody tr"
        );





    rows.forEach(

        function(row,index){



            row.style.opacity="0";


            row.style.transform=
            "translateY(20px)";





            setTimeout(



                function(){



                    row.style.transition=
                    "all 0.4s ease";



                    row.style.opacity="1";


                    row.style.transform=
                    "translateY(0)";



                },


                index * 80



            );



        }

    );









    /* ==========================================
       Confidence Tooltip
    ========================================== */


    const progressBars =
        document.querySelectorAll(
            ".progress-bar"
        );





    progressBars.forEach(

        function(bar){



            let confidence =
                bar.style.width;




            bar.parentElement
            .setAttribute(

                "title",

                "Confidence : "
                + confidence

            );




        }

    );









    /* ==========================================
       Download Button Animation
    ========================================== */


    const downloadButtons =
        document.querySelectorAll(
            ".download-btn"
        );





    downloadButtons.forEach(

        function(button){



            button.addEventListener(

                "click",

                function(){



                    button.innerHTML =
                    '<i class="fa-solid fa-spinner fa-spin"></i>';



                    setTimeout(

                        function(){


                            button.innerHTML =
                            '<i class="fa-solid fa-download"></i>';



                        },

                        1500


                    );



                }


            );



        }

    );








});