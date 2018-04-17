+++
title = "Models and Control Strategies for Data Center Energy Efficiency"

# Date first published.
date = "2012-02-01"

# Authors. Comma separated list, e.g. `["Bob Smith", "David Jones"]`.
authors = ["Luca Parolini"]

# Publication type.
# Legend:
# 0 = Uncategorized
# 1 = Conference proceedings
# 2 = Journal
# 3 = Work in progress
# 4 = Technical report
# 5 = Book
# 6 = Book chapter
publication_types = ["0"]

# Publication name and optional abbreviated version.
publication = "Dissertation"
publication_short = ""

# Abstract and optional shortened version.
abstract = "As the foundation of the nation’s information infrastructure, data centers have been grow- ing rapidly in both number and capacity to meet the increasing demands for highly- responsive computing and massive storage. Data center energy consumption doubled from 2000 to 2006, reaching a value of 60 TWh/year (Tera Watt hour / year). Coupled with increasing power and cooling demands imposed by the Moore’s law and with the quest for high density data centers, this trend has been rapidly raising the energy cost associated with data centers. Data centers are large cyber-physical systems (CPSs) with hundreds of variables that can be measured and controlled. Dynamics of the controlled processes span multiple time scales: electricity costs can fluctuate hourly, temperatures evolve in the order of minutes, and CPU power states can be changed as frequent as milliseconds. Processes also differ in the spatial areas they influence: computer room air conditioners (CRAC) affect the inlet air temperatures of multiple servers, whereas CPU power states affect only single servers. The large number of constraints and their heterogeneity in nature make data center control a challenging research problem.\n This dissertation considers data centers as CPSs, with a focus on run-time management and operating costs. The proposed modeling framework explicitly captures the cyber- physical nature of data centers and allows the development of models that represent both the computational and the thermal characteristics of a data center, as well as their interactions. The proposed control strategy attempts to manage both the computational and the thermal characteristics of a data center. The control strategy is based on a hierarchical/distributed control architecture that takes advantage of the modularity typically found in data centers. The hierarchy constitutes of three control levels. The lower levels of the hierarchy deal with fast dynamic processes, while the higher levels deal with the bulk thermal management and the coordination of the controllers at the lower levels. The focus of this dissertation is on controllers at the highest level of the hierarchy, which we call data center level. Three controllers are proposed for the data center level. Each controller takes advantage of the thermal-computational model in a different way. The performances of the controllers are compared in simulation under a variety of scenarios.\n In the dissertation, it is shown that every data center has operating regimes for which simple control strategies can be as optimal as advanced ones that consider current and future, i.e., estimated, evolutions of the data center. The dissertation also discusses the existence of data center cases for which simple control strategies are always as optimal as advanced ones, regardless of the operating regime. An index, called the cyber-physical index (CPI) is proposed to provide a priori estimates of the savings that can be gained when using advanced control strategies that consider the coupling between the computational and the thermal characteristics of a data center, rather than simpler control strategies that do not account for this coupling. A possible interaction between data centers and the power-grid is also discussed. The interaction with the power-grid is designed so that data center controllers can take advantage of a time-varying electricity price. Finally, some results about the interactions between the controllers at the lower levels of the hierarchy and the controller at the data center level are discussed."
abstract_short = ""

# Featured image thumbnail (optional)
image_preview = ""

# Is this a selected publication? (true/false)
selected = true

# Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter the filename (excluding '.md') of your project file in `content/project/`.
#   E.g. `projects = ["deep-learning"]` references `content/project/deep-learning.md`.
projects = []

# Links (optional).
url_pdf = "http://www.pdl.cs.cmu.edu/research/publications/2012/CMU-ECE-2012-010.pdf"
url_preprint = "/pdf/Defense-2012-010.pdf"
url_code = ""
url_dataset = ""
url_project = ""
url_slides = "/pdf/defense_slides_all.pdf"
url_video = ""
url_poster = ""
url_source = ""

# Custom links (optional).
#   Uncomment line below to enable. For multiple links, use the form `[{...}, {...}, {...}]`.
# url_custom = [{name = "Custom Link", url = "http://example.org"}]

# Does the content use math formatting?
math = false

# Does the content use source code highlighting?
highlight = true

# Featured image
# Place your image in the `static/img/` folder and reference its filename below, e.g. `image = "example.jpg"`.
#[header]
#image = "headers/bubbles-wide.jpg"
#caption = "My caption 😄"

+++
