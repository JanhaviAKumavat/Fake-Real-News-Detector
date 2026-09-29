// ======================================
// FakeDetect AI - Navbar JavaScript
// ======================================


// ======================================
// Change Navbar on Scroll
// ======================================

const navbar = document.querySelector(".custom-navbar");

window.addEventListener("scroll", function () {

    if (!navbar) return;

    if (window.scrollY > 50) {

        navbar.style.background = "#0d6efd";

        navbar.style.boxShadow = "0 4px 15px rgba(0,0,0,0.15)";

        navbar.style.padding = "10px 0";

    } else {

        navbar.style.background = "rgba(13,110,253,0.95)";

        navbar.style.boxShadow = "none";

        navbar.style.padding = "12px 0";

    }

});


// ======================================
// Active Navigation Link
// ======================================

const currentPage = window.location.pathname.split("/").pop();

const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

navLinks.forEach(function(link){

    const href = link.getAttribute("href");

    if(href === currentPage){

        link.classList.add("active");

    }

});


// ======================================
// Close Mobile Navbar After Click
// ======================================

const navbarCollapse = document.querySelector(".navbar-collapse");

const navItems = document.querySelectorAll(".navbar-nav .nav-link");

navItems.forEach(function(item){

    item.addEventListener("click", function(){

        if(window.innerWidth < 992){

            if(navbarCollapse){

                navbarCollapse.classList.remove("show");

            }

        }

    });

});


// ======================================
// Highlight Current Page
// ======================================

document.addEventListener("DOMContentLoaded", function(){

    const page = location.pathname.split("/").pop();

    navItems.forEach(function(item){

        const href = item.getAttribute("href");

        if(href === page){

            item.style.color = "#ffd43b";

            item.style.fontWeight = "600";

        }

    });

});


// ======================================
// Navbar Brand Animation
// ======================================

const logo = document.querySelector(".logo-text");

if(logo){

    logo.addEventListener("mouseenter", function(){

        logo.style.transform = "scale(1.05)";

        logo.style.transition = "0.3s";

    });

    logo.addEventListener("mouseleave", function(){

        logo.style.transform = "scale(1)";

    });

}


// ======================================
// Console Message
// ======================================

console.log("Navbar JS Loaded Successfully");