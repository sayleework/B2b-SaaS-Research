B2b-SaaS-Research
This research is focused on AI-powered SEO content production as a growth channel for B2B SaaS companies in the HR/recruiting space (I've tried my best to find this alignment)

Process: 
Chose the third topic: AI powered SEO content production
Will research across youtube, linkedin, spotify (for podcasts) and ofcourse google xray search for experts who practice what they preach, in this space.
Will then build different files to store all their names, content urls & content transcripts.

Research Methodology:
- Searched YouTube for terms like "AI SEO content", "programmatic SEO AI", "B2B SaaS SEO"
- Tried to look for linkedin top voices in the AI SEO / SEO / AI powered SEO space. Found a really relevant link, followed it to find multiple experts given the title "The 15 AI Search and AEO Experts to Follow in 2026" by Conductor (Link: https://www.conductor.com/academy/aeo-experts/#ryan-law)
- Prioritized creators who show real workflows, tools, and results — not just theory
- Cross-referenced names that appeared across multiple searches or were mentioned by other experts
- Came across some channels and podcasts which I've mentioned in the file "Other Research"

Tools Used
**Claude Code (Cursor IDE)**
Used to write & run the transcript collection script directly inside the repository. Claude Code generated a Python script that automated fetching and saving transcripts as markdown files.
**Supadata API**
Used to collect YouTube transcripts programmatically via API calls. The script (fetch_transcripts.py) sends video URLs to the Supadata API and saves each transcript as a .md file in /research/youtube-transcripts/.
**Python**
The fetch_transcripts.py script was written in Python by claude code and run locally to automate transcript collection.
**GitHub**
To create this repository :)

A lot of hardwork, challenges and "oh I should've checked this before committing" later, my final Repo. Hope it adds value to you, the way that it did to me while creating it :)
