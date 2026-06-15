from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from privacy_engine import HIPAAShield

# 1. Initialize the FastAPI agent application
app = FastAPI(
    title="Healthcare AI Security Agent",
    description="A local proxy agent that sanitizes PHI/PII before cloud transit.",
    version="1.0.0"
)

# Initialize your existing privacy shield
shield = HIPAAShield()

# 2. Define what the incoming data structure looks like
class DataPayload(BaseModel):
    text: str

# 3. Create a health-check endpoint to see if the agent is alive
@app.get("/health")
def health_check():
    return {"status": "healthy", "agent_mode": "local_proxy"}

# 4. Create the core security interceptor endpoint
@app.post("/v1/sanitize")
def sanitize_data(payload: DataPayload):
    if not payload.text:
        raise HTTPException(status_code=400, detail="Text payload cannot be empty.")
    
    # Run your local Microsoft Presidio scrubbing logic
    sanitized_text = shield.sanitize_clinical_notes(payload.text)
    
    # Return the clean text to the local application
    return {
        "original_length": len(payload.text),
        "sanitized_text": sanitized_text,
        "status": "SECURE_FOR_TRANSIT"
    }

# 5. Run the server locally on port 8000 when executed
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)