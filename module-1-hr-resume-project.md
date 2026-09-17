# Module 1: HR + Resume + Project Discussion (Q1–Q20)

[← Back to Index](README.md)

---

**Q1. Tell me about yourself.**

"Hi, I'm Pavan Dubey. I have around 5.5 years of experience in backend development. I started my career with PHP and Laravel at Investor Homez, then moved to Nippon Data Systems where I worked on Django applications, REST APIs, and government projects like NICSI. I also worked on Drupal 7 to 8 migration.

After that, I did freelancing for a few months where I built Django applications and FinTech solutions. Then I joined theCloudTree, and later Neighborshook Pvt. Ltd., where I worked on a hyperlocal platform called Neighborshook. There I developed scalable backend services using Laravel and Django, built REST APIs, admin dashboards, and worked on an AI-powered content moderation system using Hugging Face Transformers — mainly DistilBERT for toxicity detection and text classification.

Currently I'm working as a freelance Software Engineer, building Python automation tools using Selenium, BeautifulSoup, Pandas, OpenPyXL, and Tkinter desktop applications packaged with PyInstaller.

I'm looking for a role where I can work on larger backend systems, AI integration, and take more technical ownership."

**Follow-up: Why are you looking for a change?**

"I want to work on bigger backend systems, learn from experienced teams, and take on more challenging responsibilities — especially in Python, Django, and AI-based applications."

---

**Q2. Walk me through your resume.**

"I started at Investor Homez as a PHP Developer — worked on WordPress, Laravel, and custom backend features.

Then I joined Nippon Data Systems — worked on an intranet Stock Management System using Python and Django, maintained NICSI (Government of India) project, built REST APIs with Django and PHP, and migrated Drupal 7 to Drupal 8.

After that, I did freelancing — built secure Django applications and REST APIs for FinTech clients.

Then I joined theCloudTree — worked on Neighborshook platform, built backend services and REST APIs using Laravel, admin dashboards, and integrated NLP-based content analysis using Hugging Face Transformers.

Later the project transitioned to Neighborshook Pvt. Ltd. — there I continued backend development, built user verification, neighbourhood feeds, moderation tools, and worked on AI-powered content moderation using DistilBERT for toxicity detection.

Currently I'm freelancing — building Python automation tools, web scrapers, Excel report generators, and Tkinter desktop apps."

---

**Q3. Which project are you most proud of?**

"The AI-powered content moderation system at Neighborshook. I worked on backend APIs, integrated Hugging Face Transformers — mainly DistilBERT — for toxicity detection and text classification, built admin moderation workflows, and optimized database queries for high-traffic use cases. It gave me real exposure to both backend engineering and practical NLP."

**Follow-up: Did you train the model yourself?**

"No, I didn't train DistilBERT from scratch. We used pretrained transformer models from Hugging Face and adapted them for our classification task. My main work was backend integration, API development, prompt/response handling, and moderation workflow."

---

**Q4. Explain your role in the AI moderation project.**

"My primary responsibility was backend development. I built REST APIs using Django and Laravel, integrated Hugging Face Transformers for NLP-based toxicity detection, handled text classification, built APIs for the moderation dashboard, and optimized database queries. I wasn't responsible for training the transformer model itself — we used pretrained models."

---

**Q5. Explain the complete request flow of your moderation system.**

"A user submits content through the mobile or web app. The Laravel/Django API validates the request and stores the initial record in MySQL. Then the content is passed to the NLP pipeline where a Hugging Face transformer model — mainly DistilBERT — classifies it for toxicity, spam, or policy violations. The result is stored back in the database, and the admin dashboard displays the moderation status. For heavy processing, we also used background jobs where needed."

**Follow-up: Did you use Celery?**

"We used background processing for some tasks, but in the Neighborshook project the main moderation was handled through a separate NLP service. In my automation projects I used Celery-style async patterns where needed."

---

**Q6. What challenges did you face in the moderation project?**

"One challenge was balancing response time with moderation accuracy. Transformer models can be slow if called synchronously. We had to optimize the flow — sometimes using lighter models like DistilBERT instead of full BERT — and handle API failures gracefully. We also had to deal with false positives and false negatives, so we combined AI output with rule-based checks and manual review."

**Follow-up: How did you handle failures?**

"We implemented exception handling, logging, and marked content for manual review if automated moderation couldn't complete. We also added retries for transient failures."

---

**Q7. What did you optimize in that project?**

"I optimized database queries, reduced unnecessary ORM calls, used pagination for feeds, added indexes on frequently queried columns, and moved heavy NLP processing out of the main request cycle."

---

**Q8. Why Python instead of PHP?**

"PHP gave me a solid backend foundation — Laravel, WordPress, Drupal. But Python provides cleaner syntax, a stronger ecosystem for automation, APIs, and AI. As my work shifted towards Django, FastAPI, NLP, and automation, Python became my primary language. I still use PHP/Laravel when the project requires it."

---

**Q9. Tell me about your Wipro project.**

"Actually, I'm currently working as a freelance Software Engineer, not at Wipro. I build Python automation tools that collect journal and publication data. Depending on the website, I use BeautifulSoup or Selenium, clean the data with Pandas, generate Excel reports with OpenPyXL, and package desktop tools using PyInstaller and Tkinter."

**Follow-up: Why both Selenium and BeautifulSoup?**

"BeautifulSoup is efficient for static HTML. Selenium is needed when content is rendered dynamically through JavaScript."

---

**Q10. Why Tkinter?**

"Many end users weren't technical. A desktop interface made the automation tool easier to use than asking users to run Python scripts from the command line."

---

**Q11. How did you package the application?**

"I used PyInstaller to package the application as a standalone Windows executable so users didn't need to install Python separately."

---

**Q12. Which backend framework do you prefer?**

"For large business applications with authentication, admin features, and ORM support, I prefer Django. For lightweight API services, FastAPI is also a good option. For rapid prototyping, Flask works well."

---

**Q13. What is your biggest strength?**

"I enjoy understanding business problems and converting them into reliable backend solutions. I'm also comfortable learning new technologies when a project requires them — like I learned Hugging Face Transformers and NLP for the moderation project."

---

**Q14. What is your weakness?**

"Earlier I used to spend too much time trying to perfect an implementation. Over time, I've learned to balance quality with delivery timelines by prioritizing business requirements first."

---

**Q15. Tell me about a production issue.**

"We experienced slower API responses because some requests involved long-running NLP processing. We analyzed the flow, identified that the work didn't need to be synchronous, and moved it to background processing. That improved responsiveness."

---

**Q16. How do you debug problems?**

"I first reproduce the issue, review logs, check API responses, inspect database queries, isolate the failing component, and then verify the fix in a test environment before deployment."

---

**Q17. Why should we hire you?**

"I have hands-on experience in backend development with Python, Django, Laravel, REST APIs, MySQL, and practical AI integration using Hugging Face Transformers. I've worked on production systems, automation, and NLP-based moderation. I'm comfortable taking ownership of backend features from development through deployment."

---

**Q18. Do you have any questions for us?**

"Yes. I'd like to know more about the team's current backend architecture, the technologies used in production, and what the expectations are for someone joining this role in the first three to six months."

---

[← Back to Index](README.md) | [Next: Module 2 →](module-2-python-core.md)
