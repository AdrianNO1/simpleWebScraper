from bs4 import BeautifulSoup

def parse_html(html_string, target_elem, parent_elem=None, parent_index=0, target_index=0, element_properties=["id", "class"], debug=False):
    """
    Parses the given HTML string and returns the innerText of the target element.

    Parameters:
    - html_string (str): The HTML content to parse.
    - target_elem (str): The HTML fragment representing the target element.
    - parent_elem (str, optional): The HTML fragment representing the parent element. Defaults to None.
    - parent_index (int, optional): The index of the parent element if multiple exist. Defaults to 0.
    - target_index (int, optional): The index of the target element if multiple exist. Defaults to 0.
    - element_properties (list, optional): List of element properties to match (e.g., ["id", "class"]). Defaults to ["id", "class"].

    Returns:
    - str: The innerText of the target element, or None if not found.
    """
    soup = BeautifulSoup(html_string, 'html.parser')

    def parse_element(element_string):
        """Parses an HTML fragment and extracts tag name and specified attributes."""
        element_soup = BeautifulSoup(element_string, 'html.parser')
        tag = element_soup.contents[0]
        tag_name = tag.name
        attributes = {}
        for prop in element_properties:
            if prop in tag.attrs:
                attributes[prop] = tag.attrs[prop]
        
        return tag_name, attributes

    def find_element(soup_element, tag_name, attributes, index):
        """Finds an element in the soup matching the tag name and attributes at the specified index."""
        elements = soup_element.find_all(tag_name, attrs=attributes)
        if len(elements) > index:
            return elements[index]
        else:
            return None

    # Parse the target element
    target_tag_name, target_attributes = parse_element(target_elem)

    # If parent_elem is specified, find the parent element first
    if parent_elem:
        parent_tag_name, parent_attributes = parse_element(parent_elem)
        parent_element = find_element(soup, parent_tag_name, parent_attributes, parent_index)
        if not parent_element:
            return (None, "Parent element not found")  # Parent element not found
    else:
        parent_element = soup

    # Find the target element within the parent element
    target_element = find_element(parent_element, target_tag_name, target_attributes, target_index)
    if target_element:
        return (target_element.get_text(), None)
    else:
        return (None, "Target element not found")  # Target element not found

if __name__ == "__main__":
    with open("output.html", "r", encoding="utf-8") as file:
        html = file.read()

    target_elem = """<span style="font-weight: bold;">908K</span>"""

    print(parse_html(html, target_elem, element_properties=["id", "class", "style"], target_index=1))