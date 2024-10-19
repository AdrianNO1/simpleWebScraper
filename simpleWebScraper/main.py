from .scraper import get_html
from .parser import parse_html

def scrape(url, target_elem, use_selenium=False, parent_elem=None, parent_index=0, target_index=0, element_properties=["id", "class"], debug=False, return_html=False):
    html, error = get_html(url, use_selenium=use_selenium, debug=debug)

    if error:
        if return_html:
            return None, error, None
        else:
            return None, error
    else:
        text, error = parse_html(html, target_elem, parent_elem=parent_elem, parent_index=parent_index, target_index=target_index, element_properties=element_properties, debug=debug)
        if return_html:
            return text, error, html
        else:
            return text, error
    
if __name__ == "__main__":
    # example usage. Gets the subscriber count of a YouTube channel using Social Blade.

    url = "https://socialblade.com/youtube/channel/UCVun3IyFIh6AsEMV11zlVHg"

    # Inspect element on the page to find the element you want to scrape the innerText of
    target_elem = '<span id="youtube-stats-header-subs" style="display: none;">908K</span>'

    # use selenium when the website you are scraping doesn't like being scraped
    data = scrape(url, target_elem, use_selenium=True, element_properties=["id"])

    if data[1]:
        print(f"Error: {data[1]}")
    else:
        print(data[0])