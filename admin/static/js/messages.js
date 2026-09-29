/* =====================================================
   Fake News Detector AI
   Admin Contact Messages JavaScript
===================================================== */



document.addEventListener(
    "DOMContentLoaded",
    function(){






    // ==========================================
    // Message Search
    // ==========================================


    const searchInput =
        document.getElementById(
            "messageSearch"
        );



    const table =
        document.getElementById(
            "messagesTable"
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
    // Delete Message
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
                        "Are you sure you want to delete this message?"
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
    // Helper: update a row's status badge
    //   without a full page reload
    // ==========================================


    function updateRowStatus(row, newStatus){


        row.dataset.status = newStatus;



        let badge =
            row.querySelector(
                ".status-badge"
            );



        if(badge){


            badge.textContent = newStatus;


            badge.className =
                "status-badge status-" +
                newStatus.toLowerCase();


        }


    }









    // ==========================================
    // View Message Button
    // ==========================================


    document.querySelectorAll(
        ".view-btn"
    ).forEach(

        function(button){



            button.addEventListener(

                "click",

                function(event){



                    event.preventDefault();



                    const row =
                        button.closest("tr");



                    const id = row.dataset.id;

                    const name = row.dataset.name;

                    const email = row.dataset.email;

                    const subject = row.dataset.subject;

                    const message = row.dataset.message;

                    const created = row.dataset.created;




                    document.getElementById(
                        "viewName"
                    ).textContent = name;



                    document.getElementById(
                        "viewEmail"
                    ).textContent = email;



                    document.getElementById(
                        "viewSubject"
                    ).textContent =
                        subject || "(no subject)";



                    document.getElementById(
                        "viewCreated"
                    ).textContent = created;



                    document.getElementById(
                        "viewFullMessage"
                    ).textContent = message;




                    const replyLink =
                        document.getElementById(
                            "viewReplyBtn"
                        );



                    replyLink.href =
                        buildMailto(
                            email,
                            subject,
                            message
                        );



                    replyLink.setAttribute(

                        "data-message-id",

                        id

                    );




                    openModal(
                        "viewMessageModal"
                    );




                    // Mark as read on the server
                    // (fire and forget)


                    if(row.dataset.status === "New"){


                        fetch(

                            `/admin/messages/${id}/mark-read`,

                            { method:"POST" }

                        );



                        updateRowStatus(row, "Read");


                    }



                }


            );


        }

    );









    // ==========================================
    // Reply Button (row icon)
    // ==========================================


    document.querySelectorAll(
        ".reply-btn"
    ).forEach(

        function(button){



            button.addEventListener(

                "click",

                function(event){



                    event.preventDefault();



                    const row =
                        button.closest("tr");



                    const id = row.dataset.id;

                    const email = row.dataset.email;

                    const subject = row.dataset.subject;

                    const message = row.dataset.message;




                    window.location.href =
                        buildMailto(

                            email,

                            subject,

                            message

                        );




                    fetch(

                        `/admin/messages/${id}/mark-replied`,

                        { method:"POST" }

                    );



                    updateRowStatus(row, "Replied");



                }


            );


        }

    );









    // ==========================================
    // Reply Button (inside modal)
    // ==========================================


    const modalReplyBtn =
        document.getElementById(
            "viewReplyBtn"
        );



    if(modalReplyBtn){



        modalReplyBtn.addEventListener(

            "click",

            function(){



                const id =
                    modalReplyBtn.getAttribute(
                        "data-message-id"
                    );



                if(!id) return;




                fetch(

                    `/admin/messages/${id}/mark-replied`,

                    { method:"POST" }

                );




                const row =
                    document.querySelector(

                        `tr[data-id="${id}"]`

                    );



                if(row){


                    updateRowStatus(row, "Replied");


                }



            }


        );


    }




    // ==========================================
    // Summary Card Filtering
    // ==========================================


    const filterCards =
        document.querySelectorAll(
            ".message-card.clickable"
        );



    const messagesTable =
        document.getElementById(
            "messagesTable"
        );




    function applyFilter(filterValue){



        if(!messagesTable) return;



        const rows =
            messagesTable
            .getElementsByTagName("tbody")[0]
            .getElementsByTagName("tr");




        for(let i = 0; i < rows.length; i++){



            const row = rows[i];

            const status =
                (row.dataset.status || "")
                .toLowerCase();




            let show = true;




            if(filterValue === "new"){


                show = (status === "new");


            }

            else if(filterValue === "pending"){


                show = (status !== "replied");


            }

            // "all" -> show stays true




            row.style.display =
                show ? "" : "none";


        }




        // Highlight the active card


        filterCards.forEach(function(card){


            card.classList.toggle(

                "active-filter",

                card.dataset.filter === filterValue

            );


        });




        // Clear the search box so it doesn't

        // fight with the card filter


        const searchBox =
            document.getElementById(
                "messageSearch"
            );



        if(searchBox){

            searchBox.value = "";

        }


    }




    filterCards.forEach(function(card){



        card.addEventListener(

            "click",

            function(){



                applyFilter(

                    card.getAttribute(
                        "data-filter"
                    )

                );



            }


        );


    });





    // ==========================================
    // Build a mailto: link
    // ==========================================


    function buildMailto(email, subject, originalMessage){


        const replySubject =
            encodeURIComponent(

                "Re: " + (subject || "Your message")

            );



        const quoted =
            (originalMessage || "")
            .split("\n")
            .map(function(line){ return "> " + line; })
            .join("\n");



        const body =
            encodeURIComponent(

                "\n\n\n---\nOriginal message:\n" + quoted

            );



        return `mailto:${email}?subject=${replySubject}&body=${body}`;


    }









    // ==========================================
    // Table Animation
    // ==========================================


    const rows =
        document.querySelectorAll(
            ".messages-table tbody tr"
        );





    rows.forEach(

        function(row,index){



            row.style.opacity="0";


            row.style.transform=
            "translateY(15px)";





            setTimeout(

                function(){



                    row.style.transition =
                    "0.4s ease";



                    row.style.opacity="1";


                    row.style.transform =
                    "translateY(0)";



                },

                index * 80


            );



        }

    );






});