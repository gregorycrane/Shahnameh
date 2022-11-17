# Perseus Shahnameh -- a experimental digital edition

Our goal is to provide for the Persian Shahnameh the same level of support that is available for the Homeric Epics and other Greek and Latin works. In particular, Farnoosh Shamsian has been working to enable speakers of Persian to study Ancient Greek in particular and she begins by having them learn how to tanslate Homer. Our goal is to encourage speakers of English, for their part, to study the Persian of the Shahnameh. Ultimately, we want to stimulate cross-cultural discussion and exchange, with speakers of English and of Persian sharing their different perspectives on both the Greek and the Persian epics. 

While we will clearly benefit from those Persian speakers comfortable in Englisn and the (still much smaller number of) English speakers who can make themselves understood in Persian, machine translation has reached a level where pragmatic people acting in good faith can now communicate with each other, posing questions where the automatic translation is unclear. (Proof of concept for GRC: I read multiple tweets in Persian each day about the events in Iran in fall 2022. Some references are obscure. Sometimes the translation is not clear. But I normally understand the vast majority of what I read.) 

Subtasks wthin this larger goal include the following.

Firdawsī., Vullers, J. Augustus. (187784). Liber regum qui inscribitur Schahname. Editionem parisiensem recognitam et emendatam lectionibus variis et additamentis editionis calcuttensis auxit, notis criticis illustravit J. A. Vullers. Lugduni Batavorum.

* Scans of the three volumes that were published are available from the Hathitrust: https://catalog.hathitrust.org/Record/100351775. 

* We do not, however, have a digital transcription of this text. That would require OCR of the Persian and then post-editing.


  Pizzi, Italo. Manuale Della Lingua Persiana; Grammatica, Antologia, Vocabolario. W. Gerhard, 1883, https://catalog.hathitrust.org/Record/100547672. Pizzi's work is comparable to Pharr's Homeric Greek: it teaches Persian by giving readers heavily annotated selections with a glossary and a grammar. Notes on this:

  * Pizzi has a short grammar at the start (pp. 3-45). This is tricky to enter - grammar entries should be "alive," i.e. readers should see exactly how often and where each grammatical feature shows up in the reading passges. Thus readers should always have examples and be able to determine how important a feature is. Readers of the reading passages should also have links back into the grammar so that they can see a grammatical explanation for what they are reading.

  * Pizzi writes in Italian but machine translation converts his Italian into English very effectively. The results are not perfect but they are easily edited. 

  * pp. 57-238: Selections from 20 different sections of the Shahnameh, c. 26,000 words total (5X bigger than Iliad 1, on which Pharr bases his work). Pizzi draws these from Vullers' edition. Farnoosh has created a digital version of these transcriptions already: https://docs.google.com/document/d/1-k_YWM5SR_Yn0USE-fpAkYeuJkGKVzIwOMy29VJHvRo/edit. This gives us a substantion subet of the Shahnameh -- far more than anyone would be able to read in a single year of instruction. Probably enough to do some useful training and text mining.

  * Literal translation of readings 1-8 (pp. 239-293) with words added to the Italian for stylistic purposes marked in italics. This is enough so that an independent learner could use this to learn how to read the Shahnameh. The hardest task will be recpaturing the italics (which tells you which words are not aligned). It might be best not to bother but just to align Persian and Italian/English directly but it is a shame to leave out the information that italics conveys in print. The slightly corrected OCR of the Italian is available [on Github](https://github.com/gregorycrane/Shahnameh/blob/master/pizzi.littrans.txt).

  * A glossary not only provides definitions but also vocalized transliterations (pp. 299-473). A first pass at editing this glossary is on Github: https://github.com/gregorycrane/Shahnameh/blob/master/pizzi-glossary.it.xml. Crane did a first pass matching words in the reader to the appropriate glossary entries (some debugging info [on Google Drive](https://docs.google.com/spreadsheets/d/12Y0Icmzg7NO-zjFfV8_XuHfhGEgYlUHNizk19VRtKoM/edit#gid=0)) -- readers will be able to click on most words in the readings and go to the glossary.

  

