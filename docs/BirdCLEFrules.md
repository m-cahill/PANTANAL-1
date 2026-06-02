

[BirdCLEF+ 2026 | Kaggle](https://www.kaggle.com/competitions/birdclef-2026/)



Overview
--------

The goal of this competition is to develop machine learning frameworks capable of identifying understudied species within continuous audio data from Brazil's Pantanal wetlands. Successful solutions will help advance biodiversity monitoring in the last wild places on Earth.

Start

3 months ago

Close

a day to go

Merger & Entry

### Description

How do you protect an ecosystem you can’t fully see? One way is to listen.

This competition involves building models that automatically identify wildlife species from their vocalizations in audio recordings collected across the Pantanal wetlands. This work will support more reliable biodiversity monitoring in one of the world’s most diverse and threatened ecosystems.

Understanding how ecological communities respond to environmental change and restoration efforts is a central challenge in conservation science. The Pantanal — a wetland spanning 150,000+ km² across Brazil and neighboring countries — is home to over 650 bird species plus countless other animals, yet much of it remains unmonitored. Seasonal flooding, wildfires, agricultural expansion, and climate change make regular fieldwork challenging.

![Photo of a jaguar with its mouth open.](https://upload.wikimedia.org/wikipedia/commons/f/fb/On%C3%A7a_do_Pantanal.jpg)
Goal of the Competition
=======================

Conventional biodiversity monitoring across vast, remote regions is expensive and logistically demanding. To help address these challenges, a growing network of 1,000 acoustic recorders is being deployed across the Pantanal, running continuously to capture wildlife sounds across different habitats and seasons. Continuous audio recording allows researchers to capture multi-species soundscapes over extended periods, providing a community-level perspective on biodiversity dynamics. But the sheer volume of audio is too large to review manually, and labeled species data is limited.

This competition focuses on the development of machine learning models that identify wildlife species from passive acoustic monitoring (PAM). Proposed approaches should work across different habitats, withstand the constraints of messy, field-collected data, and support evidence-based conservation decisions. Successful solutions will help advance biodiversity monitoring in the last wild places on Earth, including research initiatives in the Pantanal wetlands of Brazil.

Listening carefully, and at scale, may be one of the most effective tools available to protect this landscape.

### Timeline

* **March 11, 2026** - Start Date.

* **May 27, 2026** - Entry Deadline. You must accept the competition rules before this date to compete.

* **May 27, 2026** - Team Merger Deadline. This is the last day participants may join or merge teams.

* **June 3, 2026** - Final Submission Deadline.

All deadlines are at 11:59 PM UTC on the corresponding day unless otherwise noted. The competition organizers reserve the right to update the contest timeline if they deem it necessary.

### Evaluation

The evaluation metric for this contest is [a version of macro-averaged ROC-AUC that skips classes that have no true positive labels.](https://www.kaggle.com/code/metric/birdclef-roc-auc)
Submission Format
=================

For each `row_id`, you should predict the probability that a given species was present. There is one column per species. **Each row covers a five-second window of audio.**

### Prizes

* 1st Place - $15,000
* 2nd Place - $10,000
* 3rd Place - $8,000
* 4th Place - $7,000
* 5th Place - $5,000

**Best working note award (optional):**

Participants of this competition are encouraged to submit working notes to the [CLEF 2026 conference](https://clef2026.clef-initiative.eu/). A best BirdCLEF+ working note competition will be held as part of the conference. The top two best working note award winners will receive $2,500 each. See the Evaluation page for judging criteria.

### Working Note Award (optional)

### Working Note Submission Timeline

We encourage participants to submit a working note write-up of their approach to the CLEF conference. Organizers will award $5,000 in prize money ($2,500 each) for the two best working note submissions.

Submission dates are:

* _June 3, 2026 - Competition deadline_
* **June 17, 2026** - Working note submission deadline
* **June 24, 2026** - Notification of acceptance
* **July 6, 2026** - Camera-ready submission deadline

Additional information on the submission process will be posted ahead of time on the discussion forum.

### Working Note Award Criteria

Criteria for the BirdCLEF+ Best Working Note Award:

**Originality**. The value of a paper is a function of the degree to which it presents new or novel technical material. Does the paper present results previously unknown? Does it push forward the frontiers of knowledge? Does it present new methods for solving old problems or new viewpoints on old problems? Or, on the other hand, is it a rehash of information already known?

**Quality**. A paper's value is a function of the innate character or degree of excellence of the work described. Was the work performed or the study made with a high degree of thoroughness? Was high engineering skill demonstrated? Is an experiment described which has a high degree of elegance? Or, on the other hand, is the work described pretty much of a run-of-the-mill nature?

**Contribution**. The value of a paper is a function of the degree to which it represents an overall contribution to the advancement of the art. This is different from originality. A paper may be highly original but may be concerned with a very minor, or even insignificant, matter or problem. On the other hand, a paper may make a great contribution by collecting and analyzing known data and facts and pointing out their significance. Or, a fine exposition of a known but obscure or complex phenomenon or theory or system or operating technique may be a very real contribution to the art. Obviously, a paper may well score highly on both originality and contribution. Perhaps the important question is, will the engineer who reads the paper be able to practice his profession more effectively because of having read it?

**Presentation**. The value of the paper is a function of the ease with which the reader can determine what the author is trying to present. Regardless of the other criteria, a paper is not good unless the material is presented clearly and effectively. Is the paper well written? Is the meaning of the author clear? Are the tables, charts, and figures clear? Is their meaning readily apparent? Is the information presented in the paper complete? At the same time, is the paper concise?

_Evaluation of the submitted BirdCLEF+ working notes:_

Each working note will be reviewed by two reviewers and scores averaged. Maximum score: 15.

a) Evaluation of work and contribution

* 5 points: Excellent work and a major contribution

* 4 points: Good, solid work of some importance

* 3 points: Solid work but a marginal contribution

* 2 points: Marginal work and minor contribution

* 1 point: Work doesn't meet scientific standards

b) Originality and novelty

* 5 points Trailblazing

* 4 points: A pioneering piece of work

* 3 points: One step ahead of the pack

* 2 points: Yet another paper about…

* 1 point: It's been said many times before

c) Readability and organization

* 5 points: Excellent

* 4 points: Well written

* 3 points: Readable

* 2 points: Needs considerable work

* 1 point: Work doesn't meet scientific standards

### Code Requirements

**This is a Code Competition**

Submissions to this competition must be made through Notebooks. For the "Submit" button to be active after a commit, the following conditions must be met:

* CPU Notebook <= 90 minutes run-time
* GPU Notebook submissions are disabled. You can technically submit but will only have 1 minute of runtime.
* Internet access disabled
* Freely & publicly available external data is allowed, including pre-trained models
* Submission file must be named submission.csv

Please see the [Code Competition FAQ](https://www.kaggle.com/docs/competitions#notebooks-only-FAQ) for more information on how to submit. And review the [code debugging doc](https://www.kaggle.com/code-competition-debugging) if you encounter submission errors.

### Acknowledgements

The development of the competition dataset was supported by the **[Bezos Earth Fund AI for Climate and Nature Grand Challenge](https://www.bezosearthfund.org/news-and-insights/bezos-earth-fund-announces-30-million-in-ai-grand-challenge-awards)**.

Compiling this extensive dataset was a major undertaking, and we are very thankful to the many domain experts who helped to collect and manually annotate the data for this competition. Specifically, we would like to thank (institutions and individual contributors in alphabetic order):

[**Chemnitz University of Technology**](https://www.tu-chemnitz.de/index.html.en): Stefan Kahl, Mario Lasseck, and Maximilian Eibl

[**Google Deepmind**](https://deepmind.google//): Tom Denton

[**iNaturalist**](https://www.inaturalist.org/): Grant van Horn

**[Instituto Homem Pantaneiro](https://institutohomempantaneiro.org.br/)**: Wener Hugo Arruda Moreno

**[Instituto Nacional de Pesquisa do Pantanal (INPP)](https://www.gov.br/inpp/en?set_language=en)**: Carolline Zatta Fieker, Karl-L. Schuchmann, Kirk Thiago Pedroso Azevedo, Lucas Korzune Sampaio Teles, Marinez Isaac Marques and Matheus Gonçalves dos Reis

[**K. Lisa Yang Center for Conservation Bioacoustics**](https://www.birds.cornell.edu/ccb/): Stefan Kahl, Larissa Sugai and Holger Klinck

[**LifeCLEF**](https://www.imageclef.org/LifeCLEF2026): Alexis Joly and Henning Müller

**[Sauá Consultoria Ambiental](https://www.sauaambiental.com.br/)**: Carolina Martins Garcia

[**Universidade Federal de Mato Grosso do Sul (UFMS)**](https://www.ufms.br/): Alyson Vieira de Melo, Daiene Louveira Hokama Sousa, José Luiz Massao Moreira Sugai, João Emílio de Almeida Júnior, Liliana Piatti, Mariana Motti Barbosa, Matheus de Oliveira Neves, Priscila do Nascimento Lopes and Ryan Christopher Kridler

[**Xeno-canto**](https://xeno-canto.org/): Willem-Pier Vellinga, Bob Planqué

**Photo Credits**

Banner picture of a Hyacinth Macaw by Thomas Fuhrmann. Inset picture of a Jaguar by Leonardo Ramos.

### Citation

Stefan Kahl, Tom Denton, Larissa Sugai, Liliana Piatti, Ryan Holbrook, Holger Klinck, and Ashley Oldacre. BirdCLEF+ 2026. https://kaggle.com/competitions/birdclef-2026, 2026. Kaggle.



---



Dataset Description
-------------------

Your challenge in this competition is to identify which species (birds, amphibians, mammals, reptiles, insects) are calling in recordings made in the **Brazilian Pantanal**. This is an important task for scientists who monitor animal populations for conservation purposes. More accurate solutions could enable more comprehensive monitoring.

This competition uses a hidden test set. When your submitted notebook is scored, the actual test data will be made available to your notebook.
Files
-----

**train_audio/** The training data consists of short recordings of individual bird, amphibian, reptile, mammal, and insect sounds generously uploaded by users of [xeno-canto.org](https://www.xeno-canto.org/) and [iNaturalist](https://www.inaturalist.org/). These files have been resampled to 32 kHz where applicable to match the test set audio and converted to the `ogg` format. Filenames consist of `[collection][file_id_in_collection].ogg`. The training data should have nearly all relevant files; we expect there is no benefit to looking for more on [xeno-canto.org](https://www.xeno-canto.org/) or [iNaturalist](https://www.inaturalist.org/) and appreciate your cooperation in limiting the burden on their servers. If you do, please make sure to adhere to the scraping rules of these data portals.

**test_soundscapes/** When you submit a notebook, the **test_soundscapes** directory will be populated with approximately 600 recordings to be used for scoring. They are 1 minute long and in `ogg` audio format, resampled to 32 kHz. The file names have the general form of `BC2026_Test_<file ID>_<site>_<date>_<time in UTC>.ogg` (e.g., file `BC2026_Test_0001_S05_20250227_010002.ogg` has file ID `0001`, was recorded at site `S05` on `Feb 27 2025` at `01:00 UTC`). It should take your submission notebook approximately five minutes to load all the test soundscapes. **Not all species from the training data actually occur in the test data.**

**train_soundscapes/** Additional audio data from roughly the same recording locations as the `test_soundscapes`. Filenames follow the same naming convention as the `test_soundscapes`; although some recording sites overlap between train and test, precise recording dates and times do NOT overlap with recordings of the hidden test data. This year, some of the `train_soundscapes` have been **labeled by expert annotators**, and we provide the ground truth for a subset of `train_soundscapes` in `train_soundscapes_labels.csv` with columns `filename` referencing the soundscape file, `start` and `end` referencing the 5-second segment for which column `primary_label` provides a semicolon-separated list of species codes that have been marked as present in this segment.

**Important note**: Some species with occurrences in the hidden test data might only have train samples in the labeled portion of `train_soundscapes` and not in the `train_audio` (XC and iNat data). However, not all species from `train_soundscapes` have occurrences in the `test_soundscapes`.

**train.csv** A wide range of metadata is provided for the training data. The most directly relevant fields are:

* `primary_label`: A code for the species (eBird code for birds, iNaturalist taxon ID for non-birds). You can review detailed information about the species by appending codes to eBird and iNaturalist taxon URL, such as `https://ebird.org/species/brnowl` for the Barn Owl or `https://www.inaturalist.org/taxa/41970` for the Jaguar. Not all species have their own pages; some links might fail.
* `secondary_labels`: List of species labels that have been marked by recordists to also occur in the recording. Can be incomplete.
* `latitude` & `longitude`: Coordinates for where the recording was taken. Some bird species may have local call 'dialects,' so you may want to seek geographic diversity in your training data.
* `author`: The user who provided the recording. `Unknown` if no name was provided.
* `filename`: The name of the associated audio file.
* `rating`: Values in 1..5 (1 - low quality, 5 - high quality; 0.5 reduction in rating when background species are present) provided by users of Xeno-canto; 0 implies no rating is available; iNaturalist does not provide quality ratings.
* `collection`: Either `XC` or `iNat`, indicating which collection the recording was taken from. Filenames also reference the collection and the ID within that collection.

**sample_submission.csv** A valid sample submission.

* `row_id`: A slug of `[soundscape_filename]_[end_time]` for the prediction; e.g., Segment 00:15-00:20 of 1-minute test soundscape `BC2026_Test_0001_S05_20250227_010002.ogg` has row ID `BC2026_Test_0001_S05_20250227_010002_20`.
* `[species_id]`: There are 234 species ID columns. You will need to predict the probability of the presence of each species for each row.

**taxonomy.csv** - Data on the different species, including iNaturalist taxon ID and class name (Aves, Amphibia, Mammalia, Insecta, Reptilia). Most insect species in this competition have **not been identified on species level and instead occur as sonotypes** (e.g., `47158son16` as insect sonotype 16); these sonotypes are treated as classes despite the lack of species ID and some of them also occur in the test data. **The 234 rows of this file represent the 234 class columns in the submission file.** `primary_label` specifies the submission file column name.

**recording_location.txt** - Some high-level information on the recording location (Pantanal, Brazil).
Files
-----

46213 files
Size
----

16.14 GB
Type
----

ogg, csv, txt
License
-------

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

### recording_location.txt(204 B)

Pantanal, Mato Grosso do Sul, Brazil, South AmericaMore info: https://en.wikipedia.org/wiki/PantanalCoordinates of recorder deployment sites:Latitude: -16.5 to -21.6Longitude: -55.9 to -57.6



---



Competition Rules
-----------------

ENTRY IN THIS COMPETITION CONSTITUTES YOUR ACCEPTANCE OF THESE OFFICIAL COMPETITION RULES.
------------------------------------------------------------------------------------------

**[See Section 3.18 for defined terms](https://www.kaggle.com/competitions/birdclef-2026/rules#18.-terms)**

_The Competition named below is a skills-based competition to promote and further the field of data science. You must register via the Competition Website to enter. To enter the Competition, you must agree to these Official Competition Rules, which incorporate by reference the provisions and content of the Competition Website and any Specific Competition Rules herein (collectively, the "Rules"). Please read these Rules carefully before entry to ensure you understand and agree. You further agree that Submission in the Competition constitutes agreement to these Rules. You may not submit to the Competition and are not eligible to receive the prizes associated with this Competition unless you agree to these Rules. These Rules form a binding legal agreement between you and the Competition Sponsor with respect to the Competition. Your competition Submissions must conform to the requirements stated on the Competition Website. Your Submissions will be scored based on the evaluation metric described on the Competition Website. Subject to compliance with the Competition Rules, Prizes, if any, will be awarded to Participants with the best scores, based on the merits of the data science models submitted. See below for the complete Competition Rules._

**You cannot sign up to Kaggle from multiple accounts and therefore you cannot enter or submit from multiple accounts.**

### 1. COMPETITION-SPECIFIC TERMS

#### 1. COMPETITION TITLE

BirdCLEF+ 2026

#### 2. COMPETITION SPONSOR

Google Research & Cornell Lab of Ornithology

#### 3. COMPETITION SPONSOR ADDRESS

1600 Amphitheatre Parkway, Mountain View, CA 94043

#### 4. COMPETITION WEBSITE

[BirdCLEF&#x2B; 2026 | Kaggle](https://www.kaggle.com/competitions/birdclef-2026)

#### 5. TOTAL PRIZES AVAILABLE: $50,000

* First Prize: $ 15,000
* Second Prize: $10,000
* Third Prize: $ 8,000
* Fourth Prize: $7,000
* Fifth Prize: $5,000

Best working note awards: $2,500 to each of the top 2 winners

#### 6. WINNER LICENSE TYPE

Open-Source

#### 7. DATA ACCESS AND USE

Attribution-NonCommercial-ShareAlike (CC BY-NC-SA)

### 2. COMPETITION-SPECIFIC RULES

In addition to the provisions of the General Competition Rules below, you understand and agree to these Competition-Specific Rules required by the Competition Sponsor:

#### 1. TEAM LIMITS

a. The maximum Team size is five (5). b. Team mergers are allowed and can be performed by the Team leader. In order to merge, the combined Team must have a total Submission count less than or equal to the maximum allowed as of the Team Merger Deadline. The maximum allowed is the number of Submissions per day multiplied by the number of days the competition has been running.

#### 2. SUBMISSION LIMITS

a. You may submit a maximum of five (5) Submissions per day. b. You may select up to two (2) Final Submissions for judging.

#### 3. COMPETITION TIMELINE

a. Competition Timeline dates (including Entry Deadline, Final Submission Deadline, Start Date, and Team Merger Deadline, as applicable) are reflected on the competition’s Overview > Timeline page.

#### 4. COMPETITION DATA

a. Data Access and Use.

1. _Data Access and Use_. You may access and use the Competition Data for non-commercial purposes only, including for participating in the Competition and on Kaggle.com forums, and for academic research and education. The Competition Sponsor reserves the right to disqualify any participant who uses the Competition Data other than as permitted by the Competition Website and these Rules.
   The Competition Data is also subject to the following terms and conditions: [Attribution-NonCommercial-ShareAlike (CC BY-NC-SA)](https://creativecommons.org/licenses/by-nc-sa/4.0/). To the extent that the terms and conditions located at the URL conflict with or are inconsistent with these Rules, these Rules will govern your use of the Competition Data.

b. Data Security.

1. You agree to use reasonable and suitable measures to prevent persons who have not formally agreed to these Rules from gaining access to the Competition Data. You agree not to transmit, duplicate, publish, redistribute or otherwise provide or make available the Competition Data to any party not participating in the Competition. You agree to notify Kaggle immediately upon learning of any possible unauthorized transmission of or unauthorized access to the Competition Data and agree to work with Kaggle to rectify any unauthorized transmission or access.

#### 5. WINNER LICENSE

a. Under Section 2.8 (Winners Obligations) of the General Rules below, you hereby grant and will grant the Competition Sponsor the following license(s) with respect to your Submission if you are a Competition winner:

1. _Open Source_: You hereby license and will license your winning Submission and the source code used to generate the Submission under an Open Source Initiative-approved license (see [www.opensource.org](http://www.opensource.org/)) that in no event limits commercial use of such code or model containing or depending on such code.

2. For generally commercially available software that you used to generate your Submission that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, you do not need to grant the license in the preceding Section for that software.

3. In the event that input data or pretrained models with an incompatible license are used to generate your winning solution, you do not need to grant an open source license in the preceding Section for that data and/or model(s).

b. You may be required by the Sponsor to provide a detailed description of how the winning Submission was generated, to the Competition Sponsor’s specifications, as outlined in Section 2.8, Winner’s Obligations. This may include a detailed description of methodology, where one must be able to reproduce the approach by reading the description, and includes a detailed explanation of the architecture, preprocessing, loss function, training details, hyper-parameters, etc. The description should also include a link to a code repository with complete and detailed instructions so that the results obtained can be reproduced.

#### 6. EXTERNAL DATA AND TOOLS

a. You may use data other than the Competition Data (“External Data”) to develop and test your Submissions. However, you will ensure the External Data is either publicly available and equally accessible to use by all Participants of the Competition for purposes of the competition at no cost to the other Participants, or satisfies the Reasonableness criteria as outlined in Section 2.6.b below. The ability to use External Data under this Section does not limit your other obligations under these Competition Rules, including but not limited to Section 2.8 (Winners Obligations).

b. The use of external data and models is acceptable unless specifically prohibited by the Host. Because of the potential costs or restrictions (e.g., “geo restrictions”) associated with obtaining rights to use external data or certain software and associated tools, their use must be “reasonably accessible to all” and of “minimal cost”. Also, regardless of the cost challenges as they might affect all Participants during the course of the competition, the costs of potentially procuring a license for software used to generate a Submission, must also be considered. The Host will employ an assessment of whether or not the following criteria can exclude the use of the particular LLM, data set(s), or tool(s):

1. Are Participants being excluded from a competition because of the "excessive" costs for access to certain LLMs, external data, or tools that might be used by other Participants. The Host will assess the excessive cost concern by applying a “Reasonableness” standard (the “Reasonableness Standard”). The Reasonableness Standard will be determined and applied by the Host in light of things like cost thresholds and accessibility.

2. By way of example only, a small subscription charge to use additional elements of a large language model such as Gemini Advanced are acceptable if meeting the Reasonableness Standard of Sec. 8.2. Purchasing a license to use a proprietary dataset that exceeds the cost of a prize in the competition would not be considered reasonable.

c. Automated Machine Learning Tools (“AMLT”)

1. Individual Participants and Teams may use automated machine learning tool(s) (“AMLT”) (e.g., Google toML, H2O Driverless AI, etc.) to create a Submission, provided that the Participant or Team ensures that they have an appropriate license to the AMLT such that they are able to comply with the Competition Rules.

#### 7. ELIGIBILITY

a. Unless otherwise stated in the Competition-Specific Rules above or prohibited by internal policies of the Competition Entities, employees, interns, contractors, officers and directors of Competition Entities may enter and participate in the Competition, but are not eligible to win any Prizes. "Competition Entities" means the Competition Sponsor, Kaggle Inc., and their respective parent companies, subsidiaries and affiliates. If you are such a Participant from a Competition Entity, you are subject to all applicable internal policies of your employer with respect to your participation.

#### 8. WINNER’S OBLIGATIONS

a. As a condition to being awarded a Prize, a Prize winner must fulfill the following obligations:

1. Deliver to the Competition Sponsor the final model's software code as used to generate the winning Submission and associated documentation. The delivered software code should follow [these documentation guidelines](https://www.kaggle.com/WinningModelDocumentationGuidelines), must be capable of generating the winning Submission, and contain a description of resources required to build and/or run the executable code successfully. For avoidance of doubt, delivered software code should include training code, inference code, and a description of the required computational environment.

a. To the extent that the final model’s software code includes generally commercially available software that is not owned by you, but that can be procured by the Competition Sponsor without undue expense, then instead of delivering the code for that software to the Competition Sponsor, you must identify that software, method for procuring it, and any parameters or other information necessary to replicate the winning Submission; Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules, including but not limited to Section 2.5 (Winners License), Section 2.8 (Winners Obligations), and Section 3.14 (Warranty, Indemnity, and Release).”

b. Individual Participants and Teams who create a Submission using an AMLT may win a Prize. However, for clarity, the potential winner’s Submission must still meet the requirements of these Rules,

1. Grant to the Competition Sponsor the license to the winning Submission stated in the Competition Specific Rules above, and represent that you have the unrestricted right to grant that license;

2. Sign and return all Prize acceptance documents as may be required by Competition Sponsor or Kaggle, including without limitation: (a) eligibility certifications; (b) licenses, releases and other agreements required under the Rules; and (c) U.S. tax forms (such as IRS Form W-9 if U.S. resident, IRS Form W-8BEN if foreign resident, or future equivalents).

#### 9. GOVERNING LAW

a. Unless otherwise provided in the Competition Specific Rules above, all claims arising out of or relating to these Rules will be governed by California law, excluding its conflict of laws rules, and will be litigated exclusively in the Federal or State courts of Santa Clara County, California, USA. The parties consent to personal jurisdiction in those courts. If any provision of these Rules is held to be invalid or unenforceable, all remaining provisions of the Rules will remain in full force and effect.
Kaggle Competition Foundational Rules
-------------------------------------

(Non-editable)

Competition participants must also agree to Kaggle's Foundational Competition Rules. These rules will supersede the competition-specific rules in the event of any conflict.

The following Kaggle Competition Foundational Rules (“ Foundational Rules ”) apply to every competition regardless of whether the Sponsor creates competition-specific rules. Any competition-specific rules provided by the Sponsor are in addition to these rules, and in the case of any conflict or inconsistency, these Foundational Rules control and nullify contrary competition-specific rules.

### GENERAL COMPETITION RULES - BINDING AGREEMENT

#### 1. ELIGIBILITY

a. To be eligible to enter the Competition, you must be:

1. a registered account holder at Kaggle.com;
2. the older of 18 years old or the age of majority in your jurisdiction of residence (unless otherwise agreed to by Competition Sponsor and appropriate parental/guardian consents have been obtained by Competition Sponsor);
3. not a resident of Crimea, so-called Donetsk People's Republic (DNR) or Luhansk People's Republic (LNR), Cuba, Iran, or North Korea; and
4. not a person or representative of an entity under U.S. export controls or sanctions (see: [https://www.treasury.gov/resourcecenter/sanctions/Programs/Pages/Programs.aspx](https://www.treasury.gov/resource-center/sanctions/Programs/Pages/Programs.aspx)).

b. Competitions are open to residents of the United States and worldwide, except that if you are a resident of Crimea, so-called Donetsk People's Republic (DNR) or Luhansk People's Republic (LNR), Cuba, Iran, North Korea, or are subject to U.S. export controls or sanctions, you may not enter the Competition. Other local rules and regulations may apply to you, so please check your local laws to ensure that you are eligible to participate in skills-based competitions. The Competition Host reserves the right to forego or award alternative Prizes where needed to comply with local laws. If a winner is located in a country where prizes cannot be awarded, then they are not eligible to receive a prize.

c. If you are entering as a representative of a company, educational institution or other legal entity, or on behalf of your employer, these rules are binding on you, individually, and the entity you represent or where you are an employee. If you are acting within the scope of your employment, or as an agent of another party, you warrant that such party or your employer has full knowledge of your actions and has consented thereto, including your potential receipt of a Prize. You further warrant that your actions do not violate your employer's or entity's policies and procedures.

d. The Competition Sponsor reserves the right to verify eligibility and to adjudicate on any dispute at any time. If you provide any false information relating to the Competition concerning your identity, residency, mailing address, telephone number, email address, ownership of right, or information required for entering the Competition, you may be immediately disqualified from the Competition.

#### 2. SPONSOR AND HOSTING PLATFORM

a. The Competition is sponsored by Competition Sponsor named above. The Competition is hosted on behalf of Competition Sponsor by Kaggle Inc. ("Kaggle"). Kaggle is an independent contractor of Competition Sponsor, and is not a party to this or any agreement between you and Competition Sponsor. You understand that Kaggle has no responsibility with respect to selecting the potential Competition winner(s) or awarding any Prizes. Kaggle will perform certain administrative functions relating to hosting the Competition, and you agree to abide by the provisions relating to Kaggle under these Rules. As a Kaggle.com account holder and user of the Kaggle competition platform, remember you have accepted and are subject to the Kaggle Terms of Service at [www.kaggle.com/terms](http://www.kaggle.com/terms) in addition to these Rules.

#### 3. COMPETITION PERIOD

a. For the purposes of Prizes, the Competition will run from the Start Date and time to the Final Submission Deadline (such duration the “Competition Period”). The Competition Timeline is subject to change, and Competition Sponsor may introduce additional hurdle deadlines during the Competition Period. Any updated or additional deadlines will be publicized on the Competition Website. It is your responsibility to check the Competition Website regularly to stay informed of any deadline changes. YOU ARE RESPONSIBLE FOR DETERMINING THE CORRESPONDING TIME ZONE IN YOUR LOCATION.

#### 4. COMPETITION ENTRY

a. NO PURCHASE NECESSARY TO ENTER OR WIN. To enter the Competition, you must register on the Competition Website prior to the Entry Deadline, and follow the instructions for developing and entering your Submission through the Competition Website. Your Submissions must be made in the manner and format, and in compliance with all other requirements, stated on the Competition Website (the "Requirements"). Submissions must be received before any Submission deadlines stated on the Competition Website. Submissions not received by the stated deadlines will not be eligible to receive a Prize. b. Submissions may not use or incorporate information from hand labeling or human prediction of the validation dataset or test data records. c. If the Competition is a multi-stage competition with temporally separate training and/or test data, one or more valid Submissions may be required during each Competition stage in the manner described on the Competition Website in order for the Submissions to be Prize eligible. d. Submissions are void if they are in whole or part illegible, incomplete, damaged, altered, counterfeit, obtained through fraud, or late. Competition Sponsor reserves the right to disqualify any entrant who does not follow these Rules, including making a Submission that does not meet the Requirements.

#### 5. INDIVIDUALS AND TEAMS

a. Individual Account. You may make Submissions only under one, unique Kaggle.com account. You will be disqualified if you make Submissions through more than one Kaggle account, or attempt to falsify an account to act as your proxy. You may submit up to the maximum number of Submissions per day as specified on the Competition Website. b. Teams. If permitted under the Competition Website guidelines, multiple individuals may collaborate as a Team; however, you may join or form only one Team. Each Team member must be a single individual with a separate Kaggle account. You must register individually for the Competition before joining a Team. You must confirm your Team membership to make it official by responding to the Team notification message sent to your Kaggle account. Team membership may not exceed the Maximum Team Size stated on the Competition Website. c. Team Merger. Teams may request to merge via the Competition Website. Team mergers may be allowed provided that: (i) the combined Team does not exceed the Maximum Team Size; (ii) the number of Submissions made by the merging Teams does not exceed the number of Submissions permissible for one Team at the date of the merger request; (iii) the merger is completed before the earlier of: any merger deadline or the Competition deadline; and (iv) the proposed combined Team otherwise meets all the requirements of these Rules. d. Private Sharing. No private sharing outside of Teams. Privately sharing code or data outside of Teams is not permitted. It's okay to share code if made available to all Participants on the forums.

#### 6. SUBMISSION CODE REQUIREMENTS

a. Private Code Sharing. Unless otherwise specifically permitted under the Competition Website or Competition Specific Rules above, during the Competition Period, you are not allowed to privately share source or executable code developed in connection with or based upon the Competition Data or other source or executable code relevant to the Competition (“Competition Code”). This prohibition includes sharing Competition Code between separate Teams, unless a Team merger occurs. Any such sharing of Competition Code is a breach of these Competition Rules and may result in disqualification. b. Public Code Sharing. You are permitted to publicly share Competition Code, provided that such public sharing does not violate the intellectual property rights of any third party. If you do choose to share Competition Code or other such code, you are required to share it on Kaggle.com on the discussion forum or notebooks associated specifically with the Competition for the benefit of all competitors. By so sharing, you are deemed to have licensed the shared code under an Open Source Initiative-approved license (see [www.opensource.org](http://www.opensource.org/)) that in no event limits commercial use of such Competition Code or model containing or depending on such Competition Code. c. Use of Open Source. Unless otherwise stated in the Specific Competition Rules above, if open source code is used in the model to generate the Submission, then you must only use open source code licensed under an Open Source Initiative-approved license (see [www.opensource.org](http://www.opensource.org/)) that in no event limits commercial use of such code or model containing or depending on such code.

#### 7. DETERMINING WINNERS

a. Each Submission will be scored and ranked by the evaluation metric stated on the Competition Website. During the Competition Period, the current ranking will be visible on the Competition Website's Public Leaderboard. The potential winner(s) are determined solely by the leaderboard ranking on the Private Leaderboard, subject to compliance with these Rules. The Public Leaderboard will be based on the public test set and the Private Leaderboard will be based on the private test set. b. In the event of a tie, the Submission that was entered first to the Competition will be the winner. In the event a potential winner is disqualified for any reason, the Submission that received the next highest score rank will be chosen as the potential winner.

#### 8. NOTIFICATION OF WINNERS & DISQUALIFICATION

a. The potential winner(s) will be notified by email. b. If a potential winner (i) does not respond to the notification attempt within one (1) week from the first notification attempt or (ii) notifies Kaggle within one week after the Final Submission Deadline that the potential winner does not want to be nominated as a winner or does not want to receive a Prize, then, in each case (i) and (ii) such potential winner will not receive any Prize, and an alternate potential winner will be selected from among all eligible entries received based on the Competition’s judging criteria. c. In case (i) and (ii) above Kaggle may disqualify the Participant. However, in case (ii) above, if requested by Kaggle, such potential winner may provide code and documentation to verify the Participant’s compliance with these Rules. If the potential winner provides code and documentation to the satisfaction of Kaggle, the Participant will not be disqualified pursuant to this paragraph. d. Competition Sponsor reserves the right to disqualify any Participant from the Competition if the Competition Sponsor reasonably believes that the Participant has attempted to undermine the legitimate operation of the Competition by cheating, deception, or other unfair playing practices or abuses, threatens or harasses any other Participants, Competition Sponsor or Kaggle. e. A disqualified Participant may be removed from the Competition leaderboard, at Kaggle's sole discretion. If a Participant is removed from the Competition Leaderboard, additional winning features associated with the Kaggle competition platform, for example Kaggle points or medals, may also not be awarded. f. The final leaderboard list will be publicly displayed at Kaggle.com. Determinations of Competition Sponsor are final and binding.

#### 9. PRIZES

a. Prize(s) are as described on the Competition Website and are only available for winning during the time period described on the Competition Website. The odds of winning any Prize depends on the number of eligible Submissions received during the Competition Period and the skill of the Participants. b. All Prizes are subject to Competition Sponsor's review and verification of the Participant’s eligibility and compliance with these Rules, and the compliance of the winning Submissions with the Submissions Requirements. In the event that the Submission demonstrates non-compliance with these Competition Rules, Competition Sponsor may at its discretion take either of the following actions: (i) disqualify the Submission(s); or (ii) require the potential winner to remediate within one week after notice all issues identified in the Submission(s) (including, without limitation, the resolution of license conflicts, the fulfillment of all obligations required by software licenses, and the removal of any software that violates the software restrictions). c. A potential winner may decline to be nominated as a Competition winner in accordance with Section 3.8. d. Potential winners must return all required Prize acceptance documents within two (2) weeks following notification of such required documents, or such potential winner will be deemed to have forfeited the prize and another potential winner will be selected. Prize(s) will be awarded within approximately thirty (30) days after receipt by Competition Sponsor or Kaggle of the required Prize acceptance documents. Transfer or assignment of a Prize is not allowed. e. You are not eligible to receive any Prize if you do not meet the Eligibility requirements in Section 2.7 and Section 3.1 above. f. If a Team wins a monetary Prize, the Prize money will be allocated in even shares between the eligible Team members, unless the Team unanimously opts for a different Prize split and notifies Kaggle before Prizes are issued.

#### 10. TAXES

a. ALL TAXES IMPOSED ON PRIZES ARE THE SOLE RESPONSIBILITY OF THE WINNERS. Payments to potential winners are subject to the express requirement that they submit all documentation requested by Competition Sponsor or Kaggle for compliance with applicable state, federal, local and foreign (including provincial) tax reporting and withholding requirements. Prizes will be net of any taxes that Competition Sponsor is required by law to withhold. If a potential winner fails to provide any required documentation or comply with applicable laws, the Prize may be forfeited and Competition Sponsor may select an alternative potential winner. Any winners who are U.S. residents will receive an IRS Form-1099 in the amount of their Prize.

#### 11. GENERAL CONDITIONS

a. All federal, state, provincial and local laws and regulations apply.

#### 12. PUBLICITY

a. You agree that Competition Sponsor, Kaggle and its affiliates may use your name and likeness for advertising and promotional purposes without additional compensation, unless prohibited by law.

#### 13. PRIVACY

a. You acknowledge and agree that Competition Sponsor and Kaggle may collect, store, share and otherwise use personally identifiable information provided by you during the Kaggle account registration process and the Competition, including but not limited to, name, mailing address, phone number, and email address (“Personal Information”). Kaggle acts as an independent controller with regard to its collection, storage, sharing, and other use of this Personal Information, and will use this Personal Information in accordance with its Privacy Policy <[www.kaggle.com/privacy](http://www.kaggle.com/privacy)>, including for administering the Competition. As a Kaggle.com account holder, you have the right to request access to, review, rectification, portability or deletion of any personal data held by Kaggle about you by logging into your account and/or contacting Kaggle Support at <[www.kaggle.com/contact](http://www.kaggle.com/contact)>. b. As part of Competition Sponsor performing this contract between you and the Competition Sponsor, Kaggle will transfer your Personal Information to Competition Sponsor, which acts as an independent controller with regard to this Personal Information. As a controller of such Personal Information, Competition Sponsor agrees to comply with all U.S. and foreign data protection obligations with regard to your Personal Information. Kaggle will transfer your Personal Information to Competition Sponsor in the country specified in the Competition Sponsor Address listed above, which may be a country outside the country of your residence. Such country may not have privacy laws and regulations similar to those of the country of your residence.

#### 14. WARRANTY, INDEMNITY AND RELEASE

a. You warrant that your Submission is your own original work and, as such, you are the sole and exclusive owner and rights holder of the Submission, and you have the right to make the Submission and grant all required licenses. You agree not to make any Submission that: (i) infringes any third party proprietary rights, intellectual property rights, industrial property rights, personal or moral rights or any other rights, including without limitation, copyright, trademark, patent, trade secret, privacy, publicity or confidentiality obligations, or defames any person; or (ii) otherwise violates any applicable U.S. or foreign state or federal law. b. To the maximum extent permitted by law, you indemnify and agree to keep indemnified Competition Entities at all times from and against any liability, claims, demands, losses, damages, costs and expenses resulting from any of your acts, defaults or omissions and/or a breach of any warranty set forth herein. To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless the Competition Entities from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from: (a) your Submission or other material uploaded or otherwise provided by you that infringes any third party proprietary rights, intellectual property rights, industrial property rights, personal or moral rights or any other rights, including without limitation, copyright, trademark, patent, trade secret, privacy, publicity or confidentiality obligations, or defames any person; (b) any misrepresentation made by you in connection with the Competition; (c) any non-compliance by you with these Rules or any applicable U.S. or foreign state or federal law; (d) claims brought by persons or entities other than the parties to these Rules arising from or related to your involvement with the Competition; and (e) your acceptance, possession, misuse or use of any Prize, or your participation in the Competition and any Competition-related activity. c. You hereby release Competition Entities from any liability associated with: (a) any malfunction or other problem with the Competition Website; (b) any error in the collection, processing, or retention of any Submission; or (c) any typographical or other error in the printing, offering or announcement of any Prize or winners.

#### 15. INTERNET

a. Competition Entities are not responsible for any malfunction of the Competition Website or any late, lost, damaged, misdirected, incomplete, illegible, undeliverable, or destroyed Submissions or entry materials due to system errors, failed, incomplete or garbled computer or other telecommunication transmission malfunctions, hardware or software failures of any kind, lost or unavailable network connections, typographical or system/human errors and failures, technical malfunction(s) of any telephone network or lines, cable connections, satellite transmissions, servers or providers, or computer equipment, traffic congestion on the Internet or at the Competition Website, or any combination thereof, which may limit a Participant’s ability to participate.

#### 16. RIGHT TO CANCEL, MODIFY OR DISQUALIFY

a. If for any reason the Competition is not capable of running as planned, including infection by computer virus, bugs, tampering, unauthorized intervention, fraud, technical failures, or any other causes which corrupt or affect the administration, security, fairness, integrity, or proper conduct of the Competition, Competition Sponsor reserves the right to cancel, terminate, modify or suspend the Competition. Competition Sponsor further reserves the right to disqualify any Participant who tampers with the submission process or any other part of the Competition or Competition Website. Any attempt by a Participant to deliberately damage any website, including the Competition Website, or undermine the legitimate operation of the Competition is a violation of criminal and civil laws. Should such an attempt be made, Competition Sponsor and Kaggle each reserves the right to seek damages from any such Participant to the fullest extent of the applicable law.

#### 17. NOT AN OFFER OR CONTRACT OF EMPLOYMENT

a. Under no circumstances will the entry of a Submission, the awarding of a Prize, or anything in these Rules be construed as an offer or contract of employment with Competition Sponsor or any of the Competition Entities. You acknowledge that you have submitted your Submission voluntarily and not in confidence or in trust. You acknowledge that no confidential, fiduciary, agency, employment or other similar relationship is created between you and Competition Sponsor or any of the Competition Entities by your acceptance of these Rules or your entry of your Submission.

#### 18. DEFINITIONS

a. "Competition Data" are the data or datasets available from the Competition Website for the purpose of use in the Competition, including any prototype or executable code provided on the Competition Website. The Competition Data will contain private and public test sets. Which data belongs to which set will not be made available to Participants. b. An “Entry” is when a Participant has joined, signed up, or accepted the rules of a competition. Entry is required to make a Submission to a competition. c. A “Final Submission” is the Submission selected by the user, or automatically selected by Kaggle in the event not selected by the user, that is/are used for final placement on the competition leaderboard. d. A “Participant” or “Participant User” is an individual who participates in a competition by entering the competition and making a Submission. e. The “Private Leaderboard” is a ranked display of Participants’ Submission scores against the private test set. The Private Leaderboard determines the final standing in the competition. f. The “Public Leaderboard” is a ranked display of Participants’ Submission scores against a representative sample of the test data. This leaderboard is visible throughout the competition. g. A “Sponsor” is responsible for hosting the competition, which includes but is not limited to providing the data for the competition, determining winners, and enforcing competition rules. h. A “Submission” is anything provided by the Participant to the Sponsor to be evaluated for competition purposes and determine leaderboard position. A Submission may be made as a model, notebook, prediction file, or other format as determined by the Sponsor. i. A “Team” is one or more Participants participating together in a Kaggle competition, by officially merging together as a Team within the competition platform.





---




