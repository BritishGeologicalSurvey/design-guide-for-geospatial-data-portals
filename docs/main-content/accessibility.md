# Accessibility

> Accessibility should be considered from the outset to ensure that as many people as possible can use your services. Considering accessibility addresses various user needs ensuring websites are faster, easer to use and appear higher in search engine rankings.

Although accessibility aims to provide the best possible experience for users with disabilities, it also applies to anyone who's ability may be affected by their circumstances, for example:

+ location - they could be in a noisy cafe, sunny park or area with slow wifi
+ health - they may be tired, affected by injury or medical procedure
+ equipment - mobile device or an older browser

According to the [service manual](https://www.gov.uk/service-manual/helping-people-to-use-your-service/making-your-service-accessible-an-introduction) provided by the [GDS accessibility community](https://www.gov.uk/service-manual/communities/accessibility-community): The UK government has set out accessibility standards to follow. If you fail to meet those standards, you could be breaking the law.

Their guidance states: "To meet government accessibility requirements, digital services must:

+ meet level AA of the [Web Content Accessibility Guidelines (WCAG 2.1)](https://www.gov.uk/service-manual/helping-people-to-use-your-service/understanding-wcag) as a minimum
+ work on the most commonly used [assistive technologies](https://www.gov.uk/service-manual/technology/testing-with-assistive-technologies) - including screen magnifiers, screen readers and speech recognition tools
+ include people with disabilities in [user research](https://www.gov.uk/service-manual/user-research)
+ have an accessibility statement that explains how accessible the service is - you need to publish this when the service moves into public beta

You can find out more about the regulations by reading the [latest guidance](https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps)."

### Accessibility best practice

Here is a roundup of best practice accessibility guidance to follow when considering the design of a geospatial portal:

#### Content
+ Ensure content is in a logical order so that users who tab through content can do so in an order that makes sense
+ Make sure headings and sections stand out with each section having its own heading
+ Ensure links are self-describing, independent to any surrounding text and front-loaded with the most notable keywords first
+ Ensure the order descriptions are read out are tested with screen readers
+ Text should be resizable and legible when resized

#### Images
+ Make sure any graphics, data visualisations or time-based media have captions or descriptions
+ Identify informative vs decorative images. Informative images require useful ALT text for screen readers. Decorative images need null ALT text assigned (i.e. alt=””)
+ Avoid embedding text within images

#### Keyboard access
+ Include a “skip to main content” link before the header for keyboard users
+ Check users can reach all interactive elements and trigger them with the spacebar, enter key, or arrow keys
+ Ensure all interactive elements have a visible focus state
+ Ensure all interactive elements have intentional styles for applied states: focus, hover, active, and visited

##### Forms
+ Ensure forms are in single column, have descriptive labels, avoid placeholder text and include clear error states
+ Ensure labels are assigned to each form element

#### Touch targets
+ Touch targets should be a minimum of 44px
+ On mobile: Ensure primary actions are achieved with either the left or right thumb and touch targets are at least 48px and separated by 8px.

#### Colour contrast
+ Ensure that there is sufficient contrast between colours, 4.5:1 for small text and 3:1 for large text


### Find out more
Further guidance regarding accessibility can be found at:
+ [UK Government Digital Services - Accessibility blog](https://gds.blog.gov.uk/category/accessibility/)
+ [UK Government - Making your service accessible: an introduction](https://www.gov.uk/service-manual/helping-people-to-use-your-service/making-your-service-accessible-an-introduction)
