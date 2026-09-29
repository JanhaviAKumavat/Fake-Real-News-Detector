/* =====================================================
   Fake News Detector AI
   Admin Users Management JavaScript
===================================================== */



document.addEventListener(
    "DOMContentLoaded",
    function(){





    // ==========================================
    // User Search Functionality
    // ==========================================


    const searchInput =
        document.getElementById(
            "userSearch"
        );



    const table =
        document.getElementById(
            "usersTable"
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







                let visibleRows = 0;






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

                        visibleRows++;


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
    // Delete Confirmation
    //   (builds and submits a hidden POST form
    //    once the user confirms)
    // ==========================================


    const deleteButtons =
        document.querySelectorAll(
            ".delete-btn"
        );





    deleteButtons.forEach(

        function(button){



            button.addEventListener(

                "click",

                function(event){



                    event.preventDefault();




                    let confirmDelete =
                    confirm(
                        "Are you sure you want to delete this user?"
                    );



                    if(!confirmDelete){


                        return;


                    }




                    let deleteUrl =
                        button.getAttribute(
                            "data-delete-url"
                        );



                    let form =
                        document.createElement(
                            "form"
                        );



                    form.method = "POST";

                    form.action = deleteUrl;



                    document.body.appendChild(form);


                    form.submit();



                }


            );


        }

    );









    // ==========================================
    // Button Hover Animation
    // ==========================================


    const actionButtons =
        document.querySelectorAll(
            ".action-buttons a"
        );



    actionButtons.forEach(

        function(btn){



            btn.addEventListener(

                "mouseenter",

                function(){


                    btn.style.transform =
                    "translateY(-3px)";


                }


            );





            btn.addEventListener(

                "mouseleave",

                function(){


                    btn.style.transform =
                    "translateY(0)";


                }


            );



        }

    );










    // ==========================================
    // Modal Open / Close Helpers
    // ==========================================


    function openModal(id){

        document.getElementById(id)
        .classList.add("active");

    }



    function closeModal(id){

        document.getElementById(id)
        .classList.remove("active");

    }




    document.querySelectorAll(
        "[data-close]"
    ).forEach(

        function(btn){


            btn.addEventListener(

                "click",

                function(){


                    closeModal(
                        btn.getAttribute(
                            "data-close"
                        )
                    );


                }

            );


        }

    );




    document.querySelectorAll(
        ".modal-overlay"
    ).forEach(

        function(overlay){


            overlay.addEventListener(

                "click",

                function(e){


                    if(e.target === overlay){


                        overlay.classList.remove(
                            "active"
                        );


                    }


                }

            );


        }

    );









    // ==========================================
    // Add User Button
    // ==========================================


    const openAddBtn =
        document.getElementById(
            "openAddUserBtn"
        );



    if(openAddBtn){


        openAddBtn.addEventListener(

            "click",

            function(){


                openModal(
                    "addUserModal"
                );


            }

        );


    }









    // ==========================================
    // View / Edit Buttons
    //   (read data from the row's
    //    data-* attributes)
    // ==========================================


    document.querySelectorAll(
        "#usersTable tbody tr"
    ).forEach(

        function(row){



            const id = row.dataset.id;

            const name = row.dataset.name;

            const email = row.dataset.email;

            const role = row.dataset.role;

            const created = row.dataset.created;




            const viewBtn =
                row.querySelector(
                    ".view-btn"
                );



            const editBtn =
                row.querySelector(
                    ".edit-btn"
                );






            if(viewBtn){


                viewBtn.addEventListener(

                    "click",

                    function(e){


                        e.preventDefault();



                        document.getElementById(
                            "viewName"
                        ).textContent = name;



                        document.getElementById(
                            "viewEmail"
                        ).textContent = email;



                        document.getElementById(
                            "viewRole"
                        ).textContent = role;



                        document.getElementById(
                            "viewCreated"
                        ).textContent = created;



                        openModal(
                            "viewUserModal"
                        );


                    }

                );


            }






            if(editBtn){


                editBtn.addEventListener(

                    "click",

                    function(e){


                        e.preventDefault();



                        document.getElementById(
                            "editName"
                        ).value = name;



                        document.getElementById(
                            "editEmail"
                        ).value = email;



                        document.getElementById(
                            "editRole"
                        ).value = role;




                        const form =
                            document.getElementById(
                                "editUserForm"
                            );



                        form.action =
                            `/admin/users/${id}/update`;




                        openModal(
                            "editUserModal"
                        );


                    }

                );


            }


        }

    );






});