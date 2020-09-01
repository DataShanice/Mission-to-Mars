def hemispheres(browser):
   url = "https://astrogeology.usgs.gov/search/results/?q=hemisphere+enhanced&k1=target&v1=Mars"
   browser.visitor(url)

   hemisphere_image_urls = []
# Get the list of all hemispheres 
   links = browser.find_by_css('a.product-item h3')

# Next loop through those links click the link and find 
   for index in range(len(links)):
      hemisphere = {}
    
    
    # Find the elements on each loop to avoid a state element exception 
       browser.find_by_css('a.product-item h3')[index].click()

    # Find the sample image anchor tag and extract 
       sample_element = browser.find_link_by_text("Sample").first
       hemisphere["img_url"] = sample_element["href"]
    
    # Get Title
       hemisphere["title"] = browser.find_by_css("h2.title").text
    
       hemisphere_image_urls.append(hemisphere)
    
    # Navigate backwards 
       browser.back()

   return hemisphere_image_urls

if __name__ == "__main__":

   print(scrape_all())