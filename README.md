# Document OCR

Link to the Webpage: [ENTER LINK HERE WHEN PUBLISHED]()

A tool that takes a `.pdf` file of handwritten, typed, or otherwise notes and turns it into a `docx` (Microsoft Word Document) for professional document _with_ Office Math Markup Language (OMML). 


Due to the lightweight Optical-Character-Recognigition (OCR) in play, the matching will not be perfect. Thus,
it is best used to ease the process of bringing written work to a more professional state that better reflects practices seen in industry.

The goal of this tool is to help myself, classmates, labmates or anyone to create more professional documents for calculations, labs, homework and assignments.



### Application Structure

#### Frontend:

Deployed through Cloudflare Pages (Static HTML Webpage hosting). 


#### Backend: 

Containerized Python FastAPI for REST API endpoints, deployed on Google Cloud Run (Google Cloud Platform) for request based, stateless compute. Also configured to scale to zero when no requests present.



#### Database:

Currently, MongoDB (NoSQL) to host transaction records?

Current configuration should have container concurrency of only 



## Development

Requires python 3.12
python -m pip install -r requirements.txt

I also intend to provide a minimal CLI tooling for those wishing to use the tool locally. (Incomplete)



