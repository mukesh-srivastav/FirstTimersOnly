import tkinter as tk
from tkinter import ttk, messagebox
import random

# ============================================================
# CURRENT AFFAIRS MCQ QUIZ
# Single-file Python application
# 100-question question bank
# ============================================================

QUESTIONS = [

    # -------------------- INDIA / POLITY --------------------

    {
        "q": "Who is the President of India in 2026?",
        "options": ["Droupadi Murmu", "Pratibha Patil", "Ram Nath Kovind", "Nirmala Sitharaman"],
        "answer": 0
    },
    {
        "q": "Who is the Prime Minister of India in 2026?",
        "options": ["Narendra Modi", "Amit Shah", "Rajnath Singh", "S. Jaishankar"],
        "answer": 0
    },
    {
        "q": "The National Dental Commission replaced which body in 2026?",
        "options": [
            "Dental Council of India",
            "Medical Council of India",
            "National Medical Commission",
            "Indian Nursing Council"
        ],
        "answer": 0
    },
    {
        "q": "The National Dental Commission is primarily related to which field?",
        "options": ["Dental education and regulation", "Banking", "Agriculture", "Railways"],
        "answer": 0
    },
    {
        "q": "Which city hosted the 2025 Maha Kumbh?",
        "options": ["Prayagraj", "Varanasi", "Haridwar", "Ujjain"],
        "answer": 0
    },
    {
        "q": "The Maha Kumbh 2025 was held in which Indian state?",
        "options": ["Uttar Pradesh", "Bihar", "Madhya Pradesh", "Rajasthan"],
        "answer": 0
    },
    {
        "q": "Which ministry is primarily responsible for India's national highways?",
        "options": [
            "Ministry of Road Transport and Highways",
            "Ministry of Railways",
            "Ministry of Commerce",
            "Ministry of Heavy Industries"
        ],
        "answer": 0
    },
    {
        "q": "PM GatiShakti is primarily associated with what?",
        "options": [
            "Multimodal infrastructure planning",
            "Healthcare insurance",
            "School education",
            "Banking regulation"
        ],
        "answer": 0
    },
    {
        "q": "Which body approves major economic infrastructure proposals of the Union Government?",
        "options": [
            "Cabinet Committee on Economic Affairs",
            "Election Commission",
            "UPSC",
            "Finance Commission"
        ],
        "answer": 0
    },
    {
        "q": "Which institution conducts India's general elections?",
        "options": [
            "Election Commission of India",
            "Supreme Court",
            "Parliament",
            "NITI Aayog"
        ],
        "answer": 0
    },

    # -------------------- ECONOMY --------------------

    {
        "q": "Which institution is India's central bank?",
        "options": [
            "Reserve Bank of India",
            "State Bank of India",
            "SEBI",
            "NABARD"
        ],
        "answer": 0
    },
    {
        "q": "What does RBI stand for?",
        "options": [
            "Reserve Bank of India",
            "Regional Bank of India",
            "Revenue Bank of India",
            "Rural Banking Institution"
        ],
        "answer": 0
    },
    {
        "q": "Which institution regulates India's securities market?",
        "options": ["SEBI", "RBI", "IRDAI", "PFRDA"],
        "answer": 0
    },
    {
        "q": "What does SEBI stand for?",
        "options": [
            "Securities and Exchange Board of India",
            "Stock Exchange Banking Institution",
            "Securities Economic Banking Institute",
            "State Exchange Board of India"
        ],
        "answer": 0
    },
    {
        "q": "UPI is primarily used for what?",
        "options": [
            "Digital payments",
            "Passport verification",
            "Satellite communication",
            "Railway signalling"
        ],
        "answer": 0
    },
    {
        "q": "UPI was developed by which organization?",
        "options": [
            "NPCI",
            "SEBI",
            "ISRO",
            "DRDO"
        ],
        "answer": 0
    },
    {
        "q": "What does NPCI stand for?",
        "options": [
            "National Payments Corporation of India",
            "National Public Credit Institution",
            "National Payment Council of India",
            "New Payments Corporation of India"
        ],
        "answer": 0
    },
    {
        "q": "Which organization operates India's RuPay card network?",
        "options": ["NPCI", "RBI", "SEBI", "IRDAI"],
        "answer": 0
    },
    {
        "q": "GST is primarily a tax on what?",
        "options": [
            "Goods and services",
            "Only agricultural land",
            "Only imports",
            "Only salaries"
        ],
        "answer": 0
    },
    {
        "q": "GST stands for what?",
        "options": [
            "Goods and Services Tax",
            "General Sales Tax",
            "Government Services Tariff",
            "Goods Supply Tariff"
        ],
        "answer": 0
    },

    # -------------------- SCIENCE / TECHNOLOGY --------------------

    {
        "q": "Which organization is India's primary space agency?",
        "options": ["ISRO", "DRDO", "CSIR", "BARC"],
        "answer": 0
    },
    {
        "q": "What does ISRO stand for?",
        "options": [
            "Indian Space Research Organisation",
            "Indian Satellite Research Organisation",
            "International Space Research Organisation",
            "Indian Scientific Research Office"
        ],
        "answer": 0
    },
    {
        "q": "What does AI stand for?",
        "options": [
            "Artificial Intelligence",
            "Automated Internet",
            "Advanced Information",
            "Artificial Internet"
        ],
        "answer": 0
    },
    {
        "q": "Tathyakosh is primarily designed for what purpose?",
        "options": [
            "Discovering public datasets",
            "Online banking",
            "Railway ticket booking",
            "Online voting"
        ],
        "answer": 0
    },
    {
        "q": "Tathyakosh was launched in August 2026 by which state's IT-BT minister?",
        "options": ["Karnataka", "Maharashtra", "Tamil Nadu", "Gujarat"],
        "answer": 0
    },
    {
        "q": "Tathyakosh aims to make what easier?",
        "options": [
            "Discovery and use of public data",
            "International travel",
            "Online shopping",
            "Stock trading"
        ],
        "answer": 0
    },
    {
        "q": "According to reports, Tathyakosh catalogues data from approximately how many sources?",
        "options": ["458", "58", "4,580", "45"],
        "answer": 0
    },
    {
        "q": "Tathyakosh focuses heavily on which technology-related objective?",
        "options": [
            "Supporting AI development and research",
            "Replacing satellites",
            "Manufacturing automobiles",
            "Cryptocurrency mining"
        ],
        "answer": 0
    },
    {
        "q": "Which organization is India's defence research agency?",
        "options": ["DRDO", "ISRO", "NPCI", "SEBI"],
        "answer": 0
    },
    {
        "q": "What does DRDO stand for?",
        "options": [
            "Defence Research and Development Organisation",
            "Department of Research and Defence Operations",
            "Defence Research Development Office",
            "Digital Research and Defence Organisation"
        ],
        "answer": 0
    },

    # -------------------- ENVIRONMENT --------------------

    {
        "q": "Which gas is the largest contributor to human-caused global warming?",
        "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Helium"],
        "answer": 0
    },
    {
        "q": "What does COP generally refer to in climate negotiations?",
        "options": [
            "Conference of the Parties",
            "Council of Pollution",
            "Climate Operations Programme",
            "Conference of Pollution"
        ],
        "answer": 0
    },
    {
        "q": "The Paris Agreement primarily addresses what?",
        "options": [
            "Climate change",
            "International trade",
            "Nuclear weapons",
            "Global banking"
        ],
        "answer": 0
    },
    {
        "q": "Which organization publishes major global climate assessments?",
        "options": [
            "IPCC",
            "WTO",
            "IMF",
            "ILO"
        ],
        "answer": 0
    },
    {
        "q": "What does IPCC stand for?",
        "options": [
            "Intergovernmental Panel on Climate Change",
            "International Panel for Carbon Control",
            "Indian Panel on Climate Change",
            "International Pollution Control Council"
        ],
        "answer": 0
    },
    {
        "q": "Which renewable energy source uses sunlight to generate electricity?",
        "options": ["Solar energy", "Geothermal energy", "Tidal energy", "Biomass"],
        "answer": 0
    },
    {
        "q": "Which renewable source uses wind turbines?",
        "options": ["Wind energy", "Solar energy", "Hydrogen energy", "Geothermal energy"],
        "answer": 0
    },
    {
        "q": "What is biodiversity?",
        "options": [
            "Variety of life",
            "Amount of rainfall",
            "Amount of carbon dioxide",
            "Ocean temperature"
        ],
        "answer": 0
    },
    {
        "q": "The Nagoya Protocol is associated mainly with what?",
        "options": [
            "Access and benefit-sharing of genetic resources",
            "Nuclear energy",
            "International banking",
            "Maritime security"
        ],
        "answer": 0
    },
    {
        "q": "Which international convention is strongly associated with biodiversity conservation?",
        "options": [
            "Convention on Biological Diversity",
            "Geneva Convention",
            "Chicago Convention",
            "Vienna Convention on Road Traffic"
        ],
        "answer": 0
    },

    # -------------------- INTERNATIONAL --------------------

    {
        "q": "Which organization is headquartered in New York and deals with global peace and security?",
        "options": ["United Nations", "WTO", "IMF", "WHO"],
        "answer": 0
    },
    {
        "q": "What does UN stand for?",
        "options": [
            "United Nations",
            "Universal Nations",
            "United Network",
            "Union of Nations"
        ],
        "answer": 0
    },
    {
        "q": "Which organization is responsible for international public health coordination?",
        "options": ["WHO", "WTO", "IMF", "UNESCO"],
        "answer": 0
    },
    {
        "q": "What does WHO stand for?",
        "options": [
            "World Health Organization",
            "World Human Organization",
            "World Healthcare Office",
            "World Health Office"
        ],
        "answer": 0
    },
    {
        "q": "Which institution is primarily concerned with international monetary cooperation?",
        "options": ["IMF", "WHO", "UNESCO", "WTO"],
        "answer": 0
    },
    {
        "q": "What does IMF stand for?",
        "options": [
            "International Monetary Fund",
            "International Market Federation",
            "Indian Monetary Fund",
            "International Money Forum"
        ],
        "answer": 0
    },
    {
        "q": "Which organization deals primarily with global trade rules?",
        "options": ["WTO", "WHO", "IMF", "UNICEF"],
        "answer": 0
    },
    {
        "q": "What does WTO stand for?",
        "options": [
            "World Trade Organization",
            "World Transport Organization",
            "World Technology Organization",
            "World Tariff Organization"
        ],
        "answer": 0
    },
    {
        "q": "The Quad consists of India, Australia, Japan and which country?",
        "options": ["United States", "United Kingdom", "France", "Germany"],
        "answer": 0
    },
    {
        "q": "The Quad is primarily associated with cooperation in which region?",
        "options": [
            "Indo-Pacific",
            "Arctic",
            "South Atlantic",
            "Mediterranean"
        ],
        "answer": 0
    },

    # -------------------- SPORTS --------------------

    {
        "q": "Where are the 2026 BWF World Championships scheduled to be held?",
        "options": ["New Delhi", "Mumbai", "Bengaluru", "Hyderabad"],
        "answer": 0
    },
    {
        "q": "The 2026 BWF World Championships are scheduled at which venue?",
        "options": [
            "Indira Gandhi Indoor Stadium",
            "Jawaharlal Nehru Stadium",
            "Major Dhyan Chand Stadium",
            "Wankhede Stadium"
        ],
        "answer": 0
    },
    {
        "q": "The 2026 BWF World Championships are scheduled for which dates?",
        "options": [
            "17–23 August",
            "1–7 August",
            "25–31 August",
            "10–16 September"
        ],
        "answer": 0
    },
    {
        "q": "Which Indian badminton player is associated with the 2026 BWF World Championships?",
        "options": ["Lakshya Sen", "Sunil Gavaskar", "Neeraj Chopra", "Viswanathan Anand"],
        "answer": 0
    },
    {
        "q": "Which Indian badminton star is also expected to compete at the 2026 BWF World Championships?",
        "options": ["PV Sindhu", "Mary Kom", "Hima Das", "Sakshi Malik"],
        "answer": 0
    },
    {
        "q": "The BWF World Championships are associated with which sport?",
        "options": ["Badminton", "Basketball", "Boxing", "Wrestling"],
        "answer": 0
    },
    {
        "q": "The 2026 Commonwealth Games were held in which city?",
        "options": ["Glasgow", "London", "Delhi", "Melbourne"],
        "answer": 0
    },
    {
        "q": "Which Indian athlete won India's first gold medal at the 2026 Commonwealth Games according to PIB?",
        "options": ["Mirabai Chanu", "PV Sindhu", "Neeraj Chopra", "Lovlina Borgohain"],
        "answer": 0
    },
    {
        "q": "Mirabai Chanu is associated with which sport?",
        "options": ["Weightlifting", "Badminton", "Boxing", "Athletics"],
        "answer": 0
    },
    {
        "q": "The 2026 Commonwealth Games were scheduled from July 23 to which date?",
        "options": ["August 2", "August 15", "July 30", "August 10"],
        "answer": 0
    },

    # -------------------- CRICKET --------------------

    {
        "q": "India's national cricket governing body is known as what?",
        "options": ["BCCI", "ICC", "CAB", "NCA"],
        "answer": 0
    },
    {
        "q": "What does BCCI stand for?",
        "options": [
            "Board of Control for Cricket in India",
            "Board of Cricket Council of India",
            "British Cricket Council of India",
            "Board for Competitive Cricket in India"
        ],
        "answer": 0
    },
    {
        "q": "Which international organization governs global cricket?",
        "options": ["ICC", "BCCI", "FIFA", "IOC"],
        "answer": 0
    },
    {
        "q": "What does ICC stand for in cricket?",
        "options": [
            "International Cricket Council",
            "Indian Cricket Council",
            "International Championship Committee",
            "International Cricket Committee"
        ],
        "answer": 0
    },
    {
        "q": "India and Afghanistan announced a three-match T20I series for September 2026. Where is it scheduled?",
        "options": [
            "Delhi",
            "Mumbai",
            "Kolkata",
            "Chennai"
        ],
        "answer": 0
    },
    {
        "q": "Which stadium is scheduled to host the India-Afghanistan T20Is in September 2026?",
        "options": [
            "Arun Jaitley Cricket Stadium",
            "Wankhede Stadium",
            "Eden Gardens",
            "M. Chinnaswamy Stadium"
        ],
        "answer": 0
    },
    {
        "q": "The India-Afghanistan T20I series is scheduled immediately before which major multi-sport event?",
        "options": ["Asian Games", "Olympics", "Commonwealth Games", "Asian Cup"],
        "answer": 0
    },
    {
        "q": "T20 cricket consists of how many overs per side?",
        "options": ["20", "10", "25", "50"],
        "answer": 0
    },
    {
        "q": "Which format normally has 50 overs per side?",
        "options": ["ODI", "T20", "Test", "The Hundred"],
        "answer": 0
    },
    {
        "q": "A Test cricket match can last for a maximum of how many days?",
        "options": ["5", "3", "4", "7"],
        "answer": 0
    },

    # -------------------- DIGITAL INDIA / TECH --------------------

    {
        "q": "Which Indian system enables instant bank-to-bank digital payments using mobile apps?",
        "options": ["UPI", "PAN", "GST", "FASTag"],
        "answer": 0
    },
    {
        "q": "FASTag is primarily used for what?",
        "options": ["Electronic toll collection", "Income tax", "Passport services", "Train booking"],
        "answer": 0
    },
    {
        "q": "DigiLocker is mainly used for what?",
        "options": [
            "Digital storage and verification of documents",
            "Online gaming",
            "Stock trading",
            "Weather forecasting"
        ],
        "answer": 0
    },
    {
        "q": "Aadhaar is issued by which organization?",
        "options": ["UIDAI", "RBI", "SEBI", "NPCI"],
        "answer": 0
    },
    {
        "q": "What does UIDAI stand for?",
        "options": [
            "Unique Identification Authority of India",
            "Universal Identification Authority of India",
            "United Identity Agency of India",
            "Unique Indian Digital Authority"
        ],
        "answer": 0
    },
    {
        "q": "Which technology is central to many modern generative AI systems?",
        "options": [
            "Large language models",
            "Fax machines",
            "CRT displays",
            "Analog radios"
        ],
        "answer": 0
    },
    {
        "q": "What does LLM stand for in AI?",
        "options": [
            "Large Language Model",
            "Long Learning Machine",
            "Logical Language Machine",
            "Large Logic Module"
        ],
        "answer": 0
    },
    {
        "q": "Which technology is used to create an immutable distributed ledger?",
        "options": ["Blockchain", "Bluetooth", "HTML", "JPEG"],
        "answer": 0
    },
    {
        "q": "Cybersecurity primarily deals with protecting what?",
        "options": [
            "Digital systems and information",
            "Roads",
            "Agricultural land",
            "Buildings only"
        ],
        "answer": 0
    },
    {
        "q": "What is IoT?",
        "options": [
            "Internet of Things",
            "Internet of Technology",
            "Integrated Online Technology",
            "International Object Transfer"
        ],
        "answer": 0
    },

    # -------------------- EDUCATION / SOCIAL --------------------

    {
        "q": "Which policy introduced major reforms in India's education system in 2020?",
        "options": [
            "National Education Policy",
            "National Skill Policy 2009",
            "Education Reform Act 2015",
            "Digital Education Act"
        ],
        "answer": 0
    },
    {
        "q": "What is the short form of National Education Policy 2020?",
        "options": ["NEP 2020", "NEP 2019", "NPE 2020", "NEA 2020"],
        "answer": 0
    },
    {
        "q": "Which organization is India's apex body for technical education?",
        "options": ["AICTE", "UGC", "NCERT", "CBSE"],
        "answer": 0
    },
    {
        "q": "What does AICTE stand for?",
        "options": [
            "All India Council for Technical Education",
            "All India Committee for Technical Education",
            "Advanced Indian Council of Technical Education",
            "All India Centre for Technology Education"
        ],
        "answer": 0
    },
    {
        "q": "Which organization coordinates university education in India?",
        "options": ["UGC", "AICTE", "CBSE", "NTA"],
        "answer": 0
    },
    {
        "q": "What does UGC stand for?",
        "options": [
            "University Grants Commission",
            "University Governance Council",
            "Union Grants Council",
            "University Government Commission"
        ],
        "answer": 0
    },
    {
        "q": "Which organization conducts JEE Main?",
        "options": [
            "National Testing Agency",
            "UPSC",
            "UGC",
            "AICTE"
        ],
        "answer": 0
    },
    {
        "q": "What does NTA stand for?",
        "options": [
            "National Testing Agency",
            "National Training Authority",
            "National Technology Agency",
            "National Teaching Authority"
        ],
        "answer": 0
    },
    {
        "q": "Which body conducts UPSC Civil Services Examination?",
        "options": [
            "Union Public Service Commission",
            "Staff Selection Commission",
            "National Testing Agency",
            "Election Commission"
        ],
        "answer": 0
    },
    {
        "q": "What does UPSC stand for?",
        "options": [
            "Union Public Service Commission",
            "United Public Service Council",
            "Union Professional Selection Commission",
            "Universal Public Service Commission"
        ],
        "answer": 0
    },

    # -------------------- GOVERNMENT SCHEMES --------------------

    {
        "q": "PM Jan Dhan Yojana primarily aims at what?",
        "options": [
            "Financial inclusion",
            "Space research",
            "Road construction",
            "Defence production"
        ],
        "answer": 0
    },
    {
        "q": "PM-KISAN is primarily aimed at supporting whom?",
        "options": ["Farmers", "Students", "Scientists", "Government employees"],
        "answer": 0
    },
    {
        "q": "Ayushman Bharat is primarily associated with which sector?",
        "options": ["Healthcare", "Education", "Transport", "Defence"],
        "answer": 0
    },
    {
        "q": "Startup India is primarily intended to encourage what?",
        "options": [
            "Entrepreneurship and startups",
            "Military recruitment",
            "Railway expansion",
            "Forest conservation"
        ],
        "answer": 0
    },
    {
        "q": "Skill India primarily focuses on what?",
        "options": [
            "Skill development",
            "Tax collection",
            "Space exploration",
            "Wildlife protection"
        ],
        "answer": 0
    },
    {
        "q": "Digital India primarily aims to transform India through what?",
        "options": [
            "Digital technologies and services",
            "Only agriculture",
            "Only defence",
            "Only tourism"
        ],
        "answer": 0
    },
    {
        "q": "Make in India primarily promotes what?",
        "options": [
            "Manufacturing in India",
            "Foreign tourism",
            "Online education",
            "Sports training"
        ],
        "answer": 0
    },
    {
        "q": "Which scheme is associated with affordable housing?",
        "options": [
            "Pradhan Mantri Awas Yojana",
            "PM-KISAN",
            "PM Jan Dhan Yojana",
            "Skill India"
        ],
        "answer": 0
    },
    {
        "q": "Swachh Bharat Mission primarily focuses on what?",
        "options": [
            "Sanitation and cleanliness",
            "Digital payments",
            "Defence",
            "Space exploration"
        ],
        "answer": 0
    },
    {
        "q": "Jal Jeevan Mission primarily focuses on providing what?",
        "options": [
            "Tap water connections",
            "Free electricity",
            "Free internet",
            "Housing loans"
        ],
        "answer": 0
    },

    # -------------------- AWARDS / CULTURE --------------------

    {
        "q": "Which is India's highest civilian award?",
        "options": ["Bharat Ratna", "Padma Vibhushan", "Padma Bhushan", "Padma Shri"],
        "answer": 0
    },
    {
        "q": "Which is India's second-highest civilian award?",
        "options": ["Padma Vibhushan", "Bharat Ratna", "Padma Bhushan", "Padma Shri"],
        "answer": 0
    },
    {
        "q": "Which award is given for exceptional contributions in various fields and is one of India's major civilian honours?",
        "options": ["Padma Shri", "Arjuna Award", "Dronacharya Award", "Khel Ratna"],
        "answer": 0
    },
    {
        "q": "The Arjuna Award is primarily associated with which field?",
        "options": ["Sports", "Literature", "Science", "Cinema"],
        "answer": 0
    },
    {
        "q": "The Dronacharya Award is mainly given to whom?",
        "options": [
            "Sports coaches",
            "Scientists",
            "Actors",
            "Journalists"
        ],
        "answer": 0
    },
    {
        "q": "The Nobel Prize is awarded in how many traditional categories?",
        "options": ["Six", "Four", "Five", "Eight"],
        "answer": 0
    },
    {
        "q": "The Oscar Awards are primarily associated with which industry?",
        "options": ["Cinema", "Sports", "Literature", "Science"],
        "answer": 0
    },
    {
        "q": "The Grammy Awards are primarily associated with what?",
        "options": ["Music", "Cinema", "Literature", "Science"],
        "answer": 0
    },
    {
        "q": "The Booker Prize is primarily associated with which field?",
        "options": ["Literature", "Physics", "Sports", "Economics"],
        "answer": 0
    },
    {
        "q": "The Jnanpith Award is associated with which field?",
        "options": ["Literature", "Sports", "Medicine", "Engineering"],
        "answer": 0
    },

    # -------------------- MIXED CURRENT AFFAIRS / GK --------------------

    {
        "q": "Which Indian city is known as the headquarters of ISRO?",
        "options": ["Bengaluru", "New Delhi", "Mumbai", "Hyderabad"],
        "answer": 0
    },
    {
        "q": "Which city is the headquarters of the Reserve Bank of India?",
        "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
        "answer": 0
    },
    {
        "q": "Which city hosts India's Parliament?",
        "options": ["New Delhi", "Mumbai", "Kolkata", "Bengaluru"],
        "answer": 0
    },
    {
        "q": "Which Indian state launched Tathyakosh according to August 2026 reports?",
        "options": ["Karnataka", "Kerala", "Maharashtra", "Punjab"],
        "answer": 0
    },
    {
        "q": "Which sport uses a shuttlecock?",
        "options": ["Badminton", "Tennis", "Table tennis", "Squash"],
        "answer": 0
    },
    {
        "q": "Which Indian athlete is famous for Olympic javelin success?",
        "options": ["Neeraj Chopra", "Lakshya Sen", "Mirabai Chanu", "Rohit Sharma"],
        "answer": 0
    },
    {
        "q": "Which sport is Neeraj Chopra associated with?",
        "options": ["Javelin throw", "Weightlifting", "Badminton", "Boxing"],
        "answer": 0
    },
    {
        "q": "Which sport is Mirabai Chanu associated with?",
        "options": ["Weightlifting", "Javelin", "Wrestling", "Badminton"],
        "answer": 0
    },
    {
        "q": "Which Indian player became a major international chess champion at a young age?",
        "options": ["D. Gukesh", "Ravichandran Ashwin", "Lakshya Sen", "Shubman Gill"],
        "answer": 0
    },
    {
        "q": "D. Gukesh is associated with which sport?",
        "options": ["Chess", "Cricket", "Badminton", "Wrestling"],
        "answer": 0
    },

    # -------------------- MORE CURRENT AFFAIRS --------------------

    {
        "q": "Which city is hosting the 2026 BWF World Championships in India?",
        "options": ["New Delhi", "Pune", "Jaipur", "Lucknow"],
        "answer": 0
    },
    {
        "q": "The 2026 BWF World Championships represent the return of the event to India after approximately how many years?",
        "options": ["17 years", "10 years", "5 years", "25 years"],
        "answer": 0
    },
    {
        "q": "Which of these players is a former badminton world champion and Olympic medallist from India?",
        "options": ["PV Sindhu", "Rohit Sharma", "Neeraj Chopra", "D. Gukesh"],
        "answer": 0
    },
    {
        "q": "Which Indian badminton player is known for winning a Commonwealth Games gold medal in men's singles?",
        "options": ["Lakshya Sen", "Virat Kohli", "Neeraj Chopra", "D. Gukesh"],
        "answer": 0
    },
    {
        "q": "What type of datasets does Tathyakosh help users discover?",
        "options": [
            "Public datasets",
            "Private bank passwords",
            "Personal medical records",
            "Private social media messages"
        ],
        "answer": 0
    },
    {
        "q": "According to August 2026 reports, Tathyakosh catalogues more than how many datasets?",
        "options": ["1.5 million", "15,000", "150,000", "15 million"],
        "answer": 0
    },
    {
        "q": "Tathyakosh is described as what kind of digital public good?",
        "options": [
            "Open and non-commercial",
            "Private and subscription-only",
            "Cryptocurrency-based",
            "Military-only"
        ],
        "answer": 0
    },
    {
        "q": "Which sector is specifically mentioned as one of the domains covered by Tathyakosh?",
        "options": ["Agriculture", "Only entertainment", "Only sports", "Only banking"],
        "answer": 0
    },
    {
        "q": "Which country is NOT a member of the Quad?",
        "options": ["Germany", "India", "Japan", "Australia"],
        "answer": 0
    },
    {
        "q": "Which country is a member of the Quad?",
        "options": ["Japan", "Germany", "Russia", "Brazil"],
        "answer": 0
    },

    # -------------------- FINAL 10 --------------------

    {
        "q": "Which institution publishes India's monetary policy decisions?",
        "options": ["RBI", "SEBI", "NITI Aayog", "UPSC"],
        "answer": 0
    },
    {
        "q": "Which body replaced the Planning Commission?",
        "options": ["NITI Aayog", "Finance Commission", "SEBI", "RBI"],
        "answer": 0
    },
    {
        "q": "NITI Aayog is primarily a government think tank of which country?",
        "options": ["India", "Japan", "United States", "Australia"],
        "answer": 0
    },
    {
        "q": "Which ministry is responsible for India's external affairs?",
        "options": [
            "Ministry of External Affairs",
            "Ministry of Home Affairs",
            "Ministry of Defence",
            "Ministry of Finance"
        ],
        "answer": 0
    },
    {
        "q": "Which ministry handles India's internal security at the Union level?",
        "options": [
            "Ministry of Home Affairs",
            "Ministry of External Affairs",
            "Ministry of Finance",
            "Ministry of Education"
        ],
        "answer": 0
    },
    {
        "q": "Which Indian organization is responsible for atomic energy research?",
        "options": ["Department of Atomic Energy", "NPCI", "SEBI", "AICTE"],
        "answer": 0
    },
    {
        "q": "BARC is primarily associated with which field?",
        "options": [
            "Nuclear research",
            "Banking",
            "Sports",
            "Agriculture"
        ],
        "answer": 0
    },
    {
        "q": "Which Indian organization is responsible for weather forecasting?",
        "options": [
            "India Meteorological Department",
            "ISRO",
            "DRDO",
            "NITI Aayog"
        ],
        "answer": 0
    },
    {
        "q": "What does IMD stand for?",
        "options": [
            "India Meteorological Department",
            "Indian Medical Department",
            "International Meteorological Division",
            "Indian Meteorology Directorate"
        ],
        "answer": 0
    },
    {
        "q": "Which field is strongly represented in the current affairs trend of 2026?",
        "options": [
            "Science and technology",
            "Only ancient history",
            "Only classical music",
            "Only geography"
        ],
        "answer": 0
    }
]


# ============================================================
# QUIZ APPLICATION
# ============================================================

class QuizApp:

    def __init__(self, root):
        self.root = root

        self.root.title("2026 Current Affairs MCQ Quiz")
        self.root.geometry("1050x700")
        self.root.minsize(900, 600)
        self.root.configure(bg="#121212")

        # Colors
        self.bg = "#121212"
        self.card = "#1e1e1e"
        self.card2 = "#252525"
        self.text = "#f5f5f5"
        self.secondary = "#aaaaaa"
        self.accent = "#00d4ff"
        self.green = "#00e676"
        self.red = "#ff5252"
        self.yellow = "#ffd740"

        # Quiz variables
        self.questions = []
        self.current = 0
        self.score = 0
        self.user_answers = []
        self.option_buttons = []

        self.setup_style()
        self.create_header()
        self.create_main_area()

        self.start_quiz()

    # --------------------------------------------------------
    # STYLE
    # --------------------------------------------------------

    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Dark.Horizontal.TProgressbar",
            troughcolor="#303030",
            background=self.accent,
            bordercolor="#303030",
            lightcolor=self.accent,
            darkcolor=self.accent
        )

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    def create_header(self):

        self.header = tk.Frame(
            self.root,
            bg="#181818",
            height=80
        )

        self.header.pack(
            fill="x",
            side="top"
        )

        title = tk.Label(
            self.header,
            text="CURRENT AFFAIRS QUIZ",
            font=("Arial", 22, "bold"),
            fg=self.accent,
            bg="#181818"
        )

        title.pack(
            side="left",
            padx=30,
            pady=20
        )

        self.score_label = tk.Label(
            self.header,
            text="Score: 0",
            font=("Arial", 14, "bold"),
            fg=self.green,
            bg="#181818"
        )

        self.score_label.pack(
            side="right",
            padx=30
        )

    # --------------------------------------------------------
    # MAIN AREA
    # --------------------------------------------------------

    def create_main_area(self):

        self.main = tk.Frame(
            self.root,
            bg=self.bg
        )

        self.main.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=25
        )

        # Question number
        self.question_number = tk.Label(
            self.main,
            text="Question 1 / 100",
            font=("Arial", 13, "bold"),
            fg=self.secondary,
            bg=self.bg
        )

        self.question_number.pack(
            anchor="w"
        )

        # Progress
        self.progress = ttk.Progressbar(
            self.main,
            style="Dark.Horizontal.TProgressbar",
            orient="horizontal",
            length=900,
            mode="determinate"
        )

        self.progress.pack(
            fill="x",
            pady=(8, 25)
        )

        # Question card
        self.question_card = tk.Frame(
            self.main,
            bg=self.card,
            bd=0
        )

        self.question_card.pack(
            fill="x",
            pady=5
        )

        self.question_label = tk.Label(
            self.question_card,
            text="",
            font=("Arial", 18, "bold"),
            fg=self.text,
            bg=self.card,
            wraplength=850,
            justify="left"
        )

        self.question_label.pack(
            anchor="w",
            padx=25,
            pady=25
        )

        # Options
        self.options_frame = tk.Frame(
            self.main,
            bg=self.bg
        )

        self.options_frame.pack(
            fill="both",
            expand=True,
            pady=15
        )

        for i in range(4):

            btn = tk.Button(
                self.options_frame,
                text="",
                font=("Arial", 13),
                fg=self.text,
                bg=self.card2,
                activeforeground=self.text,
                activebackground="#333333",
                relief="flat",
                bd=0,
                cursor="hand2",
                anchor="w",
                padx=20,
                pady=15,
                command=lambda index=i: self.select_answer(index)
            )

            btn.pack(
                fill="x",
                pady=6
            )

            self.option_buttons.append(btn)

        # Bottom controls
        self.bottom = tk.Frame(
            self.main,
            bg=self.bg
        )

        self.bottom.pack(
            fill="x",
            pady=10
        )

        self.prev_button = tk.Button(
            self.bottom,
            text="← Previous",
            font=("Arial", 12, "bold"),
            fg=self.text,
            bg="#333333",
            activebackground="#444444",
            activeforeground=self.text,
            relief="flat",
            padx=20,
            pady=10,
            command=self.previous_question
        )

        self.prev_button.pack(
            side="left"
        )

        self.next_button = tk.Button(
            self.bottom,
            text="Next →",
            font=("Arial", 12, "bold"),
            fg="#000000",
            bg=self.accent,
            activebackground="#00a8cc",
            relief="flat",
            padx=25,
            pady=10,
            command=self.next_question
        )

        self.next_button.pack(
            side="right"
        )

    # --------------------------------------------------------
    # START QUIZ
    # --------------------------------------------------------

    def start_quiz(self):

        # Make a copy so original question bank isn't modified
        self.questions = [dict(q) for q in QUESTIONS]

        # Shuffle questions
        random.shuffle(self.questions)

        # Shuffle options for every question
        for q in self.questions:

            correct_answer = q["options"][q["answer"]]

            options = q["options"][:]

            random.shuffle(options)

            q["options"] = options

            q["answer"] = options.index(correct_answer)

        self.current = 0
        self.score = 0

        self.user_answers = [
            None
            for _ in self.questions
        ]

        self.score_label.config(
            text="Score: 0"
        )

        self.show_question()

    # --------------------------------------------------------
    # SHOW QUESTION
    # --------------------------------------------------------

    def show_question(self):

        if self.current >= len(self.questions):
            self.show_result()
            return

        q = self.questions[self.current]

        self.question_number.config(
            text=f"Question {self.current + 1} / {len(self.questions)}"
        )

        self.progress["value"] = (
            (self.current + 1) /
            len(self.questions)
        ) * 100

        self.question_label.config(
            text=q["q"]
        )

        # Reset option buttons
        for i, btn in enumerate(self.option_buttons):

            btn.config(
                text=f"{chr(65 + i)}. {q['options'][i]}",
                bg=self.card2,
                fg=self.text,
                state="normal"
            )

        # If already answered
        if self.user_answers[self.current] is not None:

            selected = self.user_answers[self.current]

            self.option_buttons[selected].config(
                bg="#005f73"
            )

        # Previous button
        if self.current == 0:
            self.prev_button.config(
                state="disabled",
                bg="#222222",
                fg="#666666"
            )
        else:
            self.prev_button.config(
                state="normal",
                bg="#333333",
                fg=self.text
            )

        # Last question
        if self.current == len(self.questions) - 1:

            self.next_button.config(
                text="Finish ✓"
            )

        else:

            self.next_button.config(
                text="Next →"
            )

    # --------------------------------------------------------
    # SELECT ANSWER
    # --------------------------------------------------------

    def select_answer(self, index):

        self.user_answers[self.current] = index

        for btn in self.option_buttons:

            btn.config(
                bg=self.card2
            )

        self.option_buttons[index].config(
            bg="#005f73"
        )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    def next_question(self):

        if self.user_answers[self.current] is None:

            messagebox.showwarning(
                "Select an answer",
                "Please select an answer before continuing."
            )

            return

        self.current += 1

        if self.current >= len(self.questions):

            self.calculate_score()

            self.show_result()

        else:

            self.show_question()

    # --------------------------------------------------------
    # PREVIOUS QUESTION
    # --------------------------------------------------------

    def previous_question(self):

        if self.current > 0:

            self.current -= 1

            self.show_question()

    # --------------------------------------------------------
    # CALCULATE SCORE
    # --------------------------------------------------------

    def calculate_score(self):

        self.score = 0

        for i, q in enumerate(self.questions):

            if self.user_answers[i] == q["answer"]:

                self.score += 1

        self.score_label.config(
            text=f"Score: {self.score}"
        )

    # --------------------------------------------------------
    # RESULT SCREEN
    # --------------------------------------------------------

    def show_result(self):

        self.calculate_score()

        percentage = (
            self.score /
            len(self.questions)
        ) * 100

        # Clear main area
        for widget in self.main.winfo_children():

            widget.destroy()

        result_title = tk.Label(
            self.main,
            text="QUIZ COMPLETED",
            font=("Arial", 30, "bold"),
            fg=self.accent,
            bg=self.bg
        )

        result_title.pack(
            pady=(50, 20)
        )

        score_text = tk.Label(
            self.main,
            text=f"{self.score} / {len(self.questions)}",
            font=("Arial", 50, "bold"),
            fg=self.green,
            bg=self.bg
        )

        score_text.pack(
            pady=10
        )

        percentage_label = tk.Label(
            self.main,
            text=f"Percentage: {percentage:.1f}%",
            font=("Arial", 20),
            fg=self.text,
            bg=self.bg
        )

        percentage_label.pack(
            pady=5
        )

        # Performance message
        if percentage >= 90:

            performance = "Excellent performance."

        elif percentage >= 75:

            performance = "Very good. Keep revising current affairs."

        elif percentage >= 60:

            performance = "Decent, but you need more revision."

        elif percentage >= 40:

            performance = "Weak. Revise the topics again."

        else:

            performance = "Poor. You need serious revision."

        performance_label = tk.Label(
            self.main,
            text=performance,
            font=("Arial", 15),
            fg=self.secondary,
            bg=self.bg
        )

        performance_label.pack(
            pady=10
        )

        # Buttons
        button_frame = tk.Frame(
            self.main,
            bg=self.bg
        )

        button_frame.pack(
            pady=25
        )

        review_button = tk.Button(
            button_frame,
            text="Review Answers",
            font=("Arial", 13, "bold"),
            fg="#000000",
            bg=self.accent,
            relief="flat",
            padx=20,
            pady=12,
            command=self.show_review
        )

        review_button.pack(
            side="left",
            padx=10
        )

        restart_button = tk.Button(
            button_frame,
            text="Restart Quiz",
            font=("Arial", 13, "bold"),
            fg=self.text,
            bg="#333333",
            activebackground="#444444",
            relief="flat",
            padx=20,
            pady=12,
            command=self.restart
        )

        restart_button.pack(
            side="left",
            padx=10
        )

    # --------------------------------------------------------
    # REVIEW ANSWERS
    # --------------------------------------------------------

    def show_review(self):

        review_window = tk.Toplevel(self.root)

        review_window.title("Answer Review")

        review_window.geometry("900x650")

        review_window.configure(
            bg=self.bg
        )

        title = tk.Label(
            review_window,
            text="ANSWER REVIEW",
            font=("Arial", 22, "bold"),
            fg=self.accent,
            bg=self.bg
        )

        title.pack(
            pady=20
        )

        # Scrollable area
        container = tk.Frame(
            review_window,
            bg=self.bg
        )

        container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        canvas = tk.Canvas(
            container,
            bg=self.bg,
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            container,
            orient="vertical",
            command=canvas.yview
        )

        scroll_frame = tk.Frame(
            canvas,
            bg=self.bg
        )

        scroll_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0),
            window=scroll_frame,
            anchor="nw"
        )

        canvas.configure(
            yscrollcommand=scrollbar.set
        )

        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        for i, q in enumerate(self.questions):

            user_answer = self.user_answers[i]

            correct = q["answer"]

            if user_answer == correct:

                result = "✓ CORRECT"

                result_color = self.green

            else:

                result = "✗ WRONG"

                result_color = self.red

            frame = tk.Frame(
                scroll_frame,
                bg=self.card,
                padx=15,
                pady=15
            )

            frame.pack(
                fill="x",
                pady=6
            )

            question = tk.Label(
                frame,
                text=f"{i + 1}. {q['q']}",
                font=("Arial", 12, "bold"),
                fg=self.text,
                bg=self.card,
                wraplength=780,
                justify="left"
            )

            question.pack(
                anchor="w"
            )

            status = tk.Label(
                frame,
                text=result,
                font=("Arial", 11, "bold"),
                fg=result_color,
                bg=self.card
            )

            status.pack(
                anchor="w",
                pady=(8, 2)
            )

            correct_text = tk.Label(
                frame,
                text=f"Correct answer: {q['options'][correct]}",
                font=("Arial", 11),
                fg=self.secondary,
                bg=self.card
            )

            correct_text.pack(
                anchor="w"
            )

            if user_answer is not None:

                user_text = tk.Label(
                    frame,
                    text=f"Your answer: {q['options'][user_answer]}",
                    font=("Arial", 11),
                    fg=self.secondary,
                    bg=self.card
                )

                user_text.pack(
                    anchor="w"
                )

    # --------------------------------------------------------
    # RESTART
    # --------------------------------------------------------

    def restart(self):

        # Rebuild interface
        for widget in self.main.winfo_children():

            widget.destroy()

        self.create_main_area()

        self.start_quiz()


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = QuizApp(root)

    root.mainloop()