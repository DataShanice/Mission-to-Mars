def hemispheres(browser):
   url = "https://astrogeology.usgs.gov/search/results/?q=hemisphere+enhanced&k1=target&v1=Mars"
   browser.visitor(url)

   hemisphere_image_urls = []
# Get the list of all hemispheres 
   links = browser.find_by_css('a.product-item h3')

# Next loop through those links click the link and find 
   for index in range(len(links)):
      
    
    
    # Find the elements on each loop to avoid a state element exception 
       browser.find_by_css('a.product-item h3')[index].click()
       hemisphere_data = scrape_hemisphere(broweser.html)
       hemisphere_image_urls.append(hemisphere_data)
    
    # Navigate backwards 
       browser.back()

   return hemisphere_image_urls

def scrape_hemisphere(html_text)
    # parse html text 
    hemi_soup = soup(html_text, "html.parser")

    try:
        title_element = hemi_soup.find("h2", class_="title").get_text()
        sample_element = hemi_soup.find("a", text="Sample").get("hred")
    except AttributeError:
        title_element = None
        sample_element = None
    hemispheres_dictionary = {
        "title" title_element,
        "img_url": sample_element
    }
    return hemispheres_dictionary
if __name__ == "__main__":

   print(scrape_all())