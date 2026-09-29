/* ==========================================
   Fake News Detector AI - Sidebar JS
========================================== */


document.addEventListener("DOMContentLoaded", function () {



    const sidebar = document.getElementById("adminSidebar");

    const toggleBtn = document.getElementById("sidebarToggle");



    /*
        Safety Check
    */


    if (!sidebar || !toggleBtn) {

        console.log("Sidebar elements not found");

        return;

    }





    /*
        Create Overlay Dynamically
    */


    const overlay = document.createElement("div");


    overlay.classList.add("sidebar-overlay");


    document.body.appendChild(overlay);








    /*
        Toggle Sidebar
    */


    toggleBtn.addEventListener("click", function () {



        sidebar.classList.toggle("active");


        overlay.classList.toggle("active");



    });








    /*
        Close Sidebar On Overlay Click
    */


    overlay.addEventListener("click", function () {



        sidebar.classList.remove("active");


        overlay.classList.remove("active");



    });









    /*
        Close Sidebar After Clicking Menu
    */


    const menuLinks = document.querySelectorAll(".menu-link");



    menuLinks.forEach(function(link){



        link.addEventListener("click", function(){



            if(window.innerWidth <= 992){



                sidebar.classList.remove("active");


                overlay.classList.remove("active");



            }



        });



    });









    /*
        Desktop Sidebar Collapse
    */


    const collapseButton = document.querySelector(".sidebar-collapse");



    if(collapseButton){



        collapseButton.addEventListener("click", function(){



            const wrapper = document.querySelector(".admin-wrapper");



            if(wrapper){



                wrapper.classList.toggle("sidebar-collapsed");



            }



            sidebar.classList.toggle("collapsed");



        });



    }






    /*
        Close Sidebar On Window Resize
    */


    window.addEventListener("resize", function(){



        if(window.innerWidth > 992){



            sidebar.classList.remove("active");


            overlay.classList.remove("active");



        }



    });




});