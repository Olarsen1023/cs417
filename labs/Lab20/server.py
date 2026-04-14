"""Lab 20: Build the Other Side — Server

Your FastAPI grading server. Build each section as you work
through the tasks. The TODOs tell you what to add and where.
"""

from fastapi import FastAPI
from requests import request

app = FastAPI()


# ---------------------------------------------------------------------------
# Task 1: The Naive Server
# ---------------------------------------------------------------------------
# Import the grade function from grading.py, then create a POST /grade
# endpoint that accepts {"student": ..., "lab": ...} and returns the score.

# TODO: import grade from grading

# TODO: POST /grade endpoint

from grading import grade
##@app.post("/grade")
##def grade_endpoint(request: dict):
 ##   student = request.get("student")
 ##   lab = request.get("lab")
 ##   slow = request.get("slow", False)
 ##   score = grade(student, lab, slow)
 ##   return {"score": score, "student": student, "lab": lab}


# ---------------------------------------------------------------------------
# Task 2: Retries Reveal a Problem
# ---------------------------------------------------------------------------
# Add a grading_log list that records every grading event.
# Update POST /grade to (1) accept an optional "slow" field and pass it
# to grade(), and (2) append each grading event to the log.
# Add GET /log and POST /reset-log endpoints.

## TODO: grading_log = []
## grading_log = []

# TODO: update POST /grade to log events and support "slow"

##@app.post("/grade")
##def grade_endpoint(request: dict):
 ##   student = request.get("student")
 ##   lab = request.get("lab")
 ##   slow = request.get("slow", False)

       ## score = grade(student, lab, slow)

     ##grading_log.append({
       ## "student": student,
       ## "lab": lab,
       ## "score": score,
  ##  })
   ## print("GRADE LOG ID:", id(grading_log), "LEN:", len(grading_log))
   ## return {
     ##   "student": student,
    ##    "score": score,
     ##   "lab": lab,
    ##}

##@app.get("/log")
##def get_log():
  ##  print("LOG   LOG ID:", id(grading_log), "LEN:", len(grading_log))
  ## return {"entries": grading_log}

##@app.post("/reset-log")
##def reset_log():
##    grading_log.clear()
#    return {"message": "Log reset."}



# ---------------------------------------------------------------------------
# Task 3: Idempotency Makes Retries Safe
# ---------------------------------------------------------------------------
# Add a completed dict that maps submission IDs to results.
# Update POST /grade to check for an optional "submission_id" field —
# if the ID is already in completed, return the cached result without
# grading again or logging.
# Add POST /reset-completed endpoint.

# TODO: completed = {}
completed = {}


# TODO: update POST /grade to check submission_id
@app.post("/grade")
def grade_endpoint(request: dict):
    student = request.get("student")
    lab = request.get("lab")
    slow = request.get("slow", False)
    submission_id = request.get("submission_id")

    if submission_id and submission_id in completed:
        return {
            "student": student,
            "lab": lab,
            "score": completed[submission_id],
            }

    score = grade(student, lab, slow)
    grading_log.append({"student": student, "lab": lab, "score": score})

    if submission_id:
        completed[submission_id] = score

    return {
        "student": student,
        "lab": lab,
        "score": score,

    }


# ---------------------------------------------------------------------------
# Task 4: Honest About Time
# ---------------------------------------------------------------------------
# You'll need: from fastapi import BackgroundTasks
#              from fastapi.responses import JSONResponse
#
# Add jobs dict, job_submission_map dict, and a job ID generator.
# Create POST /grade-async (returns 202, runs grading in background).
# Create a run_grade_job helper that does the actual grading.
# Create GET /grade-jobs/{job_id} to check job status.

# TODO: jobs = {}
jobs = {}
# TODO: job_submission_map = {}
job_submission_map = {}

# TODO: POST /grade-async endpoint
from fastapi import BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
@app.post("/grade-async")
def grade_async(request: dict, background_tasks: BackgroundTasks):
    student = request.get("student")
    lab = request.get("lab")
    slow = request.get("slow", False)
    submission_id = request.get("submission_id")

    job_id = len(jobs) + 1
    jobs[job_id] = {"status": "pending", "result": None}
    job_submission_map[job_id] = submission_id

    background_tasks.add_task(run_grade_job, job_id, student, lab, slow)

    return JSONResponse(content={"job_id": job_id}, status_code=202)

# TODO: run_grade_job helper function
def run_grade_job(job_id: int, student: str, lab: str, slow: bool):
    score = grade(student, lab, slow)
    jobs[job_id] = {"status": "completed", "result": score}


# TODO: GET /grade-jobs/{job_id} endpoint
@app.get("/grade-jobs/{job_id}")
def get_grade_job(job_id: int):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return {"job_id": job_id, "status": jobs[job_id]["status"], "result": jobs[job_id]["result"]}