/* =========================
   NAVIGATION ACTIVE LINK
========================= */

const sections = document.querySelectorAll("section");

const navLinks = document.querySelectorAll(".nav-link");


window.addEventListener("scroll", () => {

    let currentSection = "";

    sections.forEach(section => {

        const sectionTop = section.offsetTop - 120;

        const sectionHeight = section.clientHeight;

        if (
            window.scrollY >= sectionTop &&
            window.scrollY < sectionTop + sectionHeight
        ) {
            currentSection = section.getAttribute("id");
        }

    });


    navLinks.forEach(link => {

        link.classList.remove("active");

        if (
            link.getAttribute("href") ===
            "#" + currentSection
        ) {
            link.classList.add("active");
        }

    });

});


/* =========================
   PAGE LOAD
========================= */

window.addEventListener("load", () => {

    console.log(
        "Riaz Ahamed Portfolio Loaded Successfully"
    );

});


/* =========================
   CONTACT FORM BUTTON
========================= */

const contactForm =
    document.querySelector(".contact-form");


if (contactForm) {

    contactForm.addEventListener("submit", () => {

        const button =
            contactForm.querySelector("button");

        button.textContent =
            "Sending...";

        button.style.opacity = "0.7";

    });

}