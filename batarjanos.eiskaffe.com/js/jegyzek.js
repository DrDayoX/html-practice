// Get the current page URL
const currentPageUrl = window.location.href;

// Get all page links
const pageLinks = document.querySelectorAll(".page-link");

// Loop through each page link
pageLinks.forEach((link) => {
  // Check if the link points to the current page
  if (link.href === currentPageUrl) {

    link.style.fontWeight = "bold";
    link.style.color = "black";

    // Make the link unclickable
    link.onmouseover = () => {
      link.style.textDecoration = "none";
      link.style.cursor = "default"
    };

    link.onclick = (event) => {
      event.preventDefault();
    };
  }
});
