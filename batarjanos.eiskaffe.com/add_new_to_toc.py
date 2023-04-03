import os
from bs4 import BeautifulSoup

# Get the link, name, and category from the user
link = input("Enter the link (href): ")
name = input("Enter the name (text): ")
category = input("Enter the category: ")

# link = "/vers/indeasdx.html"
# name = "teszt"
# category = "versifikator"

# Loop through all HTML files in the current directory
# for filename in os.listdir("."):
for filename in ["index.html"]:
    if filename.endswith(".html"):
        # Load the HTML file and parse it with BeautifulSoup
        with open(filename, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        # Loop through all links on the page
        for a in soup.find_all("a"):
            # Check if the link already exists
            if a.get("href") == link and a.text.strip() == name:
                print("This link already exists.")
                break

        else: # else of for loop
            # Find the table of contents
            toc = soup.find("ul", {"id": "toc"})
            if not toc:
                print("Table of contents not found in {}.".format(filename))
                continue

            # Find the category in the table of contents
            category_li = toc.find("li", {"id": f"jegyzek-{category}"})
            if not category_li:
                # If the category doesn't exist, create it
                category_li = soup.new_tag("li")
                category_li.append(category)
                category_li["id"] = f"jegyzek-{category}"
                category_li.string = category
                toc.append(category_li)

            # Find the list of elements in the category
            elements_ul = category_li.find("ul")
            if not elements_ul:
                # If the list doesn't exist, create it
                elements_ul = soup.new_tag("ul")
                category_li.append(elements_ul)

            # Add the new element to the list
            new_element_li = soup.new_tag("li")
            new_element_a = soup.new_tag("a", href=link)
            new_element_a.string = name
            new_element_li.append(new_element_a)
            elements_ul.append(new_element_li)

        # Write the modified HTML back to the file
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(soup))
