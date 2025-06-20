import datetime

def explain_decision(text, images, detections, prompt):
    explanation = f"Extracted text based on user prompt: '{prompt}'.\n"
    explanation += f"Found {len(images)} images, analyzed for objects.\n"
    if detections:
        explanation += "Detected objects in images: "
        explanation += ", ".join([str(d['labels']) for d in detections])
    else:
        explanation += "No objects detected in images."
    return explanation
