class element_has_css_class(object):
  def __init__(self, locator, css_class):
    self.locator = locator
    self.css_class = css_class

  def __call__(self, driver):
    element = driver.find_element(*self.locator)
    if self.css_class in element.get_attribute("class"):
        return element
    else:
        return False