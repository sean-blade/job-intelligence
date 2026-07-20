## Phase 1 - Core Analysis
Create an engine that analyzes job postings against a candidate profile.

**Completed:**

- [x] Project structure
- [x] Data models
- [x] Job loading
- [x] Candidate profiles
- [x] Skill extraction
- [x] Skill Normalization
- [x] Skill Alias handling
- [x] Differentiate required and preferred skills
- [x] Skill matcher engine
- [x] Skill category matcher engine
- [x] Scoring Engine
- [x] CLI commands
- [x] Text report
- [x] Automated testing

**Phase completion criteria**

A user can provide:
- candidate profile
- job posting

And receive:
- match score
- matched skills
- missing skills
- preferred skill matches
- category overlap
- explanation of match score

## Phase 2 - Intelligence Product
Turn analysis engine into something useful in job searching
Better decision making

### 2.1 Candidate Profile Management
Store user profile for modularity and so that it only needs to be created once instead of per analysis.

Features:
- [x] Candidate profile file
- [x] Configurable profile location
- [ ] Support:
    - [x] Skills
    - [ ] Education
    - [ ] Experience
    - [ ] Preferences

Example:
```text
config/
 └── candidate.json
 ```

### 2.2 Job Collection Input
Goal: Analyse multiple jobs without manually editing code

Input: 
```text
jobs/
 ├── job1.json
 ├── job2.json
 └── job3.json
 ```
or
```text
jobs.csv
 ```

Capability:
```text

Analyze an arbitrary number of job postings without changing code.
```

### 2.3 Ranking System
Identify which jobs I should focus on first

Features:
- [x] Rank by match score
- [x] Sort Results
- [ ] Filter By minimum score
- [x] Generate Ranked report

```text
Top Matches

1. Biomedical Engineer
   Match: 91%

2. Simulation Engineer
   Match: 86%
```

### 2.4 Improve Match Explanation
Understand why a job scored highly or poorly

Currently:
```text
Score: 83
Missing: CAD
```
Future:
```
Strong matches:
+ Finite Element Analysis
+ MATLAB
+ Biomedical Engineering

Concerns:
- CAD experience missing
- Requires medical device background
```
**Phase 2 Exit criteria**
The tool is able to:
- load candidate profile
- analyze many jobs
- rank them
- explain the ranking

## Phase 3 - Automation
Remove manual effort (host on server)

### 3.1 Persistent Storage

Add: SQLite database

Store:

Jobs: 
- title
- jobID 
- company
- description
- date found
- date posted / due

Analysis:
- Scores
- matched skills
- missing skills
- Education required
- Clearance (if applicable)

### 3.2 Automated job gathering
Find jobs for user

Sources:
- APIs
- RSS feeds
- Saved searches
- Manual imports

### 3.3 Scheduled Execution
System runs without intervention

Deploy:
- home server
- systemd timer
- logging
- error handling

**Phase 3 Exit criteria**
it should look something like: 
```text
Good morning.

5 new high-match jobs found.

Top recommendation:

Senior Biomedical Engineer
92% match

Reasons:
...
```

## Phase 4 - Polish
Make system portfolio ready

### 4.1 Dashboard
Possible stack:
- FastAPI backend
- SQLite
- React/vue/etc frontend

Features:
- job ranks
- history
- filters
- skill trends
- application tracker
- Save/load profile

### 4.2 Quality
Add:

- documentation
- architecture diagrams
- deployment guide
- screenshots
- demo data
- CI/CD
- Docker

## Stretch Goals
These are explicitly optional.

    NLP embeddings
    LLM explanations
    Resume parsing
    Personalized recommendations
    Learning recommendations:
    "Learn SolidWorks to increase match rate by X"
