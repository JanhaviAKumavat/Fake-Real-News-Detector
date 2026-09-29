/*
=====================================================
 Fake News Detector AI
 Admin Logs JavaScript
=====================================================
*/


document.addEventListener(
    "DOMContentLoaded",
    function(){



        const searchInput =
            document.getElementById(
                "logSearch"
            );



        const typeFilter =
            document.getElementById(
                "logTypeFilter"
            );



        const statusFilter =
            document.getElementById(
                "logStatusFilter"
            );



        const tableRows =
            document.querySelectorAll(
                ".logs-table tbody tr"
            );






        /*
        ===============================================
        FILTER LOG TABLE
        ===============================================
        */


        function filterLogs(){


            let searchValue =
                searchInput ?
                searchInput.value.toLowerCase()
                :
                "";



            let typeValue =
                typeFilter ?
                typeFilter.value.toLowerCase()
                :
                "";



            let statusValue =
                statusFilter ?
                statusFilter.value.toLowerCase()
                :
                "";





            tableRows.forEach(
                function(row){



                    let rowText =
                        row.textContent
                        .toLowerCase();




                    let rowType =
                        row.querySelector(
                            ".type"
                        );



                    let rowStatus =
                        row.querySelector(
                            ".status"
                        );




                    let typeText =
                        rowType ?
                        rowType.textContent
                        .toLowerCase()
                        :
                        "";




                    let statusText =
                        rowStatus ?
                        rowStatus.textContent
                        .toLowerCase()
                        :
                        "";





                    let searchMatch =
                        rowText.includes(
                            searchValue
                        );




                    let typeMatch =
                        typeValue === ""
                        ||
                        typeText.includes(
                            typeValue
                        );




                    let statusMatch =
                        statusValue === ""
                        ||
                        statusText.includes(
                            statusValue
                        );







                    if(
                        searchMatch &&
                        typeMatch &&
                        statusMatch
                    ){


                        row.style.display =
                            "";

                    }

                    else{


                        row.style.display =
                            "none";

                    }





                }
            );


        }









        /*
        ===============================================
        SEARCH EVENT
        ===============================================
        */


        if(searchInput){


            searchInput.addEventListener(

                "keyup",

                filterLogs

            );


        }







        /*
        ===============================================
        TYPE FILTER
        ===============================================
        */


        if(typeFilter){


            typeFilter.addEventListener(

                "change",

                filterLogs

            );


        }







        /*
        ===============================================
        STATUS FILTER
        ===============================================
        */


        if(statusFilter){


            statusFilter.addEventListener(

                "change",

                filterLogs

            );


        }









        /*
        ===============================================
        CLEAR LOG BUTTON
        ===============================================
        */


        const clearBtn =
            document.getElementById(
                "clearLogsBtn"
            );




        if(clearBtn){



            clearBtn.addEventListener(

                "click",

                function(){



                    let confirmDelete =
                        confirm(
                            "Are you sure you want to clear logs?"
                        );



                    if(confirmDelete){


                        alert(
                            "Logs cleared successfully."
                        );


                        /*
                        Backend API will be connected later
                        */


                    }



                }

            );


        }









        /*
        ===============================================
        EXPORT LOG BUTTON
        ===============================================
        */


        const exportBtn =
            document.getElementById(
                "exportLogsBtn"
            );





        if(exportBtn){



            exportBtn.addEventListener(

                "click",

                function(){



                    alert(
                        "Exporting logs..."
                    );



                    /*
                    Backend CSV export
                    will be connected later
                    */


                }

            );



        }






    }
);