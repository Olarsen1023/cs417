"""Lab 20: Build the Other Side — Server

Your FastAPI grading server. Build each section as you work
through the tasks. The TODOs tell you what to add and where.
"""

from fastapi import Body, FastAPI
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


grading_log = []
completed = {}

##@app.post("/grade")
##def grade_endpoint(request: dict = Body(...)):
##    student = request.get("student")
#    lab = request.get("lab")
#    slow = request.get("slow", False)
#    submission_id = request.get("submission_id")

#    if submission_id and submission_id in completed:
#        return {
#            "student": student,
#            "lab": lab,
#            "score": completed[submission_id],
#        }

#   score = grade(student, lab, slow)

#    grading_log.append({
#        "student": student,
#        "lab": lab,
#        "score": score,
#    })

#    if submission_id:
#        completed[submission_id] = score

#    return {
#        "student": student,
#        "lab": lab,
#        "score": score,
#    }

@app.get("/log")
def get_log():
    return {"entries": grading_log}

@app.post("/reset-log")
def reset_log():
    grading_log.clear()
    return {"message": "Log reset."}

@app.post("/reset-completed")
def reset_completed():
    completed.clear()
    return {"message": "Completed submissions reset."}

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


from fastapi import BackgroundTasks, Body, HTTPException
from fastapi.responses import JSONResponse

jobs = {}
job_submission_map = {}
next_job_id = 1


def run_grade_job(job_id: str, student: str, lab: int, slow: bool):
    score = grade(student, lab, slow)

    jobs[job_id] = {
        "status": "complete",
        "result": {
            "student": student,
            "lab": lab,
            "score": score,
        },
    }

    grading_log.append({
        "student": student,
        "lab": lab,
        "score": score,
    })

@app.post("/grade-async")
def grade_async(
    request: dict = Body(...),
    background_tasks: BackgroundTasks = None,
):
    global next_job_id

    student = request.get("student")
    lab = request.get("lab")
    slow = request.get("slow", False)
    submission_id = request.get("submission_id")

  
    if submission_id and submission_id in job_submission_map:
        job_id = job_submission_map[submission_id]
        return JSONResponse(
            status_code=202,
            content={"job_id": job_id, "status": "accepted"},
        )

    job_id = str(next_job_id)
    next_job_id += 1

    jobs[job_id] = {"status": "pending"}

    if submission_id:
        job_submission_map[submission_id] = job_id

    background_tasks.add_task(
        run_grade_job, job_id, student, lab, slow
    )

    return JSONResponse(
        status_code=202,
        content={"job_id": job_id, "status": "accepted"},
    )


@app.get("/grade-jobs/{job_id}")
def get_grade_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[job_id]

    response = {
        "job_id": job_id,
        "status": job["status"],
    }

    if job["status"] == "complete":
        response["result"] = job["result"]

    return response


