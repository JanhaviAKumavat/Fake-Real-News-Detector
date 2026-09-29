/*
=====================================================
 Fake News Detector AI
 Admin Activity JavaScript
=====================================================
*/


document.addEventListener(
    "DOMContentLoaded",
    function(){






        /*
        ===============================================
        Activity Filter
        ===============================================
        */


        const filter =
            document.getElementById(
                "activityFilter"
            );



        const activities =
            document.querySelectorAll(
                ".timeline-item"
            );







        if(filter){



            filter.addEventListener(

                "change",

                function(){



                    let selected =
                        this.value
                        .toLowerCase();





                    activities.forEach(

                        function(item){



                            let type =
                                item
                                .querySelector(
                                    ".timeline-icon i"
                                );



                            let content =
                                item.textContent
                                .toLowerCase();





                            if(
                                selected === ""
                                ||
                                content.includes(
                                    selected
                                )
                            ){


                                item.style.display =
                                    "flex";


                            }

                            else{


                                item.style.display =
                                    "none";


                            }





                        }

                    );




                }

            );


        }









        /*
        ===============================================
        Refresh Activity Button
        ===============================================
        */


        const refreshBtn =
            document.getElementById(
                "refreshActivityBtn"
            );





        if(refreshBtn){



            refreshBtn.addEventListener(

                "click",

                function(){



                    refreshBtn.innerHTML = `

                    <i class="fa-solid fa-spinner fa-spin"></i>

                    Loading...

                    `;




                    setTimeout(

                        function(){


                            location.reload();


                        },

                        800

                    );



                }

            );



        }









        /*
        ===============================================
        Timeline Animation
        ===============================================
        */


        const timelineItems =
            document.querySelectorAll(
                ".timeline-item"
            );





        timelineItems.forEach(

            function(item,index){



                item.style.opacity="0";


                item.style.transform =
                    "translateY(20px)";



                setTimeout(

                    function(){


                        item.style.transition =
                        "all .5s ease";



                        item.style.opacity="1";


                        item.style.transform =
                        "translateY(0)";



                    },

                    index * 120

                );



            }

        );








});
